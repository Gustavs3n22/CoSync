# CoSync

Проект, нацеленный на создание среды сопоставления двух систем электронных ведомостей – ведомости ВладиВостокского Государственного Университета и Колледжа Информационных и Креативных Технологий

<img width="1725" height="910" alt="image" src="https://github.com/user-attachments/assets/3aa44b27-b8c9-43e1-9021-59cce7b285fc" />

<img width="1650" height="902" alt="image" src="https://github.com/user-attachments/assets/5cba1016-4ba6-4278-99c2-2898441f41ba" />

<img width="1663" height="863" alt="image" src="https://github.com/user-attachments/assets/b3a69bd6-f911-44d8-832c-9427ba942071" />

### Развёртывание
В папке data-legacy находится .sql файл plain формата для восстановления в PostgreSQL базу данных. Данные для подключения неоюходимо будет изменить в файле db.py (переменная DATABASE_URL)

Необходимые Python библиотеки можно установить используя pip install на файл requirements.txt:
**pip install -r requirements.txt**

Проект запускается командой:
**uvicorn main:app --reload**
