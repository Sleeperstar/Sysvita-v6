from src.database.db import connection
from src.models.Paciente import Paciente
from src.models.Especialista import Especialista

# Función para manejar el inicio de sesión
def postLogin(correo, contra):
    try:
        conn = connection()  # Conecta a la base de datos
        usuario = None

        # Verifica en la tabla de Pacientes
        inst_paciente = '''
            SELECT PAC.* FROM Paciente PAC
            WHERE PAC.email = %(email)s
            AND PAC.contra = %(contra)s;
        '''
        with conn.cursor() as cursor:
            cursor.execute(inst_paciente, {'email': correo, 'contra': contra})
            row = cursor.fetchone()
            if row:
                usuario = Paciente(row[1], row[2], row[3], row[4])
                usuario.id_pac = row[0]
            cursor.close()

        # Si no se encontró en Pacientes, verifica en Especialistas
        if not usuario:
            inst_especialista = '''
                SELECT ESP.* FROM Especialista ESP
                WHERE ESP.correo = %(correo)s
                AND ESP.password = %(password)s;
            '''
            with conn.cursor() as cursor:
                cursor.execute(inst_especialista, {'correo': correo, 'password': contra})
                row = cursor.fetchone()
                if row:
                    usuario = Especialista(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    usuario.codigo = row[0]
                cursor.close()

        conn.close()
        return usuario  # Devuelve el usuario encontrado
    except Exception as e:
        print("→ Error: " + str(e))
        return ''
