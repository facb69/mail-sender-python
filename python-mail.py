#!/usr/bin/env python3.8

import subprocess
import os
import sys
import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# IF YOU WANT THIS SCRIPT TO BE STATIC FILL IN WITH THE INFO YOU NEED
#sender_email = "senderemail@domain.com"
#password = "yourpassword"
#receiver_email = "receiveremail@anohterdomain.com"

# IF YOU WANT THIS SCRIPT NOT TO BE STATIC PASS THE INFO AS PARAMETERS
sender_email = sys.argv[1]
password = sys.argv[2]
receiver_email = sys.argv[3]

message = MIMEMultipart("alternative")
message["Subject"] = "WHATEVER YOU WANT"
message["From"] = sender_email
message["To"] = receiver_email

# THIS PART IS RANDOM - I USED A WAY TO GET MY DISK USAGE AND SEND IT WITHIN THE HTML BODY AS VARIABLES
# IT WILL WORK ON A LINUX ENVIRONMENT
total, used, free = shutil.disk_usage("/")
disktotal = "%d GB" % (total // (2**30))
diskused = "%d GB" % (used // (2**30))

# THIS IS THE HTML/CSS PART - DO IT AS YOU PLEASE
html = """\
<html>
  <body>
<div style="margin: 20px;">
<a style='text-decoration: none;' title='FACB69' href='https://facb69.com.br' target='_blank'>
	<img src='https://facb69.com.br/logo.png' alt='' />
</a>
<h4 style="font-size:13px;font-style:italic;">"PYTHON SENDING MAIL"</h4>
<p>
<span style='letter-spacing: 3px;color:#666;'>Disk Usage of FACB69 Server</span>
<br/>
<table style='width:300px;margin:0;padding:0;font-size:11px;border:1px solid #CECECE;border-radius:2px;box-shadow: 1px 1px 0px 0px #666;'>
<tr>
<th style='margin:0;padding:0;text-align:center;border-bottom: 1px solid #CECECE;border-right: 1px solid #CECECE;'>SIZE</th>
<th style='margin:0;padding:0;text-align:center;border-bottom: 1px solid #CECECE;border-right: 1px solid #CECECE;'>USE</th>
<th style='margin:0;padding:0;text-align:center;border-bottom: 1px solid #CECECE;'>MOUNTED ON</th>
</tr>

<tr>
<td style='margin:0;padding:0;text-align:center;border-bottom:1px solid #CECECE;border-right: 1px solid #CECECE;'>""" + disktotal + """</td>
<td style='margin:0;padding:0;text-align:center;border-bottom:1px solid #CECECE;border-right: 1px solid #CECECE;'>""" + diskused + """</td>
<td style='margin:0;padding:0;text-align:center;border-bottom:1px solid #CECECE;'>/</td>
</tr>

</table>
</p></div>
  </body>
</html>
"""

# WE NEED TO TURN THE VARIABLE INTO MIMEText OBJECT
part = MIMEText(html, "html")

# NOW WE ATTACH THE VARIABLE PART SO THE MAIL CLIENT CAN UNDERSTAND IT
message.attach(part)

# HERE WE PUT THE MAIL SERVER CREDENTIALS
server = smtplib.SMTP(host='mail.yourdomain.com', port=xxx)
server.ehlo()
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()

# WE ARE DONE
