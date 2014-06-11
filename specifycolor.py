import xchat
import re
import json

__module_name__ = "SpecifyColor"
__module_author__ = "RubyPinch"
__module_version__ = "1"
__module_description__ = ("Specifies nick colors")
# Partially based on tingping's wordhilight



#Settings!
trigger_for=[
    'Channel Message',
    'Channel Action',
]



#load settings
users = xchat.get_pluginpref("SpecColor_users")
users = {} if users is None else json.loads(users)




edited = False
# remove ^K, ^K##, ^K##,##
stripper=re.compile(r'^\003(\d\d?(,\d\d?)?)?')

def decolor_cb(word, word_eol, event, attr):
    global edited
    nick = stripper.sub('',word[0])
    #Ignore our own events, empty messages, and
    # other things that don't concern us
    #note: nickcmp should probably be used, but I want to stay sane
    #and might not work in python2
    if edited or not len(word)>1 or nick.lower() not in users.keys():
        return
    edited = True
    xchat.emit_print(event,"\003{:02}{}".format(users[nick.lower()],nick),word[1],*word[2:])
    edited = False
    return xchat.EAT_ALL



def setcolor_cb(word,word_eol,userdata):
    global users

    try:
        users[word[1].lower()]=int(word[2])
    except (IndexError,ValueError):
        print("/setcolor <nick> <number>")
        return xchat.EAT_XCHAT
    if not xchat.set_pluginpref(
      "SpecColor_users",
      json.dumps(users,separators=(',',':'))):
        print("SpecifyColor: Setting could not be saved!")
    return xchat.EAT_XCHAT

for x in trigger_for:
    xchat.hook_print_attrs(x, decolor_cb, x)

xchat.hook_command('SETCOLOR', setcolor_cb, help="/setcolor <nick> <number>")
