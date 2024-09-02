# Используем образ Python 3.11
FROM python:3.11.9

# создать директорию /code
WORKDIR /number_generator

# скопировать файл requirements.txt из директории, в которой лежит докерфайл, в директорию /code
COPY ./requirements.txt /number_generator/requirements.txt

# выполнить команду (как в терминале, с тем же синтаксисом) для установки пакетов из requirements.txt
RUN pip install --no-cache-dir --upgrade -r /number_generator/requirements.txt

# скопировать всё содержимое директории, в которой лежит докерфайл, в директорию /code
COPY ./main /number_generator/main
COPY ./number_generator /number_generator/number_generator
COPY ./staticfiles /number_generator/staticfiles
COPY ./.env /number_generator/.env
COPY ./db.sqlite3 /number_generator/db.sqlite3
COPY ./manage.py /number_generator/manage.py

RUN python -m pip install -U channels["daphne"]
#COPY . /number_generator

#ENV PYTHONPATH=/number_generator:/number_generator/main
# Открытие порта
EXPOSE 8080

# Указываем команду для запуска приложения
CMD daphne -b 0.0.0.0 -p 8000 number_generator.asgi:application
