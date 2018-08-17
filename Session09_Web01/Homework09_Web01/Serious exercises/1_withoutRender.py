from flask import Flask
app = Flask(__name__)

@app.route('/BMI/<int:weight_kg>/<int:height_cm>')
def BMI(weight_kg, height_cm):
    height_m = height_cm/100
    BMI = weight_kg / (height_m ** 2)
    if BMI < 16:
        body = "Severely underweight"
    elif BMI < 18.5:
        body = "Underweight"
    elif BMI < 25:
        body = "Normal"
    elif BMI < 30:
        body = "Overweight"
    else:
        body = "Severely overweight"
    return("Your BMI: {} ===> You are: {}".format(BMI,body))

if __name__ == '__main__':
  app.run(debug=True)
