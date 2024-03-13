# MALUMOTLAR UCHUN

import psycopg2

try:
    connection = psycopg2.connect(user = 'postgres', password = 'Amirxon',  host = 'localhost', port = '5432', database = 'Ramazon bot')
    cursor = connection.cursor()
    create_table = '''CREATE TABLE ramazon (     
        NOMI VARCHAR(15) NOT NULL,
        MATN TEXT NOT NULL
        );'''

    
    cursor.execute(create_table)
    connection.commit() 
    print("Table created")
    # print(connection.get_dsn_parameters()) 
    print("You are conneted")

except (psycopg2.Error, Exception) as error:
    print(f"this {error}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Closed")
















