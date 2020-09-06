# docker-tricks
Tricks, or maybe snippets :) 
- ### Entrar al contenedor con shell (bash)
Desde la consola, se ejecuta el siguiente comando para acceder a la terminal dentro del contenedor. Es muy útil cuando tenemos contenedores tipo Linux.

```console
~# docker exec -it container_name /bin/bash
```
- ### Exportar la base de datos Docker-Postgresql
Exportar desde un contenedor de Docker, con postgresql la base de datos a una salida estandar con SQL

```console
~# docker exec -t container_name pg_dumpall -c -U postgres
```
- ### Importar una base de datos Docker-Postgresql
Importar desde un archivo con SQL, a un contenedor de Docker, con postgresql.

```console
~# cat your_dump.sql | docker exec -i container_name psql -U postgres
```
