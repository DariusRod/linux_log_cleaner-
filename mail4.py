import win32com.client as win32
from datetime import datetime
import os


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.Subject = 'Log remover' + datetime.now().strftime('%#d %b %Y %H:%M')
mail.To = "test@gmail.com"
attachment = mail.Attachments.Add(os.getcwd() + "\\apl1.txt")
# attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "currency_img")
mail.HTMLBody = r"""
Hello all,<br><br>
The highlighted of youuuu currencies exchange prices is as follow:<br><br>
<img src="cid:currency_img"><br><br>
For more details, you can check the table in the Excel file attached.<br><br>
,<br>

"""
mail.Attachments.Add(os.getcwd() + "\\apl1.txt")
mail.Send()