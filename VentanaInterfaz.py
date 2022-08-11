import wx

class DemoMenu(wx.Frame):
    def __init__(self,parent,title):
        super(DemoMenu,self).__init__(parent,title=title)
        self.InitUI()
    def InitUI(self):
            menubar = wx.MenuBar()
            fileMenu = wx.Menu()

            fileItem = fileMenu.Append(wx.ID_EXIT,'Salir')
            menubar.Append(fileMenu, '&Archivo')
            self.SetMenuBar(menubar)
            self.Bind(wx.EVT_MENU,self.OnQuit,fileItem)
            self.Show(True)

    def OnQuit(self,e):
            self.Close()

frame = wx.App()
DemoMenu(None, 'Word')
frame.MainLoop()

