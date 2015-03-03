import xchat
import re
import json

__module_name__ = "SpecifyColor"
__module_author__ = "RubyPinch"
__module_version__ = "1"
__module_description__ = ("Specifies nick colors")
# Partially based on tingping's wordhilight and alias


#Settings!
trigger_for=[
    'Channel Message',
    'Channel Action',
]
setting_prefix="specifycolor_"


#load settings
users = dict()
for pref in xchat.list_pluginpref():
    if pref.startswith(setting_prefix):
        name = pref[len(setting_prefix):]
        users[name] = xchat.get_pluginpref(setting_prefix+name)


# remove ^K, ^K##, ^K##,##
stripper=re.compile(r'^\003(\d\d?(,\d\d?)?)?')

edited = False
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
        users[word[1].lower()] = int(word[2])
    except (IndexError,ValueError):
        print("/setcolor <nick> <number>")
        return xchat.EAT_XCHAT
    print("*\tColor has been set for \003{:02}{}".format(users[word[1].lower()],word[1]))
    if not xchat.set_pluginpref(
      setting_prefix + word[1].lower(), #Name
      int(word[2]), #Color
      ):
        print("SpecifyColor: Setting could not be saved!")
    return xchat.EAT_XCHAT

for x in trigger_for:
    xchat.hook_print_attrs(x, decolor_cb, x)

xchat.hook_command('SETCOLOR', setcolor_cb, help="/setcolor <nick> <number>")
