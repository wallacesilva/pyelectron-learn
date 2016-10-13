import sys
import os 

from gi.repository import Gtk, Gdk, WebKit

class Browser(Gtk.Window):
    def __init__(self, *args, **kwargs):
        super(Browser, self).__init__(*args, **kwargs)
        
        self.connect("destroy", Gtk.main_quit)
        self.set_size_request(800,600)
        
        self.webview = WebKit.WebView()
        self.webview.load_uri("file:///{}/index.html".format(os.path.dirname(os.path.realpath(__file__))))
        
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        self.add(scrolled_window)
        scrolled_window.show_all()
        
        self.show()

class Inspector(Gtk.Window):
    def __init__(self, view, *args, **kwargs):
        super(Inspector, self).__init__(*args, **kwargs)
        
        self.set_size_request(800,600)
        self.webview = view
        
        settings = WebKit.WebSettings()   
        settings.set_property('enable-developer-extras', True)
        view.set_settings(settings)

        self.webview = WebKit.WebView()
        self.inspector = view.get_inspector()
        
        self.inspector.connect("inspect-web-view", self.inspect)
        
        self.scrolled_window = Gtk.ScrolledWindow()
        self.add(self.scrolled_window)
        self.scrolled_window.show()

        self.webview = WebKit.WebView()
        self.scrolled_window.add(self.webview)

    def inspect(self,inspector,view,*a,**kw):
        self.scrolled_window.show_all()
        self.show()
        return self.webview
            
if __name__ == "__main__":
    Gtk.init(sys.argv)
    browser = Browser()
    inspector = Inspector(browser.webview)

    Gtk.main()