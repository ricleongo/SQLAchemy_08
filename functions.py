import pandas as pd

def make_dic(query, columns):
    """
    Takes a sqlalchemy query and a list of columns, returns a dictionary.
    """    
    def make_row(x):
        return dict([(c, getattr(x, c)) for c in columns])

    return [make_row(x) for x in query]


def data_frame(query, columns):
    """
    Takes a sqlalchemy query and a list of columns, returns a dataframe.
    """
    def make_row(x):
        return dict([(c, getattr(x, c)) for c in columns])

    return pd.DataFrame([make_row(x) for x in query])

def get_one_year_ago(precipitation_last_date):
    """
    Get a date year ago from the input parameter.
    """
    from datetime import datetime, timedelta

    # Calculate one year ago from the last date found in database.
    return (datetime.strptime(precipitation_last_date, "%Y-%m-%d") - timedelta(days = 365)).strftime("%Y-%m-%d")
