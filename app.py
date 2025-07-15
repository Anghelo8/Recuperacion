from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    "host": "recuperacion.cjcko4j36hk3.us-east-1.rds.amazonaws.com",       # Cambiar a la dirección de tu servidor MySQL
    "user": "admin",            # Cambiar a tu usuario de MySQL
    "password": "admin2025",    # Cambiar a tu contraseña de MySQL
    "database": "registro_db"  # Nombre de la base de datos
}

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para recibir los datos del formulario
@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']

        # Conectar a la base de datos
        connection = pymysql.connect(
            host=db_config['host'],        # Accede correctamente a 'host'
            user=db_config['user'],        # Accede correctamente a 'user'
            password=db_config['password'],# Accede correctamente a 'password'
            database=db_config['database'] # Accede correctamente a 'database'
        )

        try:
            with connection.cursor() as cursor:
                # Consulta SQL para insertar datos
                sql = "INSERT INTO registros (nombre, apellido, fecha) VALUES (%s, %s, %s)"
                cursor.execute(sql, (nombre, apellido, fecha))
                connection.commit()  # Confirmar los cambios
        finally:
            connection.close()  # Cerrar la conexión

        return redirect(url_for('index'))

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)

