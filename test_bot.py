import requests

# URL эндпоинта
url = 'http://localhost:8000/markets/process-market-data/'


# Пример данных для создания или обновления маркета
data = """Название филиала: Навои
Номер отдела гриль: 93 380 15 11
Городской номер магазина:553511318
Режим работы магазина: 08:00-00:00
===============================
Менеджер магазина: Пардаев Фаррухжон Уктамович
Режим работы: 11:00-19:00
Выходной день: вторник 
Контактный номер:983380868


№1 супервайзер магазина:Якубова Махфуза
Режим работы:08:00-16:00
Выходной день:четверг 
Контактный номер:942512566


№2 супервайзер магазина:Рузибаев Акмаль
Режим работы:16:00-00:00
Выходной день:среда 
Контактный номер:973783828

"""

# Отправка POST-запроса
response = requests.post(url, headers={'Content-Type': 'text/plain'}, data=data)

# Проверка ответа
print(f"Status Code: {response.status_code}")
print(response.json())