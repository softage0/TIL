from pywinauto import application
from pywinauto import timings
import time
import os
import strings

app = application.Application()
app.start("C:/KiwoomFlash3/Bin/NKMiniStarter.exe")

title = "번개3 Login"
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title=title))

pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys(__env__.p)

cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys(__env__.c)

btn_ctrl = dlg.Button0
btn_ctrl.Click()

time.sleep(300)
os.system("taskkill /im nkmini.exe")
