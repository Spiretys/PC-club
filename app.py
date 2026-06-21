from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

COMPUTERS = [
    {
        "id": 1,
        "name": "Cyber Storm",
        "status": "free",
        "cpu": "Intel Core i7-13700K",
        "gpu": "NVIDIA RTX 5070",
        "ram": "32 GB DDR5",
        "monitor": "27\" 240Hz",
    },
    {
        "id": 2,
        "name": "Neon Pulse",
        "status": "busy",
        "cpu": "AMD Ryzen 7 7800X3D",
        "gpu": "NVIDIA RTX 5080",
        "ram": "32 GB DDR5",
        "monitor": "27\" 240Hz",
    },
    {
        "id": 3,
        "name": "Phantom Edge",
        "status": "free",
        "cpu": "Intel Core i5-13600K",
        "gpu": "NVIDIA RTX 5060 Ti",
        "ram": "16 GB DDR5",
        "monitor": "24\" 165Hz",
    },
    {
        "id": 4,
        "name": "Vortex Pro",
        "status": "free",
        "cpu": "AMD Ryzen 5 7600X",
        "gpu": "NVIDIA RTX 5060",
        "ram": "16 GB DDR5",
        "monitor": "24\" 165Hz",
    },
    {
        "id": 5,
        "name": "Apex Legend",
        "status": "busy",
        "cpu": "Intel Core i9-13900K",
        "gpu": "NVIDIA RTX 5090",
        "ram": "64 GB DDR5",
        "monitor": "32\" 360Hz",
    },
]

TARIFFS = [
    {"name": "Час", "price": 150, "desc": "Стандартный тариф"},
    {"name": "3 часа", "price": 400, "desc": "Пакет на 3 часа"},
    {"name": "Ночь", "price": 800, "desc": "С 22:00 до 08:00"},
    {"name": "VIP", "price": 250, "desc": "ПК №5 — топовая зона"},
]

bookings = []


@app.route("/")
def index():
    return render_template("index.html", computers=COMPUTERS, tariffs=TARIFFS)


@app.route("/api/computers")
def api_computers():
    return jsonify(COMPUTERS)


@app.route("/api/book", methods=["POST"])
def api_book():
    data = request.get_json()
    name = (data.get("name") or "").strip()
    phone = (data.get("phone") or "").strip()
    pc_id = data.get("pc_id")
    hours = data.get("hours")

    if not name or not phone or not pc_id or not hours:
        return jsonify({"ok": False, "error": "Заполните все поля"}), 400

    try:
        pc_id = int(pc_id)
        hours = int(hours)
    except (TypeError, ValueError):
        return jsonify({"ok": False, "error": "Некорректные данные"}), 400

    if hours < 1 or hours > 12:
        return jsonify({"ok": False, "error": "Часы: от 1 до 12"}), 400

    pc = next((c for c in COMPUTERS if c["id"] == pc_id), None)
    if not pc:
        return jsonify({"ok": False, "error": "ПК не найден"}), 404

    if pc["status"] == "busy":
        return jsonify({"ok": False, "error": "Этот ПК сейчас занят"}), 409

    booking = {
        "name": name,
        "phone": phone,
        "pc_id": pc_id,
        "pc_name": pc["name"],
        "hours": hours,
    }
    bookings.append(booking)
    return jsonify({"ok": True, "booking": booking})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
