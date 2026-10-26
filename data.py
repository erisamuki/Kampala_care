"""Demo data for the Kampala Care pharmacy screens.

Replace these structures with real database queries later.
DEMO_TODAY is fixed so the "days left" figures match the design.
"""
from datetime import date

DEMO_TODAY = date(2026, 10, 26)

BRANCH = {"name": "Ntinda branch", "location": "Kampala, Uganda"}

# Counts shown in the inventory header and tabs
INVENTORY_STATS = {
    "medicines": 148,
    "batches": 192,
    "below_reorder": 7,
    "expiring_90": 4,
}
TAB_TOTALS = {"available": 192, "quarantined": 2, "expired": 1}


def _b(medicine, sub, category, batch, expiry, qty, unit, pack, status, price,
       price_unit, conversion, reorder, grn, grn_date, received, move,
       supplier="Sample medical wholesaler", note=None):
    return {
        "medicine": medicine, "sub": sub, "category": category, "batch": batch,
        "expiry": expiry, "qty": qty, "unit": unit, "pack": pack,
        "status": status, "price": price, "price_unit": price_unit,
        "conversion": conversion, "reorder": reorder, "grn": grn,
        "grn_date": grn_date, "received": received, "move": move,
        "supplier": supplier, "note": note,
    }


AVAILABLE = [
    _b("Amoxicillin 250 mg", "Capsule · Antibiotic", "Antibiotic", "AMX-2408",
       date(2026, 12, 31), 80, "capsules", "8 strips × 10", "low", 200,
       "capsule", "1 strip = 10 capsules", "200 capsules", "GRN-0091",
       "12 Aug 2026", "1,000 capsules",
       ("-20 capsules", "Sale SAL-0038", "26 Oct 2026, 09:46 EAT", "100 → 80")),
    _b("Artemether / lumefantrine", "20 mg / 120 mg · Tablet", "Antimalarial",
       "AL-2602", date(2027, 1, 15), 36, "packs", "24 tablets / pack",
       "in_stock", 6000, "pack", "1 pack = 24 tablets", "20 packs", "GRN-0094",
       "02 Sep 2026", "60 packs",
       ("-4 packs", "Sale SAL-0036", "26 Oct 2026, 09:12 EAT", "40 → 36")),
    _b("Omeprazole 20 mg", "Capsule · Gastrointestinal", "Gastrointestinal",
       "OMP-2511", date(2027, 1, 20), 280, "capsules", "28 strips × 10",
       "in_stock", 500, "capsule", "1 strip = 10 capsules", "100 capsules",
       "GRN-0095", "05 Sep 2026", "400 capsules",
       ("-10 capsules", "Sale SAL-0031", "25 Oct 2026, 16:20 EAT", "290 → 280")),
    _b("Cetirizine 10 mg", "Tablet · Antihistamine", "Antihistamine", "CTZ-2604",
       date(2027, 1, 22), 120, "tablets", "12 strips × 10", "low", 200,
       "tablet", "1 strip = 10 tablets", "200 tablets", "GRN-0089",
       "30 Jul 2026", "500 tablets",
       ("-10 tablets", "Sale SAL-0030", "25 Oct 2026, 15:05 EAT", "130 → 120")),
    _b("Metformin 500 mg", "Tablet · Antidiabetic", "Antidiabetic", "MET-2601",
       date(2028, 1, 31), 600, "tablets", "6 boxes × 100", "in_stock", 200,
       "tablet", "1 box = 100 tablets", "300 tablets", "GRN-0083",
       "14 Jul 2026", "1,000 tablets",
       ("-30 tablets", "Sale SAL-0027", "25 Oct 2026, 11:40 EAT", "630 → 600")),
    _b("Salbutamol 100 mcg", "Inhaler · 200 doses", "Respiratory", "SAL-2603",
       date(2028, 3, 31), 8, "inhalers", "1 inhaler / unit", "low", 15000,
       "inhaler", "1 inhaler = 200 doses", "20 inhalers", "GRN-0087",
       "22 Jul 2026", "30 inhalers",
       ("-1 inhaler", "Sale SAL-0025", "24 Oct 2026, 17:02 EAT", "9 → 8")),
    _b("Paracetamol 500 mg", "Tablet · Analgesic", "Analgesic", "PCM-2610",
       date(2028, 9, 30), 2400, "tablets", "24 boxes × 100", "in_stock", 100,
       "tablet", "1 box = 100 tablets", "1,000 tablets", "GRN-0108",
       "26 Oct 2026", "1,000 tablets",
       ("+1,000 tablets", "Receipt GRN-0108", "26 Oct 2026, 10:42 EAT",
        "1,400 → 2,400")),
    _b("ORS low-osmolarity", "Powder · 1 L sachet", "Rehydration", "ORS-2609",
       date(2028, 9, 30), 240, "sachets", "12 boxes × 20", "in_stock", 1000,
       "sachet", "1 box = 20 sachets", "100 sachets", "GRN-0092",
       "20 Aug 2026", "300 sachets",
       ("-5 sachets", "Sale SAL-0033", "25 Oct 2026, 13:18 EAT", "245 → 240")),
]

