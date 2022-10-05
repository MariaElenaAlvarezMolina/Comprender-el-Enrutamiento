from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<nombre>')
def say(nombre):
    return f'¡Hola, {nombre}!'

@app.route('/repeat/<int:num>/<string:str>')
def repeat(str,num):
    return (str * num)

@app.errorhandler(404)
def not_found(str):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'



if __name__=='__main__':
    app.run(debug=True)