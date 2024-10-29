from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Market
from .serializers import MarketSerializer
from .serializers import UserLoginSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

@api_view(['POST'])
def handle_text_data(request):
    if request.method == 'POST':
        text_data = request.body.decode('utf-8')
        try:
            # Разделение данных на строки
            lines = text_data.strip().split('\n')
            market_data = {}

            # Обработка каждой строки
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    market_data[key.strip()] = value.strip()

            # Извлечение имени рынка для поиска или создания записи
            market_name = market_data.get('Название филиала')

            # Получение текущих данных из базы или создание новой записи
            market, created = Market.objects.get_or_create(market_name=market_name)

            # Создание словаря для обновления только предоставленных данных
            updates = {}
            fields_to_update = [
                'Адрес маркета',
                'Ориентир',
                'Режим работы магазина',
                'Городской номер магазина',
                'Номер отдела гриль',
                'Менеджер магазина Ф.И.',
                'Режим работы менеджера',
                'Выходной день менеджера',
                'Контактный номер менеджера',
                '№1 супервайзер магазина Ф.И.',
                'Контактный номер супервайзера 1',
                'Режим работы супервайзера 1',
                'Выходной день супервайзера 1',
                '№2 супервайзер магазина Ф.И.',
                'Контактный номер супервайзера 2',
                'Режим работы супервайзера 2',
                'Выходной день супервайзера 2',
                '№3 супервайзер магазина Ф.И.',
                'Контактный номер супервайзера 3',
                'Режим работы супервайзера 3',
                'Выходной день супервайзера 3',
                'Дополнительная информация'
            ]

            for field in fields_to_update:
                if field in market_data:
                    # Преобразование названия поля в название атрибута модели
                    model_field_name = convert_field_name(field)
                    updates[model_field_name] = market_data[field]

            # Обновление только если есть данные для обновления
            for key, value in updates.items():
                setattr(market, key, value)
            market.save()

            message = "Market updated successfully."

            return Response({"message": message}, status=200)

        except Exception as e:
            return Response({"error": str(e)}, status=500)

def convert_field_name(field_name):
    # Словарь для преобразования имен полей
    mapping = {
        'Адрес маркета': 'market_address',
        'Ориентир': 'market_orientation',
        'Режим работы магазина': 'market_work_time',
        'Городской номер магазина': 'market_phone',
        'Номер отдела гриль': 'market_grill',
        'Менеджер магазина Ф.И.': 'manager_full_name',
        'Режим работы менеджера': 'manager_work_time',
        'Выходной день менеджера': 'manager_day_off',
        'Контактный номер менеджера': 'manager_phone',
        '№1 супервайзер магазина Ф.И.': 'supervisor_one_full_name',
        'Контактный номер супервайзера 1': 'supervisor_one_phone',
        'Режим работы супервайзера 1': 'supervisor_one_work_time',
        'Выходной день супервайзера 1': 'supervisor_one_day_off',
        '№2 супервайзер магазина Ф.И.': 'supervisor_two_full_name',
        'Контактный номер супервайзера 2': 'supervisor_two_phone',
        'Режим работы супервайзера 2': 'supervisor_two_work_time',
        'Выходной день супервайзера 2': 'supervisor_two_day_off',
        '№3 супервайзер магазина Ф.И.': 'supervisor_three_full_name',
        'Контактный номер супервайзера 3': 'supervisor_three_phone',
        'Режим работы супервайзера 3': 'supervisor_three_work_time',
        'Выходной день супервайзера 3': 'supervisor_three_day_off',
        'Дополнительная информация': 'additional_info',
    }
    return mapping.get(field_name)

# Представление для API
class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


@api_view(['POST'])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)

    if user is not None:
        # Если аутентификация прошла успешно
        return Response({"success": True, "token": "ваш_токен"}, status=status.HTTP_200_OK)
    else:
        return Response({"success": False, "message": "Неправильное имя пользователя или пароль"},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)