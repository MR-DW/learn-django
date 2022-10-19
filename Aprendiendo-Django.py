# Crear carpeta donde se trabajara el backend
# En cmd:
# 
# 1 -INSTALAR ENTORNO VIRTUAL
# python -m venv env
# 
# 2-INICIAR ENTRONO VIRTUAL
# .\env\Scripts\activate
## para desactivar el entorno virtual
# deactivate 
# 
# 3- VER MODULOS INSTALADOS
# pip list
# 
# 4- Instalar Django
# pip install Django
# 
# 5- VERIFICAR SI SE INSTALO DJANGO CON PIP LIST
# para desinstalar es pip uninstall nombre_programa 

# 6- Crear Proyecto. Por norma general se llama backend.
# django-admin startproject nombre_proyecto
# 
# 7- Una vez creado en settings.py se puede ver un DEBUG = True eso significa que esta en 
# estado de construccion. Y la secret key.
# Templates
# Base de datos, no trabajar con el sqlite3
# Passwords
# Lenguaje, zona horaria
# Rutas de archivos(js, html, css)
# 
# 8-En el archivo urls.py nos muestra como crear importaciones de vistas
# 
# 9-wsgi.py es para levantar el proyecto
# 
# 10- manage nos permite administrar el proyecto, a traves de comandos para comenzarlo, pararlo, migraciones
# 
# 11- Si los archivos nos salen con lineas con corrector amarillo, es porque vsc no encontró los
# paquetes instalados. Se debe cambiar la ruta del interprete, ir al margen inferior derecho, 
# apretar donde dice 3.10.8 64-bit(microsoft store), en la ventana superior que aparece seleccionar
# Escriba la ruta de acceso del interprete -> Buscar... -> En la carpeta donde se creó la app -> ir al env 
# -> scripts -> python ->seleccionar -> y debe quedar en el margen inferior derecho 3.10.8 ('env':venv)
# 
# 12 - Levantar el proyecto: para ello debo estar parado en la consola en la carpeta que se encuentre el manage.py
# python manage.py runserver
# Nos devuelve un server de desarrollo con una ip (link), el cual debe abrirse en un navegador.
# Para frenar el server utilizo ctrl+c
# Crea un archivo nuevo, que es una base de datos db.sqlite3 se puede cambiar la base de datos desde settings.py
# 
# Las migaciones es traducir codigo a sentencias de sql y los inpacta en la base de datos
# Para ejecutar las migraciones de base de datos se ejecuta el comando:
# python manage.py migrate
# 
# 13 - Admin de DJANGO para poder gestionar la base de datos.
# se ejecuta el server y al server devuelto lo copio y lo pego en un navegador donde le coloco /admin
# Así voy a poder ingresar. Los datos del perfil no se comparte con nadie.
# 
# 14- CREACIÓN USUARIO ADMIN DJANGO:
# se realiza tirando el siguiente comando:
# python manage.py createsuperuser
# poner nombre usuario/mail/contra
# 
# 15 - Panel de Administración:
# Se debe volver a correr el servidor, ingresar con el server que me brinda colocarle /admin e ingresar con usuario 
# y contra creada. Luego me permite entrar y administrar el panel de usuarios.
# 

