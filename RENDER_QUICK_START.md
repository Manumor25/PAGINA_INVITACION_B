# CÓDIGO PARA RENDER - COPIAR Y PEGAR

## 🔧 Build Command (Copiar completo en Render)

```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

## ▶️ Start Command (Copiar completo en Render)

```
gunicorn card_games.wsgi:application
```

---

## 📋 Variables de Entorno a Completar

En Render → Tu Servicio → Environment → Add Environment Variable

### Variable 1
```
Key: DEBUG
Value: False
```

### Variable 2
```
Key: SECRET_KEY
Value: django-insecure-a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6a7b8c9d0e1f2
```

### Variable 3
```
Key: RENDER_EXTERNAL_HOSTNAME
Value: tu-app-nombre.onrender.com
```
(Reemplaza "tu-app-nombre" por el nombre que le diste al servicio)

### Variable 4 (Importante - De la Base de Datos)
```
Key: DATABASE_URL
Value: postgresql://usuario:contraseña@host:5432/database_name
```
(Se genera automáticamente cuando creas la Base de Datos en Render)

---

## 📊 Configuración del Servicio Web

| Campo | Valor |
|-------|-------|
| **Name** | mi-boda-invitation (o tu nombre) |
| **Region** | Virginia (USA) |
| **Branch** | main |
| **Build Command** | pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate |
| **Start Command** | gunicorn card_games.wsgi:application |
| **Instance Type** | Free |

---

## 🗄️ Configuración de Base de Datos

1. **Ve a Databases en Render**
2. **Click en "New PostgreSQL"**
3. **Llena:**
   - **Name:** card-games-db
   - **Database:** card_games_db
   - **Region:** Virginia (USA) - (misma que tu servicio)

4. **COPIA el "Internal Database URL" y pégalo en la variable DATABASE_URL**

---

## 🎉 Comandos en Shell de Render (después de deploy)

Una vez que tu servicio esté "live", abre la terminal web (Shell):

```bash
python manage.py createsuperuser
```

Luego ingresa:
- Username: admin
- Email: tu@email.com
- Password: tu-contraseña-segura

---

## ✅ URLs Finales

Tu site estará en:
- **Home:** https://tu-app-nombre.onrender.com/
- **Invitación:** https://tu-app-nombre.onrender.com/invitacion/
- **Admin:** https://tu-app-nombre.onrender.com/admin/

---

**¡Eso es todo! Tu aplicación estará lista en ~10 minutos** 🚀
