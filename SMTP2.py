import smtplib
from email.message import EmailMessage



server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("nh30112010d@big.atid.org.il", "cvea vxaa pxaa rosp")
msg = EmailMessage()

msg["Subject"] = "joke"
msg["From"] = "nh30112010d@big.atid.org.il"
msg["To"] = "merrygeva312@gmail.com"

msg.set_content("joke in file ")
with open("joke.txt", "rb") as file:
    file_data = file.read()
(msg.add_attachment(file_data, maintype="text",subtype="plain",filename="joke.txt"))
server.send_message(msg)
server.quit()