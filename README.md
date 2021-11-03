# Проект Yamdb

Yamdb - это база отзывов о фильмах, книгах и музыке. Здесь пользователь может оставить отзыв (Review) и выставить рейтинг произведению (Title). 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». При этом список категорий (Category) может быть расширен. Сами произведения в YaMDb не хранятся.

## Используемые технологии

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Palashnenkoff/REST-API-YaMDb.git

cd REST-API-YaMDb
```

Cоздать и активировать виртуальное окружение (для Windows):
###### * для Mac или Linux 'python3 -m venv venv'  
```
python -m venv venv
```
###### * для Mac или Linux 'source venv/bin/activate' 
```
source venv/Scripts/activate 
```
Обновить pip и установить зависимости:
```
python -m pip install --upgrade pip

pip install -r requirements.txt
```
Зайти в директорию приложения и выполнить миграции:
```
cd api_yamdb

python manage.py migrate
```
Вам может пригодиться супер-пользователь - он позволяет быстро и удобно создавать пользователей, посты, комментарии и другие сущности.
Для этого вам будет, находясь в директории `secure_blog/secure_blog/`, выполнить следующие команды:
```
python manage.py createsuperuser
```
Запустить проект:
```
python manage.py runserver
```

Панель админа будет доступна по ссылке: `localhost:8000/admin/`

Для знакомства со всем возможностями проекта запустите локальный сервер и посетите [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
