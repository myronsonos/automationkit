
import traceback

from sqlalchemy import create_engine

from akit.datum.orm import AutomationPod

def database_exists(username, password, dbname):
    engine = create_engine('postgresql://%s:%s@localhost:5432/postgres' % (username, password), echo=True)
    result = engine.execute("SELECT 1 AS result FROM pg_database WHERE datname='%s'" % dbname)
    return result.rowcount > 0


def database_create(username, password, dbname):
    engine = create_engine('postgresql://%s:%s@localhost:5432/postgres' % (username, password), echo=True)

    conn = engine.connect()
    try:
        conn.connection.set_isolation_level(0)
        result = conn.execute("CREATE DATABASE %s" % dbname)
    except Exception as xcpt:
        print(traceback.format_exc())
        raise
    finally:
        conn.close()

    return

def create_apod_postgresql_database(username, password):

    if not database_exists(username, password, "apod"):
        database_create(username, password, "apod")

    engine = create_engine('postgresql://%s:%s@localhost:5432/apod' % (username, password), echo=True)

    AutomationPod.metadata.create_all(engine, checkfirst=True)

    return

def open_apod_postgresql_database(username, password):
    
    create_apod_postgresql_database(username, password)

    engine = create_engine('postgresql://%s:%s@localhost:5432/apod' % (username, password), echo=True)

    return engine

if __name__ == "__main__":
    create_apod_postgresql_database("websvc", "Acess2Data!!")
