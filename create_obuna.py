import psycopg2

try:
    connection = psycopg2.connect(user = 'postgres', password = 'Amirxon',  host = 'localhost', port = '5432', database = 'Mart')
    cursor = connection.cursor()
    create_table = '''CREATE TABLE obuna1 (     
        BOT_ID BIGINT PRIMARY KEY,
        FRIST_NAME TEXT,
        LAST_NAME TEXT,
        USERNAME VARCHAR(20) 
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
