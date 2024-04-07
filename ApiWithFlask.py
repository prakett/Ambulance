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

if __name__ == '__main__':
    app.run(debug=True)
