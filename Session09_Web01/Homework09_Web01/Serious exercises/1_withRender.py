from flask import Flask, render_template
app = Flask(__name__)

@app.route('/BMi/<int:weight_kg>/<int:height_cm>')
def BMI(weight_kg, height_cm):
    
    height_m = height_cm /100
    BMI = weight_kg / (height_m ** 2)

    return render_template('BMI.html', BMI = BMI)

if __name__ == '__main__':
  app.run(debug=True)