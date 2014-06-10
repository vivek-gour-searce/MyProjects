import telnetlib

user = "IAHUVLG"#raw_input("Enter your User Name: ")
password = "WELCOME1"#raw_input("Enter your Password: ")

tn = telnetlib.Telnet("10.235.108.20")
tn.set_debuglevel(10)
tn.write(user + "\t")
tn.read_until("Welcome",3)
print 'User ID entered'
if password:
    tn.read_until("PSWD.: ",1)
    tn.write(password + "\n")
print 'Password entered'

res = tn.read_until("ZCZX",3)
print res
tn.close()