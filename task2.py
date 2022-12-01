import subprocess


f1 = open ('TaskPython.cpp' , 'w+')
f1.write ("#include <iostream>\nint main ()\n{\n")

x = input ("please Enter your words: ")

f1.write ("std :: cout <<\"" + x)
f1.write ("\";\n}\n")
f1.close ()



print ("created by: Esraa Alqassas: ");
subprocess.call (["g++", "TaskPython.cpp"], shell= True)
subprocess.call ("a", shell = True);
print ("\n\nmission completed successfully")






