from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight, weight_unit, height, height_unit):
    """Calculate BMI based on weight and height with their respective units."""
    # Convert weight to kilograms
    if weight_unit == "g":
        weight = weight / 1000
    elif weight_unit == "tonnes":
        weight = weight * 1000
    elif weight_unit == "lbs":
        weight = weight * 0.453592

    # Convert height to meters
    if height_unit == "cm":
        height = height / 100
    elif height_unit == "inch":
        height = height * 0.0254
    elif height_unit == "ft":
        height = height * 0.3048

    # Validate inputs
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be greater than zero.")

    # Calculate BMI
    bmi = weight / (height ** 2)
    return bmi

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    if request.method == "POST":
        weight = float(request.form["weight"])
        weight_unit = request.form["weight_unit"]
        height = float(request.form["height"])
        height_unit = request.form["height_unit"]
        try:
            bmi = calculate_bmi(weight, weight_unit, height, height_unit)
            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"
        except ValueError as e:
            category = str(e)
    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
