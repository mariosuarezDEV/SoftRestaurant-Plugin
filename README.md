
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

