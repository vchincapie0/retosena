from flask import Flask, render_template

app = Flask(__name__)#Se especifica que este archivo es el que va a iniciar la webapp

@app.route('/')
def index():
    '''Se establece la funcion para la ruta del index'''
    return render_template('index.html')#Devolvera el template index.html

@app.route('/registro')
def registro():
    '''Funcion para el registro de ciudadanos'''
    return 'Aqui se van a registrar los ciudadanos'

@app.route('/login')
def login():
    '''Funcion para el ingreso de usuarios'''
    return render_template('login.html')

if __name__=='__main__':
    #Se verifica que se este corriendo la aplicacion.
    app.run(debug=True)