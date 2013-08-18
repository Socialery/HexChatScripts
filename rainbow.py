import xchat
__module_name__ = "Rainbow"
__module_version__ = "1"
__module_description__ = "Rainbow command"

#Globals
r=0
colorf='\003%02d'

#Callbacks
def rainbow_cb(word, eol, userdata):
	if len(word)<2:
		print("Rainbow: Need a message")
	else:
		global r
		inp = enumerate(eol[1],r)
		f = lambda x: (colorf%((x[0])%14+2))+str(x[1])
		out = ''.join(map(f,inp))
		r = (r+1)%14
		xchat.command("SAY "+out)
	return xchat.EAT_XCHAT

#Hooks
xchat.hook_command("RAINBOW", rainbow_cb, help="/RAINBOW <message> Rainbowfies text")