# 17 - CONFIGURACIONES SETTINGS 
# 
# 18- Instalar DJANGO REST FRAMEWORK:
# comando: pip install djangorestframework
# verificar con pip list su instalación. 
# Luego en la sección de settings en installed apps, se van a dividir los modulos instalados en BASE_APPS (modulos internos bases de django), LOCAL_APPS (modulos/apps locales) 
# y THIRD_APPS(modulos de 3ros) aquí se copia/registra el 'rest_framework', para que se instale rest en nuestra aplicación
# para luego concatenarlos bajo la variable INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS
#Levantar el server para controlar que se haya realizado el proceso de manera correcta. 
# 
# 19 - BASES DE DATOS:
# Vamos a cambiar la base de datos porque sqlite3 es muy basico para la ejecución de un proyecto.
# En settigns vamos a ir al objeto DATABASES.
# 
# DATABASES = {
#     'default': { ''' Indica que se utiliza por defecto '''
#         'ENGINE': 'django.db.backends.sqlite3', '''Indica que motor se utiliza'''
#         'NAME': BASE_DIR / 'db.sqlite3', '''nombre de la base que utiliza'''
#     }
# }
#  
# Para ello accederemos al link que se encuentra por encima del objeto DATABASES.
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases 
# y lo vamos a cambiar por otra base de datos de mysql:
# DATABASES = {
#     'default': {  ''' Indica que se utiliza por defecto '''
#         'ENGINE': django.db.backends.mysql', '''Indica que motor se utiliza'''
#         'NAME': 'mydatabase', '''nombre de la base que utiliza'''
#         'USER': 'mydatabaseuser', '''buscar en el motor de base de datos'''
#         'PASSWORD': 'mypassword', '''Igual que user'''
#         'HOST': '127.0.0.1', '''Igual que user'''
#         'PORT': '3306', '''Se ve en la consola de xampp mysql port'''
#     }
# }
#  
# Buscar mas abajo el motor de base de datos a utilizar en esta ocación se usara mysql
# Luego editar los demas campos
# 
# vamos a levantar Xampp:
# creamos una nueva base de datos, la dejamos en blanco solo le colocamos el nombre relacionado a la app.
# Luego busco busco el user, host y port en phpMyAdmin -> Cuentas de usuarios ->muestra tabla con los datos.
# 
# Instalar el driver para realizar la conexión/traducción entre django y mysql: (para evitar errores)
# comando: pip install mysqlclient
# Posterior debo realizar las migraciones para que se creen automaicamente las tablas en la base de datos
# Comando: python manage.py migrate
# Y refrescar el phpMyAdmin y verificar si la base de datos contiene las nuevas tablas.
# 
# 20 - iNDEPENDIZACIÓN DE APARTADOS CON APPS
# python manage.py startapp nombreDescriptivo
# Se crea una nueva carpeta con sus archivos y secciones. La carpeta se va a llamar como el nombre descriptivo del comando tirado en consola
#Podemos manejar todas las funciones de la app. y aquí estan los modelos (patrones de diseño de la app). Modelo Vista Template/Controlador.
# Este se basa al modelo de base de datos (tablas)
# El controlador va a ser la parte de las funciones.
# Models para crear los modelos de base de datos(tablas sql)
# Controlador /Views es donde se construye toda la logica, tanto front se capturan los post los get y peticiones a la base de datos.
# Views es el front pero al trabajar con rest no se hace. La deolución se hace a traves de formato JSON(archivos que guardan info en el backend para enviarlo al front).
# 
# Ir a la carpeta de la apliación :
# Models.py -> los modelos son tablas de la base de datos. En su sección se pueden crear nuevas tablas/modelos.
# se crea una class que va a heredad de models, luego se coloca un .Model que significa que va a sobreescribir en modelo, que ya tiene su propio constuctor.
# a la clase se le dan:
# -Opciones: se van a contruir objetos que contengan valores que pueden ser obtenidos por inputs tipo radio, checkbox, desplegables. Y de esta manera simplificar la ontrucción de atributos.
# luego se va a conectar con el atributo correspondiente como valor de una de sus cualidades.
# -Atributos, a estos se es asigna un models. para darle un tipo de campo x ej. models.charfield. 
# a cada atibuto luego de darle el tipo, se le asignan cualidades: longitud, que sea unico,
# 
# # Create your models here.
# class Hero(models.Model):
    
#     #Opciones
#     UNIVERSE_CHOICES = (
#         ('1', 'Marvel'),
#         ('2', 'DC')
#     )
    
#     # Atributos
#     name = models.CharField(
#         max_length = 100,
#         unique = True,
#         verbose_name = 'Nombre', """Como figura el nombre en la tabla"""
#     )

#     age = models.IntegerField(

#     )

#     universe = models.CharField(
#         max_length = 1,
#         choices = UNIVERSE_CHOICES,
#         verbose_name = ' Universo'
#     )
# 
#  Por último, se debe registrar la app en settigns en el objeto de LOCAL_APPS
#  con el nombre de la app (nombre de la carpeta, en este caso es 'heroe')

# 21 - Volver a realizar Migrate para que se carguen los nuevos modelos. 
# Comando: python manage.py makemigrations
# En la carpeta de la app (heroe), en migrations se puede observar el nuevo archivo
# creado con el nombre 0001_initial.py que muestra la nueva tabla a crear, 
# los campos que contiene, sus tipos de datos, atributos y opciones.
# 
# Se debe volver a ejecutar una migración
# Comando: python manage.py migrate
# Refrescar el phpMyAdmin y allí debe figurar la nueva tabla dentro de nuestra base de datos.
# 

# 22- Entrar al Django Admin
# 
# 
# 23 - Debo registrar mi modelo para utilizarlo en el Django Admin.
# Voy a la carpeta de la aplicación (heroe), al archivo admin.py y en él voy a registrar mi modelo
# # Imports de models
# from heroe.models import Hero
    # """Ruta"""        """Modelo"""
    
# Register your models here.
# admin.site.register(Hero)
# 
# Refrescar admin y allí debe aparecer la nuva tabla/modelo.

#24 - Creación de servicios APIS. 
# Crear dentro de la carpeta principal de la app (en este caso heroesApp),
# una carpeta que se llame apps, para colocar en ella todas las aplicaciones nuevas que se creen.
# 
# En la carpeta hereo (carpeta de la unica app creada hasta el momento), crear una nueva carpeta donde
# se almacenaran todos los archivos relacionados al las apis (modulos, rutas, serialazers).
# 
# 25 - Crear Views:
# ir al archivo views.py de la app. 
# Importar rest, models, 
# Trabajar en vistas basadas en clases.
# se crea una class NombreServicioDescriptivo(DEDONDEVAHeredar)
# luego utilizar metodos para solicitar,pedir, modificar,etc.
# Los metodos van a recibir argumentos estos van a ser self, request y pueden ser id, etc.
# APIView intercepta metodos.
# Luego se crea la logica.
# 
# Podemos crear diferentes tipos de vistas para trabajar con n cantidad de metodos.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 







































































































