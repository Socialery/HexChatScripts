import xchat
__module_name__ = "InviteJoin"
__module_version__ = "1"
__module_description__ = "Joins channels that you are invited to."

#Callbacks
def invite_cb(word, eol, userdata):
	xchat.command("QUOTE JOIN "+word[3])

#Hooks
xchat.hook_server("INVITE", invite_cb)
