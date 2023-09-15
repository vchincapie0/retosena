from flask import Flask, render_template, request, redirect,url_for,flash,session
from flask_mysqldb import MySQL 

app = Flask(__name__)#Se especifica que este archivo es el que va a iniciar la webapp

'''Conexión a bd'''
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='partciudadana'
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
        tipodocumento = request.form['TipoDocumento']
        documento = request.form['numero_documento']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        etnia = request.form['etnia']
        fechanacimiento= request.form['fecha_nacimiento']
        telefonoCelular= request.form['telefono_celular']
        telefonoFijo= request.form['telefono_fijo']
        municipio=request.form['municipio']
        barrioVereda= request.form['barrio_vereda']
        direccion = request.form['direccion']
        estrato=request.form['estrato_residencia']
        educacion = request.form['nivel_educativo']
        discapacidad = request.form['discapacidad']
        conectividad = request.form['conectividad_internet']
        accesoTecnologia = request.form['acceso_tecnologico']
        cualAccTecnol = request.form['dispositivos_tecnologicos']
        regimen = request.form['regimen_afiliacion']
        email = request.form['email']
        password= request.form['contrasenia']

        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO ciudadanos(tipoDocumento,numeroDocumento,nombres,apellidos,sexo,fechaNacimiento,telefonoCelular,telefonoFijo,nivelEducativo,conectividad,etnia,dicapacidad,dispositivosTecnologicos,cualesDispTecn,regimenAfiliacion,municipio,barrioVereda,direccion,estrato,email,contraseña) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(tipodocumento,documento,nombres,apellidos,sexo,fechanacimiento,telefonoCelular,telefonoFijo,educacion,conectividad,etnia,discapacidad,accesoTecnologia,cualAccTecnol,regimen,municipio,barrioVereda,direccion,estrato,email,password))
        mysql.connection.commit()
        flash('Ciudadano Agregado')
        return redirect(url_for('index'))#Una vez el ciudadano este registrado se redirecciona al index
    return render_template('registro.html')



@app.route('/login', methods=['GET','POST'])
def login():
    '''Funcion para el ingreso de usuarios'''
    if request.method == 'POST' and 'email' in request.form and 'contrasenia':
        email=request.form['email']
        password=request.form['contrasenia']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM ciudadanos,administradores where ciudadanos.email=%s AND ciudadanos.contraseña=%s OR administradores.email=%s AND administradores.contraseña=%s',(email,password,email,password))
        account = cur.fetchone()

        if account:
            session['Logueado']=True

            return redirect(url_for('index'))
        else:
            flash('Usuario y/o contraseña incorrecta')
            return render_template('login.html')
    return render_template('login.html')

if __name__=='__main__':
    #Se verifica que se este corriendo la aplicacion.
    app.run(debug=True)