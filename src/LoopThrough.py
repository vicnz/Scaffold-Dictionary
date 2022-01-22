from array import array
from requests import get

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
        fun(parced_string, index=i) # operate on the string operation
        i = i + 1