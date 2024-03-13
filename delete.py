# import psycopg2 as ps2
# try:
#     con = ps2.connect(
#         host='localhost',
#         user='postgres',
#         password='Amirxon',
#         database='Ramazon bot'
#     )
   
#     cur = con.cursor()
#     rec = '''
#     DELETE FROM ramazon WHERE NOMI = 'Саждаи саҳв'
#     '''
#     cur.execute(rec)
#     con.commit()
#     print('Start!')
    
# except (Exception,ps2.Error) as err:
#     print(f'your mistake:{err}')
    
# finally:
#     if con:
#         cur.close()
#         con.close()
#         print('all close!')


import psycopg2 as ps2
try:
    con = ps2.connect(
        host='localhost',
        user='postgres',
        password='Amirxon',
        database='Mart'
    )
   
    cur = con.cursor()
    rec = '''
    DELETE FROM BOT1 WHERE BOT_ID = 6512709243
    '''
    cur.execute(rec)
    con.commit()
    print('Start!')
    
except (Exception,ps2.Error) as err:
    print(f'your mistake:{err}')
    
finally:
    if con:
        cur.close()
        con.close()
        print('all close!')