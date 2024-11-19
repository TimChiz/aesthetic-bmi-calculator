from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def bmi_calculator():
    bmi = None
    category = ""
    if request.method == "POST":
        weight = float(request.form.get("weight"))
        weight_unit = request.form.get("weight_unit")
        height = float(request.form.get("height"))
        height_unit = request.form.get("height_unit")

        # Convert weight to kilograms
        if weight_unit == "tonnes":
            weight *= 1000
        elif weight_unit == "grams":
            weight /= 1000
        elif weight_unit == "lbs":
            weight *= 0.453592

        # Convert height to meters
        if height_unit == "cm":
            height /= 100
        elif height_unit == "inch":
            height *= 0.0254
        elif height_unit == "ft":
            height *= 0.3048

        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
