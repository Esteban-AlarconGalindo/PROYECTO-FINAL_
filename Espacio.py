from db import db

class Espacio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(100))
    estrato = db.Column(db.Integer)
    sentido_via = db.Column(db.String(50))
    estado_via = db.Column(db.String(50))  # Asegúrate que sea STRING
    tipo_via = db.Column(db.String(50))
    horas_congestion = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, direccion, estrato, sentido_via, estado_via, tipo_via, horas_congestion, lat, lng):
        self.direccion = direccion
        self.estrato = estrato
        self.sentido_via = sentido_via
        self.estado_via = estado_via
        self.tipo_via = tipo_via
        self.horas_congestion = horas_congestion
        self.lat = lat
        self.lng = lng
