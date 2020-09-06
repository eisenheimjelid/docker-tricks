FROM python:3.8.1-alpine3.10

LABEL "com.github.actions.name"="Modificar el README desde archivos externos"
LABEL "com.github.actions.description"="Generar automaticamente cambios al README desde archivos de texto json"
LABEL "com.github.actions.icon"="corner-up-left"
LABEL "com.github.actions.color"="red"

LABEL "repository"="https://github.com/eisenheimjelid/docker-tricks"
LABEL "homepage"="https://www.davfl.com.mx/"
LABEL "maintainer"="Jelid Leon <jelid.leon@gmail.com>"

ADD main.py /main.py
ENTRYPOINT ["python", "/main.py"]