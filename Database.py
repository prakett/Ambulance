import mysql.connector
from faker import Faker
import random

# Create a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zxcvbnm",
    database="Ambulance"
)

cursor = connection.cursor()

fake = Faker()

for _ in range(100):
    Ambulance_id = fake.uuid4()
    Ambulance_number = fake.random_number(digits=4)
    Status = random.choice(['Available', 'Not available', 'Booked'])

    insert_query = "INSERT INTO Ambulance (Ambulance_id, Ambulance_number, Status) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (Ambulance_id, Ambulance_number, Status))

for _ in range(100):
    user_id = fake.random_number(digits=8)  # Adjust the number of digits as needed
    username = fake.user_name()
    password = fake.password()

    insert_query = "INSERT INTO users (User_ID, User_Name, Password) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (user_id, username, password))


connection.commit()
connection.close()
