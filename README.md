# Alvargmez-Web

Sitio web personal y portafolio profesional de **Álvaro Gómez**, desarrollador de software backend (Python / Java) afincado en Cádiz. Construido con **Django** y desplegado de forma autohospedada en un servidor Linux propio.

**URL de producción:** [web.alvargmez.work](https://web.alvargmez.work)

---

## Descripción de la web

El sitio presenta mi perfil profesional y gestiona todo su contenido desde el **admin de Django**. Está organizado en las siguientes secciones:

### Inicio (`/`)
- Sección *hero* con foto de perfil y badges de tecnologías.
- **Sobre mí**: presentación y trayectoria (transición de técnico de sistemas/redes al desarrollo de software).
- **Habilidades**: programación, sistemas y redes, y electrónica/hardware.
- **Líneas de tiempo** de formación y experiencia profesional.
- Botón de **descarga del CV** en PDF (gestionado desde el admin).
- Enlaces a [GitHub](https://github.com/alvargmezS) y LinkedIn.

### Proyectos (`/proyectos/`)
Portafolio de proyectos en tarjetas, cada uno con nombre, descripción, tecnologías asociadas, icono y enlaces al código y a la demo cuando están disponibles. Tanto los proyectos como las tecnologías se administran desde el panel de Django.

### Contacto (`/contacto/`)
Formulario de contacto que envía, mediante SMTP:
- Una **notificación al propietario** del sitio con los datos del remitente (con `Reply-To` configurado para responder directamente).
- Un **acuse de recibo automático** a la persona que escribe.

### Blog (`/blog/`)
Sección en construcción (*próximamente*), donde documentaré el despliegue de esta web, mi servidor, la red doméstica y servicios autohospedados (Nextcloud, Docker Compose, NGINX...).

---

## Tecnologías utilizadas

| Componente | Tecnología |
|---|---|
| Framework backend | Django 6.x (Python) |
| Base de datos | PostgreSQL |
| Servidor WSGI | Gunicorn |
| Archivos estáticos | WhiteNoise (compresión + versionado) |
| Frontend | Bootstrap 5, Font Awesome, jQuery (servidos localmente), Google Fonts |
| Formularios | django-crispy-forms + crispy-bootstrap5 |
| Imágenes | Pillow |
| Configuración | python-dotenv (variables en `.env`) |

---

## Estructura del proyecto

```
alvargmez_web/   → Configuración del proyecto (settings, urls) y vista principal
blogApp/         → Blog (placeholder de próxima implantación)
contactoApp/     → Formulario de contacto con envío de correos
cvApp/           → Gestión del CV en PDF (subida desde el admin)
proyectosApp/    → Portafolio de proyectos y tecnologías
templates/       → Plantillas globales (base + una por sección)
static/          → Estáticos de origen (CSS, imágenes, vendor)
staticfiles/     → Estáticos compilados por collectstatic (WhiteNoise)
media/           → Archivos subidos (CV en PDF)
```

---

## Desarrollo en local

1. Clona el repositorio y crea un entorno virtual:

   ```bash
   git clone https://github.com/alvargmezS/Alvargmez-Web.git
   cd Alvargmez-Web
   python -m venv venv && source venv/bin/activate
   ```

2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Copia `.env.example` a `.env` y completa las variables (clave secreta, credenciales de PostgreSQL y datos SMTP).

4. Aplica las migraciones y crea un superusuario:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Lanza el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

   La web estará en `http://127.0.0.1:8000/` y el admin en `/admin/`.

> **Nota:** recuerda configurar `DEBUG=True` en `.env` para el desarrollo local.

---

## Despliegue en un servidor Linux (resumen)

Despliegue de producción autohospedado basado en el patrón clásico **NGINX + Gunicorn + Django + PostgreSQL**:

1. **Preparar el servidor**

   ```bash
   sudo apt update && sudo apt install python3 python3-venv python3-pip postgresql nginx
   ```

2. **Base de datos**: crea la base de datos y el usuario en PostgreSQL, y vuelca las credenciales en el `.env` del proyecto (`DB_NAME`, `DB_USER`, `DB_PASSWORD`).

3. **Aplicación**: clona el repo, crea el entorno virtual, instala los requirements (`pip install -r requirements.txt`), copia el `.env` con `DEBUG=False` y ejecuta:

   ```bash
   python manage.py migrate
   python manage.py collectstatic --no-input
   ```

4. **Servicio con Gunicorn + systemd**: crea una unidad `alvargmez-web.service` que lance Gunicorn contra `alvargmez_web.wsgi` (con `--workers` y socket/bind acordes), habilítala con `systemctl enable --now`. Los logs quedan disponibles en `journalctl -u alvargmez-web`.

5. **NGINX como proxy inverso**: configura un `server` que:
   - Haga `proxy_pass` al socket/puerto de Gunicorn.
   - Sirva `/static/` desde `staticfiles/` (aunque WhiteNoise ya los sirve comprimidos y versionados).
   - Sirva `/media/` desde el directorio `media/`.

6. **HTTPS**: instala un certificado con Certbot (`sudo certbot --nginx`) y añade el dominio a `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS` en los settings.

7. **Contenido**: accede a `https://tu-dominio/admin/`, crea un superusuario si no lo hiciste, y sube tus proyectos, tecnologías y CV desde el panel de administración.

---

## Autor

**Álvaro Gómez** — [GitHub](https://github.com/alvargmezS) · [LinkedIn](https://www.linkedin.com/) · [web.alvargmez.work](https://web.alvargmez.work)
