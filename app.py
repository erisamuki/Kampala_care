import csv
import io

from flask import Flask, Response, render_template, request

import data

app = Flask(__name__)


@app.template_filter("num")
def num(n):
    return f"{n:,}"


@app.template_filter("fdate")
def fdate(d):
    return f"{d.day:02d} {d:%b} {d.year}"


def days_left(d):
    return (d - data.DEMO_TODAY).days


app.jinja_env.globals.update(days_left=days_left, DEMO_TODAY=data.DEMO_TODAY)


def filtered_rows(tab, q, category, status):
    rows = list(data.TABS.get(tab, data.AVAILABLE))
    if q:
        needle = q.lower()
        rows = [r for r in rows if needle in r["medicine"].lower()
                or needle in r["batch"].lower() or needle in r["sub"].lower()]
    if category:
        rows = [r for r in rows if r["category"] == category]
    if status:
        rows = [r for r in rows if r["status"] == status]
    return sorted(rows, key=lambda r: r["expiry"])


@app.route("/")
def overview():
    o = data.OVERVIEW
    peak = 1200000  # chart axis maximum
    payments_total = sum(v for _, v in o["payments"])
    return render_template(
        "overview.html", page="overview", o=o, peak=peak,
        week_total=sum(v for _, _, v in o["week"]),
        payments_total=payments_total, branch=data.BRANCH,
        today=data.DEMO_TODAY,
    )


@app.route("/inventory")
def inventory():
    tab = request.args.get("tab", "available")
    if tab not in data.TABS:
        tab = "available"
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "")
    status = request.args.get("status", "")
    rows = filtered_rows(tab, q, category, status)

    selected = None
    wanted = request.args.get("batch")
    for r in rows:
        if r["batch"] == wanted:
            selected = r
    if selected is None and rows and wanted != "none":
        selected = rows[0]

    filtered = bool(q or category or status)
    total = len(rows) if filtered else data.TAB_TOTALS[tab]
    return render_template(
        "inventory.html", page="inventory", rows=rows, selected=selected,
        tab=tab, q=q, category=category, status=status, total=total,
        categories=data.CATEGORIES, stats=data.INVENTORY_STATS,
        tab_totals=data.TAB_TOTALS, branch=data.BRANCH,
    )


@app.route("/inventory/export.csv")
def export_csv():
    tab = request.args.get("tab", "available")
    rows = filtered_rows(tab, request.args.get("q", "").strip(),
                         request.args.get("category", ""),
                         request.args.get("status", ""))
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["Medicine", "Form", "Batch", "Expiry", "Available qty",
                "Unit", "Status", "Unit price (UGX)"])
    for r in rows:
        w.writerow([r["medicine"], r["sub"], r["batch"], r["expiry"].isoformat(),
                    r["qty"], r["unit"], r["status"], r["price"]])
    return Response(buf.getvalue(), mimetype="text/csv", headers={
        "Content-Disposition": f"attachment; filename=inventory-{tab}.csv"})


@app.route("/<section>")
def placeholder(section):
    """Sales, Purchases, Suppliers, Reports and Settings are not built yet."""
    if section not in {"sales", "purchases", "suppliers", "reports", "settings"}:
        return render_template("placeholder.html", page="", title="Not found",
                               branch=data.BRANCH), 404
    return render_template("placeholder.html", page=section,
                           title=section.title(), branch=data.BRANCH)


if __name__ == "__main__":
    app.run(debug=True)
