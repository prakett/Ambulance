from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

database = {
    'host': 'localhost',
    'user': 'root',
    'password': 'zxcvbnm',
    'database': 'ambulance'
}

def connect_mysql():
    return mysql.connector.connect(**database)

@app.route('/ambulances', methods=['GET'])
def ambulance():
    try:
        connection = connect_mysql()
        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT * FROM ambulances')
        ambulances = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(ambulances)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/users', methods=['GET'])
def get_users():
    try:
        connection = connect_mysql()
        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(users)

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/register',methods =['POST'])
def register():
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Email and password are required'}), 400

        connection = connect_mysql()
        cursor = connection.cursor()

        query = 'Insert into users (email,password) values (%s,%s)'
        cursor.execute(query,(email,password))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({'message': 'Registration successful!'}),201
    except Exception as e:
        return jsonify({'error':str(e)}),500



if __name__ == '__main__':
    app.run(debug=True)
