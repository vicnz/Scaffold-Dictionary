import traceback
from requests import get
from main import DatabaseError
from log import logger

def loopThrough(fun, end, start = 1):
    '''
    Parse Url Links\n
    Derived Operation
    '''
    i = start;
    while i <= end:
        number = str(i)
        strLength = len(number)
        j = 0;
        while j < 5 - strLength:
            number = '0' + str(number)
            j += 1
        parced_string = f'https://sil-philippines-languages.org/online/ivb/dict/lexicon/lx{number}.html'

        try:
            request = get(parced_string);
            if request.ok :
                fun(request.text, currentIndex=i) # operate on the string operation
            else:
                raise Exception(f"Connection Error : {request.reason}")
        except DatabaseError as e:
            print(f"Connection Error\nError at Index [{i}]")
            logger.error(f"Execution Terminated At Index -> [{i}]")
            logger.error(f"file: {__file__} -> {e}")
            print(e)
            traceback.print_exc()
            break
        except Exception as e:
            print(f"Connection Error\nError at Index [{i}]")
            logger.error(f"Execution Terminated At Index -> [{i}]")
            logger.error(f"file: {__file__} -> {e}")
            print(e)
            traceback.print_exc()
            break
        finally:
            request.close()

        i = i + 1