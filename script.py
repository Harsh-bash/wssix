import sys

# file route
admin = "admin\static\js\main.4e383c73.js"
client = "client\index.html"

# check argument
try:
    api = sys.argv[1]
except:
    print("Enter your apikey after file name!!")
    exit()

# values
c = "https://yourapikey"
r = api

# main function
f = open(admin, "r")
text = f.read()
text = text.replace(c, r)
f.close()
f = open(admin, "w")
f.write(text)
f.close()

s = open(client, "r")
value = s.read()
value = value.replace(c, r)
s.close()
s = open(client, "w")
s.write(value)
s.close()
print("Your Files are readey now !!!")
