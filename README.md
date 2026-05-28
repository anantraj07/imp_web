# ISI Kolkata — Newcomers Welcome Site 🌟

A Django-powered welcome page for each incoming batch of ISI Kolkata students.
Built to replace repetitive WhatsApp announcements with a beautiful, permanent guide.

---

## ✨ Features

- **Dark Academic design** — midnight navy + saffron gold + floating math symbols
- **Interactive packing checklist** — tick off items, progress saved in session
- **Food & Mess guide** — timings, canteens, how-to
- **Hostel tips** — floor/wing rankings from seniors
- **Admission Day timeline** — step-by-step walkthrough
- **Aadhaar Seeding guide** — stipend setup instructions
- **Quick links** — all important URLs in one place
- **Admin panel** — update G-Form URL, batch year, WhatsApp link, and announcements without touching code

---

## 🚀 Setup (first time)

```bash
# 1. Install Django
pip install django

# 2. Apply migrations
python manage.py migrate

# 3. Create admin user
python manage.py createsuperuser

# 4. Run the server
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

---

## 🔧 Every New Batch — Just 3 Steps

1. Log into admin: **http://127.0.0.1:8000/admin/**
   - Username: `admin` | Password: `isikolkata2025` (change this!)

2. Go to **Welcome → Site Configuration → Edit**

3. Update:
   - `batch_year` → e.g. `2026`
   - `gform_url` → paste new G-Form link
   - `whatsapp_channel_url` → new channel invite
   - `announcement` → any urgent message (leave blank to hide banner)
   - `admission_date` → e.g. `15th July 2026`

That's it. The whole site updates automatically. ✅

---

## 📁 Project Structure

```
isi_welcome/
├── manage.py
├── db.sqlite3
├── isi_welcome/
│   ├── settings.py
│   └── urls.py
└── welcome/
    ├── models.py          ← SiteConfig model
    ├── views.py           ← Single index view
    ├── admin.py           ← Admin config
    └── templates/
        └── welcome/
            └── index.html ← The entire beautiful site
```

---

## 🌐 Deployment (optional, for public access)

To make this accessible over the internet:

```bash
pip install gunicorn
gunicorn isi_welcome.wsgi:application --bind 0.0.0.0:8000
```

Use a free tier on Railway, Render, or PythonAnywhere for hosting.
Set `DEBUG = False` and add your domain to `ALLOWED_HOSTS` in `settings.py`.

---

Made with ❤️ for ISI Kolkata juniors — Batch 2025 onwards.
