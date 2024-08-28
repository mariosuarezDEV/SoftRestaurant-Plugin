
# Extensión de cambio de cheques para SoftRestaurant

Stack tecnológico:

### Backend
- **Python**
    - Django
    - Django RESt Framework
- **SQL server**
- **Anaconda Python**
- **SQLite**

# Entorno virtual

En este proyecto se esta utilizando la versión de **python 3.11** y se uso conda para la creación del entorno virtual, el comando para la creción del entorno es: 
```
conda create -n env_name python=3.11
```

# Ejecución del proyecto
Pasos para poder ejecutar el proyecto y trabajarlo en desarrollo:

1. **Clonar el respositorio**

```
git clone https://github.com/mariosuarezDEV/SoftRestaurant-Plugin
```

2. **Instalar las biblitecas necesarias que vienen en el archivo requirements.txt**

- **Usando el entorno virtual con Anaconda**
```
conda install --yes --file requirements.txt
```

- **Usando el entorno virtual virtualenv**
```
pip install -r requirements.txt
```

3. **Ejecutar el servicio del proyecto**

```
python manage.py runserver
```

- Si deseas ejecutar el servicio para que todos los clientes puedan acceder al sitio ejecuta el comando runserver con los paramentros: **0.0.0.0:80**
El puerto puede ser diferente siempre y cuando este disponible.

```
python manage.py runserver 0.0.0.0:80
```

# Iniciando el proyecto Alfa 0.3
### Paso 1: Migrar la base de datos

```
python manage.py migrate
```

- Debes tener en cuenta que antes debes tener una conexión a tu base de datos, esta conexión se hace en el archivo **settings.py** situado en el directorio **Backend**

```
DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'nombre de la base de datos',
            'USER': 'nombre de usuario',
            'PASSWORD': 'contraseña',
            'HOST': 'DESKTOP-TEST\\Instacia',
            'PORT': '1433',
            'OPTIONS': {
                        'driver': 'ODBC Driver 17 for SQL Server',
                    },
        },
    }
```

### Paso 2: Crear un usuario administrador
```
python manage.py createsuperuser
```

- Ingresar el nombre de usuario (este nombre de usuaio será solicitado para iniciar sesión posteriormente).
- Ingresa un correo electronico (opcional)
- Ingresas contraseña para el usuario (Esta contraseña es la clave para iniciar sesión en el sistema y en el /admin)

### Paso 3: Iniciar el servicio
```
python manage.py runserver 0.0.0.0:80
```

- Ahora entramos al sistema con  la direccion ip de la maquina que corre el servcio: **192.168.1.2/cheques**

- Iniciar sesión con la cuenta de super usuario

### Paso 4: Configuración automatica
Si existe un error con código **42S22** puedes ir a la ruta **192.168.1.2/cheques/configurar** lo que hara esta página es corregir los diseño de la base de datos y sean aptas para funcionar con el sistema.

En caso de no existir cierto error y fuiste redirijido automaticamente a **192.168.1.2/cheques/configurar** solo regresa a **192.168.1.2/cheques** y podras empezar a utilizar el sistema.