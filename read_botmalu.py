import psycopg2 as ps2

def oqish():
    try:
        con = ps2.connect(
        host='localhost',
        user='postgres',
        password='Amirxon',
        database='Ramazon bot'
    )
        cur = con.cursor()
        cur.execute('select * from ramazon') 
        res = cur.fetchall()
        return res
    except (Exception,ps2.Error) as err:
        print(f'your mistake:{err}')
    finally:
        if con:
            cur.close()
            con.close()
            print('all reading')
# print(reading())
