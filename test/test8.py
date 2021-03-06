import wx
import wx.lib.inspection

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
    	wx.Frame.__init__(self, *args, **kwargs)

    	self.p1 = wx.Panel(self)
    	lst = ['1','2','3']
    	self.st = wx.ComboBox(self.p1, -1, choices = lst, style=wx.TE_PROCESS_ENTER)

    	self.st.Bind(wx.EVT_COMBOBOX, self.text_return)


    def text_return(self, event):
    	lst = ['3','4']
    	self.st = wx.ComboBox(self.p1, -1, choices = lst, style=wx.TE_PROCESS_ENTER)


class MyApp(wx.App):
    def OnInit(self):
    	frame = MyFrame(None, -1, '20_combobox.py')
    	frame.Show()
    	self.SetTopWindow(frame)
    	return 1

if __name__ == "__main__":
    app = MyApp(0)
#    wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()