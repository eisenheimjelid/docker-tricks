# docker-tricks
Tricks, or maybe snippets :) 
- ### Entrar al contenedor con shell (bash)
Desde la consola, se ejecuta el siguiente comando para acceder a la terminal dentro del contenedor. Es muy útil cuando tenemos contenedores tipo Linux.

```console
~# docker exec -it container_name /bin/bash
```
