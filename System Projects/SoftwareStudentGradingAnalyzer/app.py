from flask import Flask, render_template, request

app = Flask(__name__)


# ----------------------
# Logic functions
# ----------------------

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def determine_letter_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else: return "F"


# ----------------------
# Routes
# ----------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    grades = [float(x) for x in request.form["grades"].split(",")]

    avg = calculate_average(grades)
    letter = determine_letter_grade(avg)

    # save to file
    with open("grades.txt", "a") as f:
        f.write(f"{name}: {grades} -> {avg:.2f} ({letter})\n")

    return render_template(
        "index.html",
        result={"average": avg, "letter": letter}
    )


# ----------------------
# Run server
# ----------------------

if __name__ == "__main__":
    app.run(debug=True)