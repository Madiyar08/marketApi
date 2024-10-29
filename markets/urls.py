from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from markets.views import MarketViewSet, handle_text_data
from .views import login_view

router = DefaultRouter()
router.register(r'markets', MarketViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('api/', include(router.urls)),  # Подключаем маршруты API
    path('markets/process-market-data/', handle_text_data, name='process-market-data'),  # Обработчик текстовых данных
]
