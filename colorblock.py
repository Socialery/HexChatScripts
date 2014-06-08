import xchat
import re

__module_name__ = "ColorBlock"
__module_author__ = "Socialery"
__module_version__ = "1"
__module_description__ = ("disables single-colored lines,"
                          "Mibbit users for example")

edited = False

stripper=re.compile(
    r'^\003(?:\d\d?(?:,\d\d?)?)?([^\003]*)(?:\003(?:\d\d?(?:,\d\d?)?)?)?')

def decolor_cb(word, word_eol, event, attr):
    global edited
    #Ignore our own events, bouncer playback, empty messages
    if edited or attr.time or not len(word) > 1:
        return
    result = stripper.match(word[1])
    if result:
        edited = True
        xchat.emit_print(event,word[0],result.group(1),*word[2:])
        edited = False
        return xchat.EAT_ALL
    
for x in ['Channel Message','Channel Action']:
    xchat.hook_print_attrs('Channel Message', decolor_cb, 'Channel Message')
