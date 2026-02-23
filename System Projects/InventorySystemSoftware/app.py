from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
FILE = "inventory.txt"

# Helper functions
def read_items():
    items = []
    if not os.path.exists(FILE):
        return items
    with open(FILE, "r") as f:
        for line in f:
            name, qty, price = line.strip().split(",")
            qty = int(qty)
            price = float(price)
            items.append({"name": name, "qty": qty, "price": price, "amount": qty*price})
    return items

def add_or_update_item(name, qty, price):
    items = read_items()
    updated = False
    for item in items:
        if item["name"].lower() == name.lower():
            item["qty"] = qty
            item["price"] = price
            updated = True
            break
    if not updated:
        items.append({"name": name, "qty": qty, "price": price})
    with open(FILE, "w") as f:
        for item in items:
            f.write(f"{item['name']},{item['qty']},{item['price']}\n")

def delete_item(name):
    items = read_items()
    new_items = [item for item in items if item["name"].lower() != name.lower()]
    with open(FILE, "w") as f:
        for item in new_items:
            f.write(f"{item['name']},{item['qty']},{item['price']}\n")

# Routes
@app.route('/')
def index():
    items = read_items()
    return render_template('index.html', items=items)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    qty = int(request.form['qty'])
    price = float(request.form['price'])
    add_or_update_item(name, qty, price)
    return redirect(url_for('index'))

@app.route('/delete/<name>', methods=['POST'])
def delete(name):
    delete_item(name)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)