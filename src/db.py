import os
from posixpath import curdir
import sqlite3

# Constants
CURRENT_DB = os.getcwd() + "\\src\\" + 'data.sqlite'
TABLE_NAME = 'dictionary'

# SHOULD BE RUN ONCE (AFTER THE DB FILE IS CREATED YOU NO LONGER NEED TO CALL THIS)
def createDatabaseFile():
    '''
    Creates Database File
    '''

    fDB = None
    try:
        fDB = open(CURRENT_DB, 'w+')
    except Exception as e:
        print("An Error Occured While Making Database File:", e)
    finally:
        fDB.close() # close file descriptor

# RUN ONCE, (CAN BE RUN MULTIPLE IF DATABASE HAS ERROR, THIS RECREATE THE TABLE AND REMOVE ALL DATA PREVIOUSLY ADDED)
def createTable():
    '''
    Create a Table from the Database
    '''
    db = None
    try:
        db = sqlite3.connect(CURRENT_DB)
        createSQL = f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
            word TEXT PRIMARY KEY,
            origin TEXT,
            definitions JSON NOT NULL
        );
        '''
        db.execute(createSQL)
    except Exception as e:
        print("Error Creating Table", e)
    finally:
        db.close() # Close Database Connection

# make sure database exists already
def insertInto(data):
    f'''
    Insert Into Table {TABLE_NAME}
    '''
    try:
        db = sqlite3.connect(CURRENT_DB)
        insertSQL = f'''
        INSERT INTO {TABLE_NAME}
        VALUES
        (?, ?, ?)
        '''
        cursor = db.cursor()
        cursor.execute(insertSQL, data)
        db.commit()
        print(cursor.lastrowid)
    except Exception as e:
        print("Error Creating Table", e.with_traceback)
        raise Exception("Database Error")
    finally:
        cursor.close()
        db.close() # Close Database Connection