from src.database.db import connection

def postRegisterEspecialista(nombre, apellido, correo, password, hospital, especialidad, consultorio):
    try:
        conn = connection()
        inst = '''
                INSERT INTO Especialista (nombre, apellido, correo, password, hospital, especialidad, consultorio)
	                VALUES (%(nombre)s, %(apellido)s, %(correo)s, %(password)s, %(hospital)s, %(especialidad)s, %(consultorio)s);
            '''
        with conn.cursor() as cursor:
            cursor.execute(inst, {
                'nombre': nombre,
                'apellido': apellido,
                'correo': correo,
                'password': password,
                'hospital': hospital,
                'especialidad': especialidad,
                'consultorio': consultorio
            })
            conn.commit()
            cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("→ Error: " + str(e))
        return False
