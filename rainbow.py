import xchat
__module_name__ = "Rainbow"
__module_version__ = "1"
__module_description__ = "Rainbow command"

#Globals
r=0

#Callbacks
def rainbow_cb(word, eol, userdata):
	if len(word)<2:
		print("Rainbow: Need a message")
	else:
		global r
		in=eol[1]
		# could use a map for the following? yes, yes I could, noted.
		color=lambda a,b:'\003%02d'%((a+b)%14+2) #\003 folowed by 02-15 I think?
		out=[color(r,n)+in[n] for n in range(len(in))] #then append that to each char
		out=''.join(out) #and concat
		r=(r+1)%14 #then rotate the initial color
		xchat.command("SAY "+out)
	return xchat.EAT_XCHAT

#Hooks
xchat.hook_command("RAINBOW", rainbow_cb, help="/RAINBOW <message> Rainbowfies text")



