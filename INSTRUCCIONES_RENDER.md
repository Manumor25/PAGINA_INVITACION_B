# 🚀 INSTRUCCIONES PARA RENDER

## PASO 1: Preparar localmente

```bash
# Activar entorno virtual
python -m venv venv
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Hacer migraciones
python manage.py migrate
```

## PASO 2: Subir a GitHub

```bash
git add .
git commit -m "Configuración para Render"
git push origin main
```

## PASO 3: Configurar en Render.com

### 3.1 Crear Web Service
1. Ve a render.com
2. Clic en "New +" → "Web Service"
3. Conecta tu repo de GitHub
4. Llena los campos:

**Name:** tu-app-name (ejemplo: mi-boda-invitation)

**Branch:** main

**Build Command:**
```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

**Start Command:**
```
gunicorn card_games.wsgi:application
```

**Instance Type:** Free

### 3.2 Agregar Variables de Entorno

Ve a la tab "Environment" y agrega estas variables:

| Key | Value |
|-----|-------|
| DEBUG | False |
| SECRET_KEY | tu-clave-secreta-larga-aleatoria |
| RENDER_EXTERNAL_HOSTNAME | tu-app-name.onrender.com |

**Para SECRET_KEY**, usa una clave larga. Ejemplo:
```
django-insecure-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0
```

### 3.3 Crear Base de Datos PostgreSQL

1. En Render, ve a "Databases"
2. Clic en "New PostgreSQL"
3. Llena:
   - **Name:** card-games-db
   - **Database:** card_games_db
4. Copia el `Internal Database URL` (comienza con postgresql://)

### 3.4 Conectar Base de Datos

En tu Web Service (tab Environment), agrega:

| Key | Value |
|-----|-------|
| DATABASE_URL | [Pega la URL de PostgreSQL] |

### 3.5 Deploy

Haz clic en "Create Web Service"

Espera ~5-10 minutos a que se compile y desplegue.

Verás "Service is live" cuando esté listo.

## PASO 4: Crear Admin

1. En Render, ve a tu servicio
2. Abre la terminal (Shell) en la esquina superior derecha
3. Ejecuta:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear el admin.

## ✅ Verificar que todo funciona

Visita estos URLs:
- https://tu-app-name.onrender.com/
- https://tu-app-name.onrender.com/invitacion/
- https://tu-app-name.onrender.com/admin/

## 🆘 Si algo falla

Ve a "Logs" en Render para ver que salió mal.

Errores comunes:
- **ModuleNotFoundError**: Falta dependencia en requirements.txt
- **Database connection refused**: DATABASE_URL incorrea. Cópiala nuevamente
- **Static files missing**: Abre Shell y ejecuta: `python manage.py collectstatic --noinput`

---

Listo! Tu página estará online en pocos minutos 🎉
