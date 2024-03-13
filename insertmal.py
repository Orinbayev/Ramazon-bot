import psycopg2 as ps2
def add_cmd(n1, n2):
    try:
        con = ps2.connect(
        host='localhost',
        user='postgres',
        password='Amirxon',
        database='Ramazon bot'
    )
        cur = con.cursor()
        table_add = '''
        INSERT INTO ramazon(
        NOMI,
        MATN
        ) VALUES (
        %s,%s
        )
        '''
        cur.execute(table_add,(n1, n2))
        con.commit()
    except:
        print('eror')
    finally:
        if con:
            cur.close()
            con.close()
            print('add table')
