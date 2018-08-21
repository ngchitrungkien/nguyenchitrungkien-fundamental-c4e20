from flask import Flask,render_template
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer

app = Flask(__name__) 

mlab.connect() #ket noi DB voi server
#design pattern(MVC, MVP)

@app.route('/')
def index():

    return render_template('index.html')
@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g,yob__lte = 1998,height__gte=165,address__icontains="Hà Nội")
    return render_template('search.html',all_service=all_service)

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer=all_customer)

@app.route('/customer/male/not-yet-contacted/first10')
def first10male_notyetcontacted():
    first10 = Customer.objects[0:10]
    all_customer = first10(
        gender=1,
        contacted=False,
    )
    return render_template('customer.html', all_customer=all_customer)

if __name__ == '__main__': 
  app.run(debug=True)