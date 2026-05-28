# CoSync

Проект, нацеленный на создание среды сопоставления двух систем электронных ведомостей – ведомости ВладиВостокского Государственного Университета и Колледжа Информационных и Креативных Технологий

### Интерфейс приложения
Интерфейс имеет как светлую, так и тёмную тему для удобства преподавателя

![light-theme](https://github.com/Gustavs3n22/CoSync/blob/main/static/light.png)
![dark-theme](https://github.com/Gustavs3n22/CoSync/blob/main/static/dark.png)

### Развёртывание
В папке data-legacy находится .sql файл plain формата для восстановления в PostgreSQL базу данных. Данные для подключения неоюходимо будет изменить в файле db.py (переменная DATABASE_URL)

Необходимые Python библиотеки можно установить используя pip install на файл requirements.txt:
**pip install -r requirements.txt**

Проект запускается командой:
**uvicorn main:app --reload**
