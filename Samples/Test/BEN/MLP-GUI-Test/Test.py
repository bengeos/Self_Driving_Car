import wx
import serial as sp

class Test(wx.Frame):
    def __init__(self):
        self.Port = sp.Serial('COM1',9600)
        wx.Frame.__init__(self,None,wx.ID_ANY,"BENGEOS")
        panel = wx.Panel(self,wx.ID_ANY)
        btn = wx.Button(panel,label="OK")
        btn.Bind(wx.EVT_KEY_DOWN,self.OnKeyPressed)
        btn.Bind(wx.EVT_KEY_UP,self.OnKeyReLeased)
    def ben(self,evt):
        print('bemgeos')
        evt.Skip()
    def OnKeyPressed(self,event):
        keyCode = event.GetKeyCode()
        print(keyCode)
        if(keyCode == 73):
            self.Port.write('I\r\n')
        if(keyCode == 79):
            self.Port.write('O\r\n')
        if(keyCode == 80):
            self.Port.write('P\r\n')
        if(keyCode == 76):
            self.Port.write('L\r\n')
        if(keyCode == 77):
            self.Port.write('M\r\n')
    def OnKeyReLeased(self,event):
        keyCode = event.GetKeyCode()
        self.Port.write('M\r\n')


app = wx.PySimpleApp()
frame = Test()
frame.Show()
app.MainLoop()