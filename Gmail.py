import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("nabilatarannum2023@gmail.com", "Jkwpsr@#")
server.sendmail(
    "nabilatarannum2023@gmail.com",
    ["stmollik2020@gmail.com", "shamillabdullah2250@gmail.com"],
    "Hi Samiha Tabassum & Shamil Abdullah , it's just a test.",
)
