import json

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse
from rest_framework import generics, viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from . import models
from .forms import UserForm, ProfileForm, LoginForm
from .models import Vegetable, Fruit, Meat, Grain, Profile, Record
from .serializers import ProfileSerializer, VegetableSerializer, RecordSerializer
from .utils import get_context_data, get_cpfc, add_product_to_table, remove_product_from_table, get_products, load_table


# class ProfileViewSet(viewsets.ModelViewSet):
#     # queryset = Vegetable.objects.all()
#     serializer_class = ProfileSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Profile.objects.all()
#         return Profile.objects.filter(pk=pk)

    # @action(methods=['get'], detail=True)
    # def fruit(self, request, pk=None):
    #     fruit = Fruit.objects.get(pk=pk)
    #     return Response({'fruit': fruit.name})

class ProfileAPIList(generics.ListCreateAPIView):
    queryset = Profile.objects.filter((Q(name__startswith='П') | Q(name__startswith='А')) & ~Q(age__lte=20))
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
class ProfileAPIDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, )

class VegetableViewSet(viewsets.ModelViewSet):
    queryset = Vegetable.objects.filter((Q(name__startswith='Б') | Q(name__startswith='А')) & ~Q(calories__lte=30))
    serializer_class = VegetableSerializer
    @action(detail=False)
    def some_vegs(self, request):
        vegs = Vegetable.objects.all().order_by('-calories')

        serializer = self.get_serializer(vegs, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['post'])
    def add_veg(self, request, pk=None):
        serializer = VegetableSerializer(data=request.data)
        if serializer.is_valid():
            valid_fields = [field.name for field in Vegetable._meta.get_fields()]
            valid_vegetable_data = {key: request.data[key] for key in valid_fields if key in request.data}
            vegetable = Vegetable.objects.create(**valid_vegetable_data).save()
            # Vegetable.objects.create(request.data).save()
            return Response({'status': 'Vegetable added'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # filterset_fields = ['name', 'fats']

# class FruitViewSet(viewsets.ModelViewSet):
#     queryset = Fruit.objects.filter((Q(name__startswith='Б') | Q(name__startswith='А')) & ~Q(calories__lte=30))
#     serializer_class = FruitSerializer

class RecordAPIList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    def get_queryset(self):
        veg_id = self.kwargs['veg_id']
        user = self.request.user
        profile = Profile.objects.get(user_id=user)
        return Record.objects.filter(user_id=profile, veg_id=veg_id)

class RecordQueryAPIList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user_id=user)
        veg_id = self.request.query_params.get('veg_id')
        if veg_id is not None:
            return Record.objects.filter(user_id=profile, veg_id=veg_id)
        return Record.objects.filter(user_id=profile)

# class VegetableAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vegetable.objects.all()
#     serializer_class = VegetableSerializer

# class VegetableAPIView(APIView):
#     def get(self, request):
#         v = Vegetable.objects.all()
#         return Response({'veg': VegetableSerializer(v, many=True).data})
#
#     def post(self, request):
#         serializer = VegetableSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'veg': serializer.data})
#
#     # позиционные и именнованные аргументы
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT is not allowed"})
#         try:
#             instance = Vegetable.objects.get(pk=pk)
#         except:
#             return Response({"error": "Objects does not exist"})
#         serializer = VegetableSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"veg": serializer.data})


# class VegetableAPIView(generics.ListAPIView):
#     queryset = Vegetable.objects.all()
#     serializer_class = VegetableSerializer


def index(request):
    context = get_context_data(title="Главная", active_url='home')
    return render(request, 'main/index.html', context)


@ensure_csrf_cookie
def calculator(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        product_id = body.get('product_id', None)
        product_table = body.get('product_table', None)

        if product_id and product_table:
            result = add_product_to_table(request, product_table, product_id)
            return JsonResponse(result)
        return JsonResponse({'status': 'fail'})

    elif request.user.is_authenticated:
        result = get_products(request)
        products = result[0]
        total = result[1]
        cpfc = get_cpfc(request)
        vegetables = Vegetable.objects.all()

        context = get_context_data(title="Калькулятор", active_url='calculator', products_list=products,
                                   products_list2=vegetables, products_list_len=len(products), total=total, cpfc=cpfc)

    else:
        vegetables = Vegetable.objects.all()

        context = get_context_data(title="Калькулятор", active_url='calculator', products_list=vegetables)
    return render(request, 'main/calc.html', context)


def products(request):
    vegetables = Vegetable.objects.all()
    fruits = Fruit.objects.all()
    grains = Grain.objects.all()
    meat = Meat.objects.all()

    context = get_context_data(title="Продукты", active_url='products', products=[
        {'title': 'Овощи', 'list': vegetables},
        {'title': 'Фрукты', 'list': fruits},
        {'title': 'Крупы', 'list': grains},
        {'title': 'Мясо', 'list': meat},
    ])

    return render(request, 'main/products.html', context)


def profile(request):
    cpfc = get_cpfc(request)
    context = get_context_data(title="Профиль", active_url='profile', cpfc=cpfc)
    return render(request, 'main/profile.html', context)


def registration(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            profile.user_id = user
            profile.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    context = get_context_data(title="Регистрация", active_url='registration', user_form=user_form,
                               profile_form=profile_form)
    return render(request, 'main/reg.html', context)


def authentication(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        login_form = LoginForm()
    context = get_context_data(title="Вход", active_url='authentication', login_form=login_form)
    return render(request, 'main/auth.html', context)


def exit_account(request):
    logout(request)
    return redirect('home')


def get_data(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        value = body['value']

        result = load_table(value)
        new_products = result[0]
        tbody_id = result[1]

        return JsonResponse({'status': 'success', 'products': new_products, 'tbody_id': tbody_id})
    return redirect('home')


def remove_product(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        record_id = body.get('record_id', None)

        if record_id:
            result = remove_product_from_table(request, record_id)
            if result == 'success':
                return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'})
    return redirect('home')
