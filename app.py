from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL 

app = Flask(__name__)#Se especifica que este archivo es el que va a iniciar la webapp

'''Conexión a bd'''
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='pruebaproyecto'
mysql=MySQL(app)

'''Settings'''
app.secret_key='mysecretkey'

@app.route('/index')
def index():
    '''Se establece la funcion para la ruta del index'''
    return render_template('index.html')#Devolvera el template index.html

@app.route('/registro', methods=['GET','POST'])
def registro():
    '''Funcion para el registro de ciudadanos'''
    if request.method == 'POST':
        documento = request.form['documento']
        nombres = request.form['nombres']
        sexo = request.form['sexo']
        fechanacimiento= request.form['fecha_nacimiento']
        telefono= request.form['telefono_celular']
        apellidos=request.form['apellidos']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO ciudadano(tipodocumento,nombre,sexo,fechanacimiento,telefonos,apellidos) VALUES(%s,%s,%s,%s,%s,%s)',(documento,nombres,sexo,fechanacimiento,telefono,apellidos))
        mysql.connection.commit()
        flash('Ciudadano Agregado')
        return redirect(url_for('index'))
    return render_template('registro.html')



@app.route('/login')
def login():
    '''Funcion para el ingreso de usuarios'''
    return render_template('login.html')

if __name__=='__main__':
    #Se verifica que se este corriendo la aplicacion.
    app.run(debug=True)