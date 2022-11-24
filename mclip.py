import sys
import pyperclip

TEXT = {'ok': 'Ok, grazie.',
        '10x': 'Grazie.',
        'dispo': 'Resto a disposizione, grazie.',
        }


if len(sys.argv) < 2:
    print('Usage: python myclip [keyphrase]')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' in clipboard.')
else:
    print('No text for: ' + keyphrase)
