# Daily Planner Backend

## **Описание проекта**
Это бэкенд-приложение для ежедневника. Позволяет:

- Создавать задачи
- Редактировать задачи
- Удалять задачи
- Просматривать список задач
- Отмечать задачи как выполненные

Все данные хранятся в базе данных **PostgreSQL**.

## **Технологии**
- Python 3  
- Django + Django REST Framework  
- PostgreSQL  

> Примечание: API реализовано с использованием Django REST Framework. Несмотря на упоминание FastAPI/Flask в задании, DRF полностью подходит для демонстрации CRUD операций и работы с базой данных.

## **Установка и запуск локально**
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/bakhvalov4/test_daily_planner_backend
   cd backend```

2. Создайте и активируйте виртуальное окружение:
   ```python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows```

3. Установите зависимости
   ```pip install -r requirements.txt```

4. Настройте базу данных PostgreSQL, создайте базу данных как в settings.py и создайте пользователя с паролем, как в settings.py

5. Выполните миграции
   ```python manage.py migrate```

6. Запустите сервер 
   ```python manage.py runserver```


## **Работа с API**

Получить список задач
   ```GET
   /api/daily/```

Создать новую задачу
   ```POST
   /api/daily/```
Тело запроса (JSON):
   ```{
     "title": "Купить продукты",
     "description": "Молоко, хлеб, яйца"
      }```

Отметить задачу как выполненную/невыполненную
   ```POST
   /api/daily/{id}/worked_out/{id}```

Редактировать задачу
   ```PUT
   /api/daily/{id}/```

Удалить задачу
   ```DELETE
   /api/daily/{id}/```