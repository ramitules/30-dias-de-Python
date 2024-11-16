from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
# Sin cache para archivos estaticos
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')  # Este decorador crea la ruta HOME
def home():
    # return '<h1>Bienvenido!<h1>'
    techs = ('HTML', 'CSS', 'Flask', 'Python')
    nombre = '30 dias de Python'
    return render_template('home.html', techs=techs, name=nombre, title='Home')  # Con template


@app.route('/about')
def about():
    # return '<h1>Acerca de<h1>'
    nombre = '30 dias de Python'
    return render_template('about.html', name=nombre, title='Acerca de')  # Con template


@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/post', methods=['GET', 'POST'])
def post():
    nombre = 'Analisis de texto'
    if request.method == 'GET':
        return render_template('post.html', name=nombre, title=nombre)

    if request.method == 'POST':
        contenido = request.form['content']
        print(contenido)
        return redirect(url_for('result'))


if __name__ == '__main__':
    # Para deploy usamos environ, asi funciona tanto en produccion como en desarrollo
    puerto = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=puerto)
