# OBUNACHILAR SONINI ANIQLASH UCHUN
import psycopg2
def get_post(n,n1,n2,n3):
    try:
        con = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Amirxon',
        database='Mart'
    )
        cur = con.cursor()
        table_add = '''
        INSERT INTO obuna1 (
        BOT_ID,
        FRIST_NAME,
        LAST_NAME,
        USERNAME
        ) VALUES (
        %s,%s,%s,%s
        )
        '''
        cur.execute(table_add,(n,n1,n2,n3))
        con.commit()
    except:
        print('eror')
    finally:
        if con:
            cur.close()
            con.close()
            print('add table')
# id = int(input())
# frist_name = input()
# last_name = input()
# username = input()
# get_post(id, frist_name, last_name, username)

