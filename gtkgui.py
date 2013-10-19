#!/usr/bin/python
#from gi.repository import Gtk
import pyex


import gtk

class PyApp(gtk.Window):
	def __init__(self):
		super(PyApp, self).__init__()
		
		self.set_title("Hipbit Client")
		self.set_size_request(260,150)
		self.set_position(gtk.WIN_POS_CENTER)

		vbox = gtk.VBox(False, 5)
		hbox = gtk.HBox(True, 3)

		valign = gtk.Alignment(0,1,0,0)
		vbox.pack_start(valign)

		testb = gtk.Button("Test")
		ok.set_size_request(70,30)
		close = gtk.Button("Close")

		hbox.add(ok)
		hbox.add(close)
	
		halign = gtk.Alignment(1,0,0,0)
		halign.add(hbox)

		vbox.pack_start(halign, False, False, 3)

		self.add(vbox)

		self.connect("destroy", gtk.main_quit)
		self.show_all()

PyApp()
gtk.main()

"""
#TODO gtk2 compliant.

class MyWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="hipbit")
		
		self.box = Gtk.Box(spacing=6)
		self.add(self.box)
		
		self.button = Gtk.Button(label="Click to test!")
		self.button.connect("clicked", self.on_test_clicked)
		self.box.pack_start(self.button, True, True, 0)

		self.button = Gtk.Button(label="Exit.")
		self.button.connect("clicked", self.on_exit_click)
		self.box.pack_start(self.button, True, True, 0)

	def on_test_clicked(self, button):
		print("Performing tests..")
		pyex.testsuite()
	
	def on_exit_click(self, quit_button):
		Gtk.main_quit()

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
"""
