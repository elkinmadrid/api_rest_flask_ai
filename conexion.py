## LA CONEXION A LA BASE DE DATOS
import mysql.connector

class conexion: 
    
    
    def run_query(query='', arge={}, one = False):


        conn = mysql.connector.connect( host='database-1.cd4clhrqd9yb.us-east-1.rds.amazonaws.com', 
                                        user= 'admin', 
                                        passwd='1143463269Cc', 
                                        db='database1' ) # Conectar a la base de datos 
        cursor = conn.cursor()         # Crear un cursor 

        print(query)
        # PREGUNTAMOS SI ES UNA SELECT -> SI ES UN SELECT TRAEMOS LOS REGISTROS SI EXISTEN, SINO ES UN SELECT HACEMOS COMMIT PARA CONFIRMAR LOS 		#CAMBIOS	
        if query.upper().startswith('SELECT'): 
            cursor.execute(query)          # Ejecutar una consulta 
           # r = [dict((cursor.description[i][0], value) \
            #   for i, value in enumerate(row)) for row in cursor.fetchall()]
            #return (r[0] if r else None) if one else r
            data = cursor.fetchall()
            
        else:
            print (arge)
            cursor.execute(query, arge)
            conn.commit()                   
            
            data = cursor.lastrowid    
    

        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 
        print (data)
        return data
