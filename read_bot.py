import psycopg2 as ps2

def reading12():
    try:
        con = ps2.connect(
        host='localhost',
        user='postgres',
        password='Amirxon',
        database='Mart'
    )
        cur = con.cursor()
        cur.execute('select * from obuna1') 
        res = cur.fetchall()
        return res
    except (Exception,ps2.Error) as err:
        print(f'your mistake:{err}')
    finally:
        if con:
            cur.close()
            con.close()
            print('all reading')

