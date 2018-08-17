import os
from flask import Flask,redirect,render_template

app = Flask(__name__)

@app.route('/about-me/')
def introduce_myself():
    infos = {
            'name': 'Nguyễn Chí Trung Kiên',
            'age': 18,
            'university': 'Hanoi University Of Science and Technology',
            'hobbies': 'Football, Tennis, Singing, Beatboxing, Cooking,...',
            'dogs': "I have 4 dogs: Corgi - Her name's Lim; Bulldog English - His name's Bun; Malinois - Her name's Mun; Pug - Her name's Su"
        }
    return render_template('introduce_myself.html', infos = infos)
   
@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=301)

if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
 
    