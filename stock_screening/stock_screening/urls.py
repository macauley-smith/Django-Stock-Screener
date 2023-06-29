from django.contrib import admin
from django.urls import include, path
from stocks.views import get_stock_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', get_stock_data, name='get_stock_data'),
    path('', get_stock_data, name='home'),
]

