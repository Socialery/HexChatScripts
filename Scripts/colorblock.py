import xchat
import re

__module_name__ = "ColorBlock"
__module_author__ = "Socialery"
__module_version__ = "2"
__module_description__ = ("disables unimaginatively colored lines")

rm_color_regex = re.compile(r'''\x03          # Color
                                (?:\d{,2})    # Foreground
                                (?:,\d{1,2})? # Background
                             ''', re.X)
rm_color = lambda x: rm_color_regex.sub('', x, 1)


def decolor_cb(word, word_eol, userdata, attributes):
    # Fast ignore any irrelevant lines, also ignores any messages we emit
    if not (word[1].startswith('\x03') and word[1].count('\x03') == 1):
        return
    # Emit the new line
    xchat.emit_print(userdata, word[0], rm_color(word[1]), *word[2:])
    # And eat all, so other plugins don't get double lines
    return xchat.EAT_ALL


for event in ['Channel Message', 'Channel Action']:
    xchat.hook_print_attrs(event, decolor_cb, event)