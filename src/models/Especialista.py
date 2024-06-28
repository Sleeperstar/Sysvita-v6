from src.database.db import db

# Define el modelo Especialista
class Especialista(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120))
    apellido = db.Column(db.String(120))
    correo = db.Column(db.String(80))
    password = db.Column(db.Text)
    hospital = db.Column(db.String(120))
    especialidad = db.Column(db.String(120))
    consultorio = db.Column(db.String(120))

    # Constructor para inicializar una instancia de Especialista
    def __init__(self, nombre, apellido, correo, password, hospital, especialidad, consultorio) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.hospital = hospital
        self.especialidad = especialidad
        self.consultorio = consultorio

    # Método para convertir una instancia de Especialista a formato JSON
    def to_json(self):
        return {
            'codigo': self.codigo,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'password': self.password,
            'hospital': self.hospital,
            'especialidad': self.especialidad,
            'consultorio': self.consultorio
        }
