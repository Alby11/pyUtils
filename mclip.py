from calendar import month_name
from datetime import datetime
import pwd
import sys
from time import time
import pyperclip
from datetime import date, time
from translate import Translator
import secrets
import string

TEXT = {'ok': 'Ok, grazie.',
        '10x': 'Grazie.',
        'dispo': 'Resto a disposizione, grazie.',
        }


if len(sys.argv) < 2:
    print('''
    Usage:

    myclip [keyphrase] -- to put a keyphase into clipboard
    myclip generate -- to generate a password following "MonthYY!!" pattern
    myclip genrandom -- to generate a random pw
    ''')
    sys.exit()

keyphrase = sys.argv[1]
if keyphrase == "generate":
    translator = Translator(to_lang="italian")
    month = datetime.now().strftime("%B").capitalize()
    month = translator.translate(month)
    year = datetime.now().strftime("%y")
    result = month + year + "!!"
    pyperclip.copy(result)
    print(result)
    sys.exit()

if keyphrase == "random":
    alphabet = string.ascii_letters + string.digits + string.punctuation
    pwdLength = 14
    pwd = ''
    for i in range(pwdLength):
        pwd += ''.join(secrets.choice(alphabet))
    pyperclip.copy(pwd)
    print(pwd)
    sys.exit()

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' in clipboard.')
else:
    print('No text for: ' + keyphrase)
