import gtk
import gtk.glade
import pyex

class hello:
	def __init__(self):
		self.gladefile = "gtkapp.glade"
		self.wTree = gtk.glade.XML(self.gladefile)
		
		self.window = self.wTree.get_widget("MainWindow")
		dic = {"on_b1_clicked": self.b1_test ,
               "on_b2_clicked": gtk.main_quit }
		if (self.window):
			self.window.connect("destroy", gtk.main_quit)

		self.wTree.signal_autoconnect(dic)
		self.window.show_all()

	def b1_test(self, widget):
		pyex.testsuite()


a = hello()
gtk.main()
