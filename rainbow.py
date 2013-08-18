import xchat
__module_name__ = "Rainbow"
__module_version__ = "1.1"
__module_description__ = "Rainbow command"

#Globals
r=0
d=+1
#Callbacks
def rainbow_cb(word, eol, userdata):
	if len(word)<2:
		print("Rainbow: Need a message")
	else:
		global r
		r = (r+d)%14
		inp = enumerate(eol[1],r)
		f = lambda x: '\003%02d'%(x[0]%14+2) + x[1]
		out = ''.join(map(f,inp))
		xchat.command("SAY "+out)
	return xchat.EAT_XCHAT

def rainbowflip_cb(word, eol, userdata):
	global d
	d = -d
	return xchat.EAT_XCHAT

#Hooks
xchat.hook_command("RAINBOW", rainbow_cb, help="/RAINBOW <message> Rainbowfies text")
xchat.hook_command("RAINBOWFLIP", rainbowflip_cb, help="/RAINBOWFLIP reverses the rainbowing rotation direction")


