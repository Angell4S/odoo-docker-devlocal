##asdasdasd

# Instalación y Configuración Inicial

## Preparación Inicial
1. Instalar docker -> https://docs.docker.com/get-docker/
2. Instalar docker-compose -> https://docs.docker.com/compose/install/

## Instalación de Odoo con docker
1. Descargar el repositorio
~~~
git clone link
~~~
2. Ingresar a la carpeta 
~~~
cd odoo-docker-devlocal
~~~
3. Crear archivo .env y docker-compose.yaml
~~~
cp copy.env .env
cp copy.docker-compose.yaml docker-compose.yaml
~~~
4. Editar parámetros de .env
~~~
Ejemplo:
WEB_HOST=dev_odoo_empresa1 
WEB_PORT=8087
~~~
5. Opcional: Editar docker-compose.yaml, esto siempre y cuando se requiera añadir nuevos servicios o modificar parámetros.
6. Ejecutar docker-compose
~~~
docker-compose up -d
