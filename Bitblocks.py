#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.5 on Sun Oct 20 16:11:10 2013

import wx
import pyex
import login_frame #for login menubar window
import check_delete #for deleting objects
import os
# begin wxGlade: extracode
# end wxGlade


'''
Will hold menubar information for the class
'''
class MyMenuBar3(wx.MenuBar):

    def logger(self, event):  # wxGlade: MyMenuBar3.<event_handler>
        print "Event handler `logger' not implemented!"
        event.Skip()

# end of class MyMenuBar3

class NewWindow(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, id, 'New Window', size=(400,300))
        wx.Frame.CenterOnScreen(self)
        #self.new.Show(False)

class MainConsole(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainConsole.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        bg_img='cloudlayer.png' #background to use for the program
        self.bg = wx.Bitmap(bg_img)
        self._width, self._height = self.bg.GetSize()
        self.TitleGreet = wx.StaticText(self, -1, "Pick your MP3 folder!", style=wx.ALIGN_CENTRE)
        self.filestatus = wx.StaticText(self, -1, "________________________")
        self.browse_button = wx.Button(self, wx.ID_OPEN, "")
        self.button_1 = wx.Button(self, -1, "Scan and Refresh\nDatabase")
        self.datareset = wx.Button(self, -1, "Reset\nDatabase")
        self.Statusbar = wx.StaticText(self, -1, "Hope you enjoy!", style=wx.ALIGN_CENTRE)
        self.new = login_frame.my_login_frame(parent=None, id=-1)

        
        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        self.file_bar = wx.Menu()
        self.login_bar = wx.MenuItem(self.file_bar, wx.NewId(), "Login", "Enter login information", wx.ITEM_NORMAL)
        self.file_bar.AppendItem(self.login_bar)
        self.frame_1_menubar.Append(self.file_bar, "File")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.browsing, self.browse_button)
        self.Bind(wx.EVT_BUTTON, self.scan_start, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.reset_window, self.datareset)
        self.Bind(wx.EVT_MENU, self.logger, self.login_bar)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        # end wxGlade

        self.path_dir = "________________________" #path directory initializer
        self.menubar = MyMenuBar3()


    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        self.Draw(dc)

    '''
    Function which redraws the background as the window is resized.
    '''
    def Draw(self, dc):
        cliWidth, cliHeight = self.GetClientSize()
        if not cliWidth or not cliHeight:
            return
        dc.Clear()
        xPos = (cliWidth - self._width)/2
        yPos = (cliHeight - self._height)/2
        dc.DrawBitmap(self.bg, xPos, yPos)

    def scan_start(self, event):
        if(self.config_exists()):
            #self.deleter = check_delete.check_del(parent=None, id=-1)
            #self.deleter.Show()
            pass
        #TODO start scanning
        pyex.realtest(self.path_dir)
        self.Statusbar.SetLabel("Done")

    def reset_window(self, event):
        if(self.config_exists()):
            self.deleter = check_delete.check_del(parent=None, id=-1)
            self.deleter.Show()
        if(os.path.isfile(open("config.cfg", "r").readline().rstrip() + ".db")):
            pass
        else:
            self.Statusbar.SetLabel("Database wiped.")

    def __set_properties(self):
        # begin wxGlade: MainConsole.__set_properties
        self.SetTitle("Hip Bit")
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("folder_music.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetSize((210, 148))
        self.TitleGreet.SetMinSize((127, 17))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainConsole.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.TitleGreet, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.filestatus, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.browse_button, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.datareset, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_2.Add(self.Statusbar, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def browsing(self, event):  # wxGlade: MainConsole.<event_handler>
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            self.path_dir = dlg.GetPath() 
            if (len(self.path_dir) > 15):  #Allows so there's no dynamic size constraints
                self.filestatus.SetLabel(self.path_dir[0:15] + "...")
            else:
                self.filestatus.SetLabel(self.path_dir)
        dlg.Destroy()
        event.Skip()

    def config_exists(self):
        try:
            open("config.cfg","r")
            return 1
        except:
            self.Statusbar.SetLabel("Error. No login info.")
            return 0

    def logger(self, event):  #login frame appears to store login data.
        self.new = login_frame.my_login_frame(parent=None, id=-1) #required for reinitializing multiple exits
        self.new.Show(True)
        event.Skip()

''''''#self.filestatus.SetLabel(self.new.get_text())
# end of class MainConsole
class UserGui(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame_1 = MainConsole(None, -1, "")
        self.SetTopWindow(frame_1)
        frame_1.Show()
        if(not frame_1.config_exists()): #For initial login checking.
            frame_1.new.SetFocus()
            frame_1.new.Raise()
            frame_1.new.Show(True)
        return 1

# end of class UserGui

if __name__ == "__main__":
    app = UserGui(0)
    app.MainLoop()
