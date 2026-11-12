# SanjuanEnriquezBrandonAlexisUnidad3

---

## FinanTrack — Sistema de Control de Gastos y Servicios Web

Proyecto desarrollado para la materia **Desarrollo Web Integral**, correspondiente a la Unidad 3.

FinanTrack es una aplicación web de administración financiera personal desarrollada con Django que permite registrar ingresos y gastos, clasificarlos por categorías y calcular automáticamente el saldo disponible. En esta tercera unidad, el sistema se ha ampliado incorporando robustos mecanismos de seguridad web, la integración de un Web Service de terceros (Frankfurter API) para consultar tipos de cambio en tiempo real, y el desarrollo de un Web Service propio (API REST en formato JSON) protegido por autenticación y restricciones de privacidad por usuario.

---

## Tecnologías utilizadas

- Python 3.14.6
- Django 6.1.1
- SQLite (Base de datos del proyecto)
- Requests (Biblioteca para consumo de APIs externas)
- HTML5 y CSS3 (Interfaz adaptable a dispositivos móviles)
- Git y GitHub (Control de versiones)
- Visual Studio Code y Git Bash

---

## Funcionalidades del Sistema

### Gestión Financiera General
- Inicio y cierre de sesión de usuarios mediante el sistema de autenticación de Django.
- Panel principal (Dashboard) que muestra tarjetas dinámicas con el total de ingresos, gastos, saldo disponible y el tipo de cambio USD/MXN actualizado.
- Registro de movimientos financieros especificando concepto, monto, tipo (ingreso o gasto), categoría, fecha y descripción opcional.
- Visualización en tablas detalladas y eliminación de movimientos.

### Mecanismos de Seguridad
- Autenticación obligatoria: Restricción de acceso a vistas protegidas y endpoints mediante el decorador @login_required.
- Privacidad de datos por usuario: Aislamiento estricto de la información; cada usuario consulta y gestiona exclusivamente sus propios registros financieros utilizando filtros basados en el usuario autenticado actual (request.user).
- Protección CSRF: Inclusión de la etiqueta de seguridad {% csrf_token %} en todos los formularios con peticiones POST.
- Eliminación segura y bloqueo HTTP 405: La eliminación de registros se efectúa mediante formularios POST acompañados de una confirmación en JavaScript, bloqueando de forma estricta las solicitudes mediante métodos GET (@require_POST), devolviendo un código de error 405 Method Not Allowed.

### Web Service de Terceros (Frankfurter API)
- Integración con la API pública Frankfurter (https://api.frankfurter.dev/v1/latest?base=USD&symbols=MXN) a través de la biblioteca requests.
- Consulta automatizada del tipo de cambio actual entre el dólar estadounidense y el peso mexicano, integrada directamente en el dashboard con manejo controlado de excepciones y tiempos de espera (timeout).

### Web Service Propio (API REST en formato JSON)
- Creación de un endpoint dedicado en la ruta /api/movimientos/ que serializa la información financiera de la base de datos y la devuelve en formato universal JSON mediante JsonResponse.
- Validación de sesión activa para impedir el acceso anónimo y garantizar la confidencialidad de los datos.

---

## Control de versiones y flujo de trabajo

El proyecto utiliza Git para el control de cambios locales y GitHub como repositorio remoto. El flujo de desarrollo consistió en:
1. Realizar y verificar las modificaciones de código en el entorno local.
2. Comprobar el estado de los archivos modificados mediante git status.
3. Preparar los cambios con git add.
4. Registrar los avances mediante commits descriptivos y limpios con git commit.
5. Sincronizar el repositorio remoto mediante git push origin main.

---

## Instalación, Ejecución Local y Enlace del Repositorio

Para ejecutar y probar el proyecto en tu equipo utilizando Git Bash, sigue los siguientes pasos:

1. Clonar el repositorio oficial:
git clone https://github.com/BrandonSanjuan/SanjuanEnriquezBrandonAlexisUnidad3.git
cd SanjuanEnriquezBrandonAlexisUnidad3
(También puedes consultar el repositorio directamente en línea en el siguiente enlace: https://github.com/BrandonSanjuan/SanjuanEnriquezBrandonAlexisUnidad3)

2. Crear y activar el entorno virtual:
python -m venv .venv
source .venv/Scripts/activate

3. Instalar las dependencias del proyecto:
pip install -r requirements.txt

4. Aplicar las migraciones a la base de datos SQLite:
python manage.py migrate

5. Crear un usuario administrador:
Para poder iniciar sesión y probar los mecanismos de seguridad y la API propia, crea una cuenta de superusuario desde la terminal:
python manage.py createsuperuser
(Sigue las instrucciones en pantalla para ingresar tu nombre de usuario, correo opcional y contraseña).

6. Iniciar el servidor de desarrollo:
python manage.py runserver

7. Rutas de acceso en el navegador:
- Panel principal (Dashboard): http://127.0.0.1:8000/
- Endpoint del Web Service propio (JSON): http://127.0.0.1:8000/api/movimientos/ (requiere haber iniciado sesión previamente).

---

## Autor

**Brandon Alexis Sanjuan Enríquez**  
Proyecto académico — Materia: Desarrollo Web Integral, Unidad 3.