import getpass
print("Please imput your Schoology credentials. Please note you will not see your password as you type it in!")
x = input("Enter Schoology Username : ")
y = open('SchoologyUsername.txt', 'w')
p = getpass.getpass("Enter Schoology Password : ")
w = open('SchoologyPassword.txt', 'w')
y.write(x)
w.write(p)