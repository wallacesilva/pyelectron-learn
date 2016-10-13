import gtk, webkit
import thread
import utils

class BrowserWindow():

	def __init__(self, options):

		self.options_default = {
			'width': 800,
			'height': 600,
			'x': 0,
		    'y': 0,
		    'position': "center",
			'minWidth': 0,
			'minHeight': 0,
			'maxWidth': 0,
			'maxHeight': 0,
		    'topLevel': True,
		    'resizable': True,
		    'movable': True,
		    'minimizable': True,
		    'maximizable': True,
		    'closable': True,
		    'focusable': True,
		    'alwaysOnTop': False,
		    'fullscreen': False,
		    'title': '',
		    'icon': None,
		    'show': True,
		    'modal': False,
		    'backgroundColor': '#ffffff',
		    'darkTheme': False,
		    'transparent': False,
		    'webPreferences': {
		    	'devTools': False,
		    	'preload': None,
		    	'javascript': True,
		    	'images': True,
		    	'webgl': True,
		    	'webaudio': True
		    }
		}

		self.options = options
		self.options.update(self.options_default)

		self.start(self.options)

	def start(self, options):

		# Create a GtkMain
		self.win = gtk.Window(type=gtk.WINDOW_TOPLEVEL)
		self.win.connect('destroy', lambda w: gtk.main_quit())

		options.width = 800 if options.width < 1 else options.width
		options.height = 600 if options.height < 1 else options.height

		if hasattr(options, 'show') == False:
			options.show = True
		
		self.win.resize(options.width, options.height)

		self._set_position(options.position)

		# self.win.set_title(app.name)

		self.win.set_keep_above(options.alwaysOnTop)
		self.win.set_resizable(options.resizable)
		
		if type(options.icon) == str:
			self.win.set_icon_from_file(options.icon)

		if options.fullscreen:
			self.win.fullscreen()

		self.scroller = gtk.ScrolledWindow()
		self.web = webkit.WebView()

		self.win.add(self.scroller)
		self.scroller.add(self.web)

		self.win.show_all()


		# start gtk on new thread
		#gtk.gdk.threads_init()
		#thread.start_new_thread(gtk.main, ())
		#gtk.main()

	def _set_position(self, pos):

		if pos == 'center':
			position = gtk.WIN_POS_CENTER
		elif pos == 'mouse':
		  	position = gtk.WIN_POS_MOUSE
		elif pos == 'center_always':
		  	position = gtk.WIN_POS_CENTER_ALWAYS
		elif pos == 'center_on_parent':
		  	position = gtk.WIN_POS_CENTER_ON_PARENT
		else:
		  	position = gtk.WIN_POS_NONE
		
		self.win.set_position(position)

	def openUrl(self, url):
		self.web.open(url)

	def openUri(self, uri):
		self.web.load_uri("file:///{}/".format(os.path.dirname(os.path.realpath(__file__))) + uri)

	def reload(self):
		self.web.reload()

	def maximize(self):
		self.win.maximize()

	def minimize(self):
		self.win.iconify()