from os import path, getcwd
from json import dumps
import sqlite3

CURRENT_DB = getcwd() + "\\src\\" + 'data.sqlite'
CURRENT_JSON = getcwd() + "\\src\\" + 'words.json'

def main():
    if path.exists(CURRENT_DB):
        db = None
        cursor = None
        try:
            data = []
            db = sqlite3.connect(CURRENT_DB)
            cursor = db.cursor()
            cursor.execute("SELECT word FROM dictionary")

            rows = cursor.fetchall()
            for row in rows:
                data.append(row[0])
            
            parsed = dumps(data, ensure_ascii=True, indent=3) # convert to json string
            # put data to json file
            with open(CURRENT_JSON, 'w') as json_file:
                json_file.writelines(parsed)
                json_file.close()

        except Exception as e:
            print("Error on Database")
            print(e)
        finally:
            cursor.close()
            db.close()
    else:
        print('Error Database Does Not Exist\nReasons:\n- `data.sqlite` is not yet created, run `main.py` first before running this command\n- file may be `deleted`, `moved` or `renamed`')

if __name__ == '__main__':
    main()