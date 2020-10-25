#! python
# mapIt.py - Launches a map in the browser using an address from the
# comand line clip board
import webbrowser
import sys
import pyperclip

if len(sys.argv[1:]) > 1:
    # take the argument provided from the cli
    address = ' '.join(sys.argv[1:])
else:
    # take the input from  clipboard
    address = pyperclip.paste()

# url to be opened
addressUrl = ('https://maps.google.com/maps/place/' + address)
webbrowser.open(addressUrl)
