#1: Выделение бизнес-логики в отдельный слой

До рефакторинга:

# views.py
def process_order(request):
    # Получение данных из запроса
    # Валидация данных
    # Создание заказа в базе данных
    # Отправка email-уведомления
    # Возврат ответа

После рефакторинга:

# views.py
from .services import OrderService

def process_order(request):
    # Получение данных из запроса
    order_data = request.POST
    
    order_service = OrderService()
    order = order_service.create_order(order_data)
    
    return render(request, 'order_success.html', {'order': order})

# services.py
from .models import Order
from .notifications import send_order_notification

class OrderService:
    def create_order(self, order_data):
        # Валидация данных
        # Создание заказа в базе данных
        order = Order.objects.create(**order_data)
        
        # Отправка email-уведомления
        send_order_notification(order)
        
        return order

Границы:
- Явные границы через интерфейс `OrderService`, который инкапсулирует логику создания заказа.
- Неявные границы через документацию, описывающую назначение и использование `OrderService`.

Влияние на другие части системы:
- `views.py` теперь делегирует создание заказа сервису `OrderService`, что упрощает код представления и делает его более читаемым.
- `services.py` содержит бизнес-логику создания заказа, включая валидацию данных, сохранение в базу данных и отправку уведомлений. Эта логика может быть переиспользована в других частях системы.

Тест:

# tests.py
def test_create_order():
    # Подготовка тестовых данных
    order_data = {
        'customer_name': 'John Doe',
        'total_amount': 100.0,
        # ...
    }
    
    # Вызов сервиса создания заказа
    order_service = OrderService()
    order = order_service.create_order(order_data)
    
    # Проверка результата
    assert order.customer_name == 'John Doe'
    assert order.total_amount == 100.0
    # ...
    
    # Проверка отправки уведомления
    assert_email_sent(to=order.customer_email, subject='Order Confirmation')





#2: Выделение логики работы с внешним API в отдельный модуль

До рефакторинга:

# utils.py
import requests

def fetch_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    # Обработка данных
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    return temperature, humidity, description

def get_weather_summary(city):
    temperature, humidity, description = fetch_weather_data(city)
    summary = f"Temperature: {temperature}°C, Humidity: {humidity}%, Description: {description}"
    return summary

После рефакторинга:

# weather_api.py
import requests

class WeatherAPI:
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    API_KEY = 'YOUR_API_KEY'
    
    def fetch_weather_data(self, city):
        url = f'{self.BASE_URL}?q={city}&appid={self.API_KEY}'
        response = requests.get(url)
        data = response.json()
        return data

# weather_service.py
from .weather_api import WeatherAPI

class WeatherService:
    def __init__(self):
        self.weather_api = WeatherAPI()
    
    def get_weather_summary(self, city):
        weather_data = self.weather_api.fetch_weather_data(city)
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        summary = f"Temperature: {temperature}°C, Humidity: {humidity}%, Description: {description}"
        return summary

# utils.py
from .weather_service import WeatherService

def get_weather_info(city):
    weather_service = WeatherService()
    weather_summary = weather_service.get_weather_summary(city)
    return weather_summary
```

Границы:
- Явные границы через классы `WeatherAPI` и `WeatherService`, которые инкапсулируют логику взаимодействия с внешним API погоды и обработку данных.

Влияние:
- `utils.py` теперь использует `WeatherService` для получения сводки погоды, что упрощает код и делает его более читаемым.
- `weather_api.py` содержит логику взаимодействия с внешним API погоды, включая формирование URL-адреса и получение данных. Эта логика может быть переиспользована в других частях системы.
- `weather_service.py` содержит логику обработки данных погоды и формирования сводки. Этот сервис может быть использован в различных частях системы, где требуется информация о погоде.


В данном примере рефакторинга выделена логика работы с внешним API погоды в отдельный класс WeatherAPI, который инкапсулирует детали взаимодействия с API, такие как базовый URL-адрес, API-ключ и выполнение HTTP-запросов. Это позволяет изолировать эту логику от остальной части системы и делает ее более переиспользуемой.





#3 с рефакторингом логики работы с базой данных.

До рефакторинга:

# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # ...

# views.py
from .models import User

def create_user(request):
    # Получение данных из запроса
    name = request.POST['name']
    email = request.POST['email']
    # ...
    
    # Создание пользователя в базе данных
    user = User(name=name, email=email)
    user.save()
    
    return render(request, 'user_created.html', {'user': user})

def get_user(request, user_id):
    # Получение пользователя из базы данных
    user = User.objects.get(id=user_id)
    
    return render(request, 'user_details.html', {'user': user})

После рефакторинга:

# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # ...

# repositories.py
from .models import User

class UserRepository:
    def create(self, name, email):
        user = User(name=name, email=email)
        user.save()
        return user
    
    def get_by_id(self, user_id):
        user = User.objects.get(id=user_id)
        return user

# services.py
from .repositories import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
    
    def create_user(self, name, email):
        user = self.user_repository.create(name, email)
        return user
    
    def get_user_by_id(self, user_id):
        user = self.user_repository.get_by_id(user_id)
        return user

# views.py
from .services import UserService

def create_user(request):
    # Получение данных из запроса
    name = request.POST['name']
    email = request.POST['email']
    # ...
    
    user_service = UserService()
    user = user_service.create_user(name, email)
    
    return render(request, 'user_created.html', {'user': user})

def get_user(request, user_id):
    user_service = UserService()
    user = user_service.get_user_by_id(user_id)
    
    return render(request, 'user_details.html', {'user': user})

Границы:
- Явные границы через классы `UserRepository` и `UserService`, которые инкапсулируют логику работы с моделью `User` и предоставляют четкий интерфейс для создания и получения пользователей.

Влияние:
- `views.py` теперь использует `UserService` для создания и получения пользователей, что упрощает код представлений и делает его более читаемым.
- `repositories.py` содержит логику работы с моделью `User` на уровне базы данных, включая создание и получение пользователей. Этот репозиторий может быть использован в различных частях системы, где требуется доступ к данным пользователей.
- `services.py` содержит бизнес-логику, связанную с пользователями, и использует `UserRepository` для доступа к данным. Этот сервис предоставляет высокоуровневые методы для работы с пользователями и может быть использован в других частях системы.









