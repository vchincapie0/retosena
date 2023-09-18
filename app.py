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


'''Ruta para el index'''
@app.route('/index')

def index():
    '''Se establece la función para la ruta del index'''
    return render_template('index.html')#Devolvera el template index.html


'''Ruta para el registro'''
@app.route('/registro', methods=['GET','POST'])

def registro():
    '''Función para el registro de ciudadanos'''
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
        return redirect(url_for('home'))#Una vez el ciudadano este registrado se redirecciona al index
    return render_template('registro.html')


'''Ruta para el login'''
@app.route('/login', methods=['GET','POST'])

def login():
    '''Función para el ingreso de usuarios(ciudadanos y administradores)'''
    if request.method == 'POST' and 'email' in request.form and 'contrasenia':
        email=request.form['email']
        password=request.form['contrasenia']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM ciudadanos,administradores where ciudadanos.email=%s AND ciudadanos.contraseña=%s OR administradores.email=%s AND administradores.contraseña=%s',(email,password,email,password))
        account = cur.fetchone()

        if account:
            session['Logueado']=True


            flash('Bienvenido')
            return redirect(url_for('home'))#si el usuario ingresa correctamente lo redireccionara al home
        else:
            flash('Datos incorrectos')#Si no, le saldra un mensaje de validacion y lo redirigirá al login de nuevo 
            return render_template('login.html')
    return render_template('login.html')


@app.route('/home')
def home():
    '''Función para el home'''
    return render_template('home.html')


@app.route('/home/sondeos')
def sondeos():
    '''Función para los sondeos'''
    return render_template('sondeos.html')


@app.route('/admin')
def admin():
    '''Funcion para el home de administrador'''
    return render_template('admin.html')

@app.route('/admin/sondeos')
def crear_sondeos():
    '''Funcion para que el administrador cree sondeos'''
    return render_template('crear.html')



if __name__=='__main__':
    #Se verifica que se este corriendo la aplicacion.
    app.run(debug=True)