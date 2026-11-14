import smtplib
from email.message import EmailMessage



server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("nh30112010d@big.atid.org.il", "cvea vxaa pxaa rosp")
msg = EmailMessage()

msg["Subject"] = "joke"
msg["From"] = "nh30112010d@big.atid.org.il"
msg["To"] = "merrygeva312@gmail.com"
msg.set_content("הייתי מורה לחשבון איך היה? יש פלוסים ויש מינוסים")
server.send_message(msg)
server.quit()