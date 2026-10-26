# Kampala Care Pharmacy

Flask build of the Overview and Inventory screens.

## Run

    pip install -r requirements.txt
    python app.py

Then open http://127.0.0.1:5000

## Structure

- app.py: routes (Overview, Inventory with tabs/search/filters, CSV export)
- data.py: demo data. Replace with database queries.
- templates/: base layout, overview, inventory, icon macros
- static/style.css: all styling

## Not built yet

Receive stock, New sale, stock adjustment, pagination, and the Sales, Purchases,
Suppliers, Reports and Settings screens are placeholders.
