# UF API
Esta es una API que permite obtener el valor de la Unidad de Fomento (UF) para una fecha en particular.

## Requerimientos
* Python 3.6 o superior
* Pip
## Instalación
1. Clona el repositorio: 

```git clone https://github.com/MartinAAcebeyL/ApiUnidadFomento.git```

2. Ingresa al directorio del proyecto: 

```cd ApiUnidadFomento```

3. Crea un entorno virtual: 

```python3 -m venv venv```

4. Activa el entorno virtual:

 ```source venv/bin/activate```

5. Instala las dependencias: 

```pip install -r requirements.txt```
## Uso
1. Inicia el servidor: 

```python manage.py```

2. Realiza una solicitud GET a http://127.0.0.1:5000//api/v1/uf/<<fecha>> donde fecha es un string en formato dd-mm-yyyy.
3. Recibirás un objeto JSON como  respuesta.
### Ejemplo
Si deseas obtener el valor de la UF para el 1 de enero de 2022, debes realizar una solicitud GET a http://127.0.0.1:5000//api/v1/uf/30-05-2022.

La respuesta será un objeto JSON con la siguiente estructura:

```
{
  "data": "32.664,89",
  "message": "UF value",
  "succses": true
}
```
## Pruebas
Para ejecutar las pruebas, asegúrate de estar dentro del entorno virtual y en la raíz del proyecto, y luego corre el siguiente comando:

```python -m unittest discover```
## Cobertura
Para obtener un reporte de cobertura de las pruebas, asegúrate de estar dentro del entorno virtual y en la raíz del proyecto, y luego corre los siguientes comandos:

```coverage run -m unittest discover```

```coverage report```
## Documentación
Para ver la documentación de la API, asegúrate de estar dentro del entorno virtual y en la raíz del proyecto, y luego ejecuta la aplicación y visita la siguiente URL en tu navegador:

http://localhost:5000/apidocs/
