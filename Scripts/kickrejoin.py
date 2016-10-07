import xchat
__module_name__ = "KickRejoin"
__module_version__ = "1"
__module_description__ = "Joins channels that you are kicked from."

#Callbacks
def kick_cb(word, eol, userdata):
	if xchat.nickcmp(word[3], xchat.get_info('nick')) == 0:
		xchat.command("JOIN "+word[2])

#Hooks
xchat.hook_server("KICK", kick_cb)
