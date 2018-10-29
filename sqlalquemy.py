from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
from functions import data_frame, get_one_year_ago, make_dic

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, and_, or_

engine = create_engine("sqlite:///./data/hawaii.sqlite")
inspector = inspect(engine)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


def getPrecipitation():
    # Get the latest date from database.
    precipitation_last_date = session.query(Measurement.date)\
        .order_by(Measurement.date.desc())\
        .first()[0]

    # Calculate one year ago from last date.
    one_year_ago = get_one_year_ago(precipitation_last_date)

    # Design a query to retrieve the last 12 months of precipitation data and plot the results
    precipitation = session.query(Measurement.date, Measurement.tobs)\
        .filter(and_(Measurement.date >= one_year_ago, Measurement.date <= precipitation_last_date))\
        .filter(Measurement.prcp != "None")\
        .order_by(Measurement.date)\
        .all()

    return make_dic(precipitation, ["date", "tobs"])

def getListStations():
    # Get the latest date from database.
    precipitation_last_date = session.query(Measurement.date)\
        .order_by(Measurement.date.desc())\
        .first()[0]

    # Calculate one year ago from last date.
    one_year_ago = get_one_year_ago(precipitation_last_date)

    stations = session.query(Measurement.station, Station.name)\
        .filter(and_(Measurement.date >= one_year_ago, Measurement.date <= precipitation_last_date))\
        .group_by(Measurement.station)\
        .all()

    return make_dic(stations, ["station", "name"])
    
def getTempertureObservations():
    # Get the latest date from database.
    precipitation_last_date = session.query(Measurement.date)\
        .order_by(Measurement.date.desc())\
        .first()[0]

    # Calculate one year ago from last date.
    one_year_ago = get_one_year_ago(precipitation_last_date)

    stations = session.query(Measurement.tobs, Measurement.station)\
        .filter(and_(Measurement.date >= one_year_ago, Measurement.date <= precipitation_last_date))\
        .group_by(Measurement.station)\
        .all()

    return make_dic(stations, ["tobs", "station"])

def getTobsDescrip(start_date):
    temp_qr = session.query(Measurement.station, Measurement.tobs)\
        .filter(Measurement.date >= start_date)\
        .all()

    return make_dic(temp_qr, ['station', 'tobs'])

def getTobsDescrip2(start_date, end_date):
    temp_qr = session.query(Measurement.station, Measurement.tobs)\
        .filter(and_(Measurement.date >= start_date, Measurement.date <= end_date))\
        .all()

    return make_dic(temp_qr, ['station', 'tobs'])