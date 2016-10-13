#!/usr/bin/env python

import sys
import gtk, webkit
import thread 
import utils
import pprint
from browserwindow import BrowserWindow

# check python version
if sys.version_info < (2,6):
	sys.exit("Required python version 2.6")

app = utils.getJsonFromFile('./package.json')

win = BrowserWindow(app.window)

win.win.set_title(app.name)

#win.openUrl('file:///index.html') #app.main_url
win.openUri('index.html') 

gtk.main()

#sys.exit()


# app = {
# 	'name': 'Electron Aplication'
# }

"""
winOptions = {
	'width': 1080,
  'minWidth': 680,
  'height': 840,
  'isTopLevel': gtk.WINDOW_TOPLEVEL if app.isTopLevel else None, 
  'isFullscreen': False,
  'isResizable': False,
  'position': 'center',
	'title': app.name
} ""

winOptions = app.window
# winOptions.isTopLevel = gtk.WINDOW_TOPLEVEL if app.isTopLevel else None

# win = gtk.Window(type=winOptions.isTopLevel)
win = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
win.connect('destroy', lambda w: gtk.main_quit())

win.set_title(app.name)

if winOptions.position == 'center':
  position = gtk.WIN_POS_CENTER
elif winOptions.position == 'mouse':
  position = gtk.WIN_POS_MOUSE
elif winOptions.position == 'center_always':
  position = gtk.WIN_POS_CENTER_ALWAYS
elif winOptions.position == 'center_on_parent':
  position = gtk.WIN_POS_CENTER_ON_PARENT
else:
  position = gtk.WIN_POS_NONE

win.set_position(position)
win.set_resizable(winOptions.isResizable)
win.set_icon_from_file(winOptions.icon)
win.resize(winOptions.width, winOptions.height)

if winOptions.isFullscreen:
  win.fullscreen()

def _key_pressed(self, widget, event):
  modifiers = gtk.accelerator_get_default_mod_mask()
  mapping = {
    gtk.gdk.KEY_r: web.reload(),
    # gtk.gdk.KEY_w: self._close_current_tab,
    # gtk.gdk.KEY_t: self._open_new_tab,
    # gtk.gdk.KEY_l: self._focus_url_bar,
    # gtk.gdk.KEY_f: self._raise_find_dialog,
    gtk.gdk.KEY_q: gtk.main_quit
  }

  if event.state & modifiers == gtk.gdk.ModifierType.CONTROL_MASK \
    and event.keyval in mapping:
      mapping[event.keyval]()  

# win.connect("key-press-event", _key_pressed)

scroller = gtk.ScrolledWindow()
web = webkit.WebView()

web.open("http://localhost:9000/")

# web.reload()

win.add(scroller)
scroller.add(web)

win.show_all()

gtk.gdk.threads_init()
thread.start_new_thread(gtk.main, ())

# gtk.main()


""" 
"""
import sys

from gi.repository import Gtk, Gdk, WebKit

class MainWindow(Gtk.Window):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.set_size_request(400,400)

        # connect signals
        self.connect("destroy", Gtk.main_quit)
        self.connect("key-press-event", self._key_pressed)

    def _key_pressed(self, widget, event):
        modifiers = Gtk.accelerator_get_default_mod_mask()
        mapping = {Gdk.KEY_r: self._reload_tab,
                   Gdk.KEY_w: self._close_current_tab,
                   Gdk.KEY_t: self._open_new_tab,
                   Gdk.KEY_l: self._focus_url_bar,
                   Gdk.KEY_f: self._raise_find_dialog,
                   Gdk.KEY_q: Gtk.main_quit}

        if event.state & modifiers == Gdk.ModifierType.CONTROL_MASK \
          and event.keyval in mapping:
            mapping[event.keyval]()

if __name__ == "__main__":
    Gtk.init(sys.argv)

    mainWindow = MainWindow()

Gtk.main()
"""