QUARANTINED = [
    _b("ORS low-osmolarity", "Powder · 1 L sachet", "Rehydration", "ORS-2606",
       date(2028, 6, 30), 12, "sachets", "1 box × 12", "quarantined", 1000,
       "sachet", "1 box = 20 sachets", "100 sachets", "GRN-0088", "25 Jul 2026",
       "60 sachets",
       ("-12 sachets", "Moved to quarantine", "26 Oct 2026, 09:58 EAT", "12 → 0"),
       note="Damaged packaging"),
    _b("Ibuprofen 400 mg", "Tablet · Analgesic", "Analgesic", "IBU-2511",
       date(2028, 2, 28), 200, "tablets", "2 boxes × 100", "quarantined", 150,
       "tablet", "1 box = 100 tablets", "300 tablets", "GRN-0090", "10 Aug 2026",
       "500 tablets",
       ("-200 tablets", "Moved to quarantine", "22 Oct 2026, 14:30 EAT",
        "200 → 0"),
       note="Storage temperature check pending"),
]

EXPIRED = [
    _b("Amoxicillin 125 mg / 5 mL", "Suspension · Antibiotic", "Antibiotic",
       "AMS-2501", date(2026, 9, 30), 6, "bottles", "1 box × 6", "expired",
       4500, "bottle", "1 bottle = 100 mL", "10 bottles", "GRN-0061",
       "15 Jan 2026", "24 bottles",
       ("-6 bottles", "Moved to expired stock", "01 Oct 2026, 08:15 EAT",
        "6 → 0"),
       note="Past expiry date; cannot be sold"),
]

TABS = {"available": AVAILABLE, "quarantined": QUARANTINED, "expired": EXPIRED}

CATEGORIES = sorted({b["category"] for b in AVAILABLE + QUARANTINED + EXPIRED})

# ---------------------------------------------------------------- overview
OVERVIEW = {
    "sales_today": 864000,
    "sales_count": 42,
    "sales_yesterday": 725000,
    "stock_value": 18420000,
    "below_reorder": 7,
    "out_of_stock": 3,
    "running_low": 4,
    "expiring_batches": 4,
    "week": [
        ("Tue", 20, 600000), ("Wed", 21, 760000), ("Thu", 22, 690000),
        ("Fri", 23, 900000), ("Sat", 24, 1120000), ("Sun", 25, 694000),
        ("Mon", 26, 864000),
    ],
    "week_range": "20–26 Oct 2026",
    "payments": [("Cash", 412000), ("MTN MoMo", 326000), ("Airtel Money", 126000)],
    "activity": [
        ("package", "Stock received · Paracetamol 500 mg",
         "1,000 tablets · batch PCM-2610 · receipt GRN-0108", "10:42"),
        ("bag", "Sale recorded · UGX 24,000", "Receipt SAL-0042 · Cash", "10:36"),
        ("archive", "Batch moved to quarantine",
         "ORS-2606 · 12 sachets · damaged packaging", "09:58"),
        ("check", "Stock count completed · Cetirizine 10 mg",
         "120 tablets confirmed · no adjustment", "09:20"),
    ],
}
