from django.shortcuts import get_object_or_404
from .models import Vegetable, Fruit, Meat, Grain, Record

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Калькулятор', 'url_name': 'calculator'},
    {'title': 'Продукты', 'url_name': 'products'},
]


def get_context_data(**kwargs):
    context = kwargs
    context['menu'] = menu
    return context


def get_cpfc(request):
    user = request.user
    cals = int(10 * user.profile.weight + 6.25 * user.profile.height - 5 * user.profile.age + 5)
    proteins = int(cals * 0.3 / 4)
    fats = int(cals * 0.3 / 9)
    crbs = int(cals * 0.4 / 4)
    cpfc = {
        'cals': cals,
        'proteins': proteins,
        'fats': fats,
        'crbs': crbs,
    }
    return cpfc


def add_product_to_table(request, product_table, product_id):
    pr = Record.objects.create(user_id=request.user.profile)
    match product_table:
        case 'vegetables':
            pr.veg_id.add(get_object_or_404(Vegetable, pk=product_id))
        case 'fruits':
            pr.fruit_id.add(get_object_or_404(Fruit, pk=product_id))
        case 'grains':
            pr.grain_id.add(get_object_or_404(Grain, pk=product_id))
        case 'meat':
            pr.meat_id.add(get_object_or_404(Meat, pk=product_id))
    pr.save()
    return {'status': 'success', 'id': pr.pk}


def remove_product_from_table(request, record_id):
    pr = Record.objects.get(id=record_id)
    pr.delete()
    return 'success'


def get_products(request):
    records = Record.objects.filter(user_id=request.user.profile)

    products = []

    for record in records:
        for r in record.veg_id.all(): products.append([record.pk, r])
        for r in record.fruit_id.all(): products.append([record.pk, r])
        for r in record.grain_id.all(): products.append([record.pk, r])
        for r in record.meat_id.all(): products.append([record.pk, r])

    cals = 0
    proteins = 0
    fats = 0
    carbohydrates = 0

    for product in products:
        cals += product[1].calories
        proteins += product[1].proteins
        fats += product[1].fats
        carbohydrates += product[1].carbohydrates

    total = {
        'calories': cals,
        'proteins': round(proteins, 1),
        'fats': round(fats, 1),
        'carbohydrates': round(carbohydrates, 1)
    }

    return [products, total]


def load_table(value):
    match value:
        case 'vegs':
            tbody_id = 'vegetables'
            products = Vegetable.objects.all()
        case 'fruits':
            tbody_id = 'fruits'
            products = Fruit.objects.all()
        case 'grains':
            tbody_id = 'grains'
            products = Grain.objects.all()
        case 'meat':
            tbody_id = 'meat'
            products = Meat.objects.all()

    new_products = []
    for product in products:
        p = []
        p.append(product.id)
        p.append(product.name)
        p.append(product.calories)
        p.append(product.proteins)
        p.append(product.fats)
        p.append(product.carbohydrates)

        new_products.append(p)

    return [new_products, tbody_id]