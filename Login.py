import wx

class MyFrame(wx.Frame):
    

    def __init__(self):
        wx.Frame.__init__(self, None, title="Login")
        panel = wx.Panel(self)
        self.count = 0

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)

        usernameLbl = wx.StaticText(panel, label="Usuario:")
        self.username = ex.TextCtrl(panel)
        self.addWidgets(usernameLbl, self.username)

        pwLbl = wx.StaticText(panel, label="Contraseña:")
        self.pw = wx.TextCtrl(panel)
        self.addWidgets(pwLbl, self.pw)

        btn = wx.Button(panel, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.onClick)
        self.mainSizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)

        panel.SetSizer(self.mainSizer)
        self.Show()

    def addWidgets(self, lbl, txt):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(lbl, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(txt, 1, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(sizer, 0, wx.ALL|wx.EXPAND)

    def onClick(self, event):
        password = self.pw.GetValue()
        user = self.username.GetValue()

        if user!= "alumno" and password!="alumno":
            msg = "Te quedan %s intentos"%(str(3-self.count))
            dlg = wx.MessageDialog(self, msg, "", wx.OK)

        if user!="alumno" and password!="alumno":
            msg = "Te quedan %s intentos"%(str(3-self.count))
            dlg = wx.MessageDialog(self, msg, "", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

            self.count += 1
            password=self.username.GetValue()
            user=self.username.GetValue()
            if self.count == 3:
                self.Destroy()
        if user == "alumno" and password== "alumno":
                vn=VentanaNueva(None)
                vn.Show()

        class VentanaNueva(wx.Frame):
            def __init__(self,parent):
                wx.Frame.__init__(self, parent)
                panel = wx.Panel(self,-1)
                txt = wx.StaticText(panel, label="Estas dentro;;")


    if __name__ == "__main__":
        app = wx.App(False)
        frame = MyFrame()
        app.MainLoop()
                            
