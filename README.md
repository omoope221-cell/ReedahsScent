# Reedah's Scent — Django E-commerce Backend

A mini Django e-commerce site for a perfume store. No payment gateway —
customers add items to a cart, fill in their delivery details, and get
redirected straight to WhatsApp with a pre-filled message (order summary +
your bank account details) ready to send.

## Admin Dashboard

A custom, hidden admin dashboard lives at:

- `/admin-login/` — staff-only login (not linked anywhere in the public site)
- `/admin-dashboard/` — overview: total/pending orders, product count, confirmed revenue, low-stock alerts, recent orders
- `/admin-dashboard/products/` — add, edit, delete products
- `/admin-dashboard/categories/` — add/delete categories
- `/admin-dashboard/orders/` — filter by status, view full order details, update status, message the customer on WhatsApp directly from the order page

Only accounts with `is_staff=True` can log in here — create one with `python manage.py createsuperuser`. This is separate from Django's built-in `/admin/`, which still works too if you ever need it, but the dashboard above is the one designed for day-to-day use.

## Apps

- **store** — Categories & Products, product listing/detail pages
- **cart** — session-based shopping bag (no login required to add items)
- **orders** — checkout form, order + order items, builds the WhatsApp message
- **accounts** — simple signup/login/logout (Django's built-in auth)

## How ordering works

1. Customer browses `/shop/`, adds products to their bag.
2. At `/orders/create/` they fill in name, email, phone, and delivery address.
3. On submit, an `Order` + `OrderItem`s are saved, the cart is cleared, and the customer is redirected to WhatsApp with the order summary and your bank details.
4. You confirm the order and payment directly with the customer over WhatsApp, then update the order's status from the Django admin.

## Setup (Windows / VS Code)

1. Open this folder in VS Code, then open a terminal inside this folder (the one containing `manage.py`).

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create your `.env` file:

```bash
copy .env.example .env
```

5. Run migrations:

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Start the server:

```bash
python manage.py runserver
```
