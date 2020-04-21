
from sqlalchemy import create_engine

from akit.datum.orm import AutomationBase

def create_sqlite_database():

    engine = create_engine('sqlite:///C:\\sqlitedbs\\school.db', echo=True)

    AutomationBase.metadata.create_all(engine, checkfirst=True)

    return

