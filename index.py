from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/lenguajes')
def mostrarLenguajes():
    mislenguajes=("PHP","Python","Java","C#","JavaScript","Perl","Ruby","Rust")
    return render_template('lenguajes.html', lenguajes=mislenguajes)

@app.route("/contacto")
def contacto():
    return render_template('contact.html')

if __name__ == '__main__':
   app.run(debug=True, port=5817)