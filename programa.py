

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///espacios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class EspacioPublico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_via = db.Column(db.String(50))
    numero_principal = db.Column(db.Integer)
    letra_principal = db.Column(db.String(2))
    bis = db.Column(db.String(10))
    numero_secundario = db.Column(db.String(50))
    estrato = db.Column(db.String(10))
    sentido_via = db.Column(db.String(100))
    estado_via = db.Column(db.String(50))
    tipo_via_clasificacion = db.Column(db.String(50))  # Para "Vía Principal/Secundaria"
    horas_congestion = db.Column(db.String(50))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

@app.route('/', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nuevo = EspacioPublico(
            tipo_via=request.form['tipo_via'],
            numero_principal=request.form['numero_principal'],
            letra_principal=request.form['letra_principal'],
            bis=request.form['bis'],
            numero_secundario=request.form['numero_secundario'],
            estrato=request.form['estrato'],
            sentido_via=request.form['sentido_via'],
            estado_via=request.form['estado_via'],
            tipo_via_clasificacion=request.form['tipo_via'],
            horas_congestion=request.form['horas_congestion'],
            lat=request.form['lat'],
            lng=request.form['lng']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect('/consulta')
    return render_template("agregar_espacio.html")

@app.route('/consulta')
def consulta():
    espacios = EspacioPublico.query.all()
    return render_template("consultaDireccion.html", espacios=espacios)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

