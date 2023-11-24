from django.urls import path
from .views import index, calculator, products, registration, authentication, exit_account, profile, \
    get_data, remove_product

urlpatterns = [
    path('', index, name='home'),
    path('calc/', calculator, name='calculator'),
    path('products/', products, name='products'),
    path('reg/', registration, name='registration'),
    path('auth/', authentication, name='authentication'),
    path('exit/', exit_account, name='exit'),
    path('profile/', profile, name='profile'),
    path('get_data/', get_data, name='get_data'),
    path('remove_product/', remove_product, name='remove_product'),
]
