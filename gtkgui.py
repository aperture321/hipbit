#!/usr/bin/python
from gi.repository import Gtk
import pyex

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
