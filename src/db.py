import os
import sqlite3
from log import logger

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
            definitions JSON NOT NULL,
            isFavorite INTEGER DEFAULT 0
        );
        '''
        db.execute(createSQL)
    except Exception as e:
        print("Error Creating Table ", e)
        logger.error(f"file: {__file__} -> {e}")
    finally:
        db.close() # Close Database Connection

# make sure database exists already
def insertInto(data, currentIndex):
    f'''
    Insert Into Table {TABLE_NAME}
    '''
    try:
        db = sqlite3.connect(CURRENT_DB)
        insertSQL = f'''
        INSERT INTO {TABLE_NAME}
        VALUES
        (?, ?, ?, ?)
        '''
        cursor = db.cursor()
        cursor.execute(insertSQL, data)
        db.commit()
        print("Item Added ", currentIndex, " = [word] -> ", data[0])
    except Exception as e:
        print("Error Database Insertion", e)
        logger.error(f"file: {__file__} -> {e}")
        raise Exception("Database Error")
    finally:
        cursor.close()
        db.close() # Close Database Connection