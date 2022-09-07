import wx

class Observable:
    def __init__(self, initalValue=None):
        self.data = initalValue
        self.callbacks = {}

    def addCallback(self, func):
        self.callbacks[func] = 1

    def delCallback(self, func):
        del self.callback[func]
    
    def _docallbacks(self):
        for func in self.callbacks:
            func(self.data)

    def set(self, data):
        self.data = data
        self._docallbacks()

    def get(self):
        return self.data

    def unset(self):
        self.data = None

class Model: # Clase Modelo: Hará referencia a los datos representados asi como los métodos
    def __init__(self):
        self.myMoney = Observable(0)

    def addMoney(self, value):
        self.myMoney.set(self.myMoney.get() + value)

    def removeMoney(self, value):
        self.myMoney.set(self.myMoney.get() - value)

class View(wx.Frame): # Clase Vista para la interfaz de la aplicación por donde se moverá el usuario
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Vista principal")
        sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self, label="Mi dinero")
        ctrl = wx.TextCtrl(self)
        sizer.Add(text, 0, wx.EXPAND | wx.ALL)
        sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL)
        ctrl.SetEditable(False)
        self.SetSizer(sizer)
        self.moneyCtrl = ctrl

    def SetMoney(self, money):
        self.moneyCtrl.SetValue(str(money))

class ChangeWidget(wx.Frame): # Clase ChangeWidget presentará una vista con las funciones de la app
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="Vista principal")
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.add = wx.Button(self, label="Añadir dinero")
        self.remove = wx.Button(self, label="Quitar dinero")
        sizer.Add(self.add, 0, wx.EXPAND | wx.ALL)
        sizer.Add(self.remove, 0, wx.EXPAND | wx.ALL)
        self.SetSizer(sizer)

class Controller: # Clase controlador tendrá los métodos con los que el usuario podrá actuar en la app
    def __init__(self, app):
        self.model = Model()
        self.view1 = View(None)
        self.view2 = ChangeWidget(self.view1)
        self.MoneyChanged(self.model.myMoney.get())
        self.view2.add.Bind(wx.EVT_BUTTON, self.AddMoney)
        self.view2.remove.Bind(wx.EVT_BUTTON, self.RemoveMoney)
        self.model.myMoney.addCallback(self.MoneyChanged)
        self.view1.Show()
        self.view2.Show()

    def AddMoney(self, evt):
        self.model.addMoney(10)
    
    def RemoveMoney(self, evt):
        self.model.removeMoney(10)
    
    def MoneyChanged(self, money):
        self.view1.SetMoney(money)

app = wx.App(False)
controller = Controller(app)
app.MainLoop()
