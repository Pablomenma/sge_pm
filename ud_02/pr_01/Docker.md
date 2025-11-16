# SISTEMAS DE GESTIÓN EMPRESARIAL

## Unidad de Trabajo:          UT02. Instalación y configuración de un ERP

### Práctica:                   PR0201: Entorno de producción de desarrollo contenerizado


Con esta práctica vamos a ser si has comprendido bien los conceptos de Docker Compose. El objetivo será, partiendo del fichero compose.yml facilitado por el profesor, levantar un entorno de contenedores que tenga una instalación de Odoo para desarrollo y otra para producción. Las características de este entorno serán:

El fichero compose tendrá 4 servicios: dos con Postgres (desarrollo y producción) y dos con Odoo (desarrollo y producción)
El entorno de producción únicamente tendrá mapeado el volumen /mnt/extra/addons mientras que el de desarrollo tendrá los 4 directorios que vimos en la exposición del tema (addons, filestore, sessions y base de datos).
Es decisión tuya qué puertos mapearás a la máquina física.
Entrega
Debes documentar los pasos tomados, así como entregar el fichero compose.yml que hayas creado.



### Documentación 


Como nos indica el enunciado, el archivo *Compose.yml* contará con cuatro servicios,  (postgres_A, odooA ,postgres_B y odooB ) .


1. Entorno de desarrollo : 
El servicio postgres_A ofrece una base de datos PostgreSQL para Odoo. Dentro del servicio definimos los datos para la imagen, el nombre del contenedor, las variables de entorno (el nombre de nuestra base de datos, usuario y contraseña), el volumen que mapearemos fuera del contenedor .


Con odooA levantaremos una instancia de Odoo 16 que se conectará a la base de datos del servicio que hemos creado en el paso anterior.  A la hora de crearlo, tenemos que definir los datos para la imagen, el nombre del contenedor, las variables de entorno (nombre de la base de datos, usuario y contraseña), los puertos donde podremos visualizar la interfaz (8069 si utilizamos la máquina física), los volúmenes donde se cargarán los módulos adicionales, el volumen donde se guardarán los archivos que generé Odoo, las dependencias y el comando para activar el modo desarrollador completo.

2.  Entorno de produccion.
El servicio postgres_B ofrece una base de datos PostgreSQL para Odooen el entorno de producción. Dentro del servicio definimos los datos para la imagen, el nombre del contenedor, las variables de entorno (el nombre de otra base de datos, usuario y contraseña), el volumen que mapearemos fuera del contenedor , en un directorio diferente  al de desarrollo.
Con odooB levantaremos una instancia de Odoo 16 que se conectará a la base de datos del servicio postgres_B.  A la hora de crearlo, tenemos que definir los datos para la imagen, el nombre del contenedor, las variables de entorno (nombre de la base de datos, usuario y contraseña), los puertos donde podremos visualizar la interfaz (8070 en el caso de que se utilice la máquina física), los volúmenes donde se cargan los módulos adicionales, el volumen donde se guardarán los archivos que generé Odoo, las dependencias .

### el archivo compose.yaml

```yaml
services:
  postgres_A:
    image: postgres:14
    container_name: dbDesarrollo
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=paso
    volumes:
      - ~/OdooDev/dataDev:/var/lib/postgresql/data

  postgres_B:
    image: postgres:14
    container_name: dbProduccion
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=paso
    volumes:
      - ~/OdooDev/dataProd:/var/lib/postgresql/data

  odoo_A:
    image: odoo:16
    container_name: odooDesarrollo
    environment:
      - HOST=postgres_A
      - USER=odoo
      - PASSWORD=paso
    ports:
      - '8069:8069'
    volumes:
      - ~/OdooDev/volumesOdoo/addons:/mnt/extra-addons
      - ~/OdooDev/volumesOdoo/sessions:/var/lib/odoo/sessions
      - ~/OdooDev/volumesOdoo/filestore:/var/lib/odoo/filestore
    depends_on:
      - postgres_A
    command: --dev=all

  odooB:
    image: odoo:16
    container_name: odooProduccion
    environment:
      - HOST=postgres_B
      - USER=odoo
      - PASSWORD=paso
    ports:
      - '8070:8069'
    volumes:
      - ~/OdooDev/volumesOdoo/addons:/mnt/extra-addons
    depends_on:
      - postgres_B
```