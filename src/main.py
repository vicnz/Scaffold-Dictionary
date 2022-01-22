import app as app
import sys

def runCommand():

    countVal = 10
    startVal = 1
    initDB = True

    def showHelp():
        message = '''
Run Commands
USAGE:
    python main.py [--count=int | 10, [--start=int | 1, --init]]
    - '--count' -> int + number must not exceed 60000
    - '--start' -> int + number must not exceed 1 or below
    - '--init' -> no parameter + initialize database
        '''

        print(message)
    # by default set the Count (Defaults: 10)

    if("--count" in sys.argv):
        countindex = sys.argv.index("--count")
        countvalue = 0
        try:
            countvalue = int(sys.argv[countindex + 1])
            countVal = countvalue
        except:
            print("ARGUMENT ERROR FOR '--count'")
            showHelp()
            return None
    else:
        pass

    if "--start" in sys.argv:
        startIndex = sys.argv.index("--start")
        startvalue = 1
        try:
            startvalue = int(sys.argv[startIndex + 1])
            startVal = startvalue
        except:
            print("ARGUMENT ERROR FOR '--start'")
            showHelp()
            return None
    else:
        pass

    # create Database
    if "--init" in sys.argv:
        print("Initialized Database")
    else:
        pass
    
    if(countVal < startVal):
        print(f"START [{startVal}] CANNOT BE GREATER THAN THE COUNT [{countVal}]")
        showHelp()
    else:
        return(countVal, startVal, initDB)


def main(*params):
    result = runCommand()
    if(result == None):
        print("COMMAND FINISHED")
        sys.exit()
    else:
        app.Main(start=result[1], count=result[0], initDB=result[2])


if __name__ == '__main__':
    main()