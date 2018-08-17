from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
        'Minh':{
            'name': 'Minh',
            'gender': 'Male',
            'age': 18,
            'hobbies': 'Singing'
        },
        'Xuan':{
            'name': 'Xuan',
            'gender': 'Female',
            'age': 19,
            'hobbies': 'Shopping'
        },
        'Trang':{
            'name': 'Trang',
            'gender': 'Female',
            'age': 19,
            'hobbies': 'Make-up'
        },
        'Nhat':{
            'name': 'Nhat',
            'gender': 'Male',
            'age': 19,
            'hobbies': 'Football'
        }
    }
    if username in users:
        return render_template('user.html', username = users[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)