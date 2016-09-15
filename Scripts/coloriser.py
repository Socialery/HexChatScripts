import xchat
from itertools import chain,cycle
__module_name__ = "Coloriser"
__module_version__ = "1.2"
__module_description__ = "Coloriser commands"

#Functions
def colorfactory(items):
	def colorise(message):
		return u''.join(
			chain(
				*zip(
					cycle(u'\003{:0>2}'.format(x) for x in items),
					message
				)
			)
		)
	return colorise


#Globals
colors={
	"rainbow":colorfactory(range(2,14)),
	"christmas":colorfactory([3,4]),
}

#Callbacks
def colorise_cb(word, eol, userdata):
	if len(word)<2:
		print("Rainbow: Need a message")
	else:
		xchat.command(("SAY "+userdata(eol[1])).encode('utf-8'))
	return xchat.EAT_XCHAT
#Hooks
for x in colors:
	print "/"+x.upper()+" hooked"
	xchat.hook_command(
		x.upper(),
		colorise_cb,
		userdata=colors[x]
	)
print 'Coloriser loaded'