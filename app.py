from flask import Flask, jsonify
import sqlalquemy as sa

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(sa.getPrecipitation())

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(sa.getListStations())

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(sa.getTempertureObservations())

@app.route("/api/v1.0/<start>")
def filter1(start):
    # 2016-08-23
    return jsonify(sa.getTobsDescrip(start))

@app.route("/api/v1.0/<start>/<end>")
def filter2(start, end):
    # 2016-08-23 - 2017-08-23
    return jsonify(sa.getTobsDescrip2(start, end))


if __name__ == "__main__":
    app.run(debug=True)