from flask import *
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

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html',all_service=all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return'Service not found'


@app.route('/new-service', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('new-service.html')
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        address = form['address']

        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender,
            address = address
        )
        new_service.save()

        return redirect(url_for('admin'))

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service = service)    

@app.route('/update-service/<service_id>', methods = ['GET', 'POST'])
def update_service(service_id):
    service = Service.objects.with_id(service_id)
    if request.method == 'GET':
        return render_template('update-service.html', service = service)
    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        service.name = name
        service.yob = yob
        service.phone = phone

        service.save()
        
        return redirect(url_for('admin'))

if __name__ == '__main__': 
  app.run(debug=True)

#setdefault input value
#radio button