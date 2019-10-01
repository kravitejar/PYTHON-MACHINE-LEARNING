
##### Create the file in 'write' mode
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "w")
##
### Write some text to the file
##f.write("Hello World! Hi")
##
### Close the file
##f.close()




### Open the file in 'read' mode
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##
### Put the contents of the file into a variable
##f_contents = f.read()
##
### Close the file
##f.close()
##
### Print the file's contents
##print(f_contents)




### Read the original file and print
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##f_contents = f.read()
##print("Original content:", f_contents)
##f.close()
##
### Update the file
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "w")
##f_contents = "Hey there Everyone!"
##f.write(f_contents)
##f.close()
##
### Read the updated file and print
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##f_contents = f.read()
##print("Updated content:", f_contents)
##f.close()







### Read the original file and print
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##f_contents = f.read()
##print("Original content:", f_contents)
##f.close()
##
### Update the file
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "a")
##f_contents = "\n " + "Hey there Uranus!"
##f.write(f_contents)
##f.close()
##
### Read the updated file and print
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##f_contents = f.read()
##print("Updated content:", f_contents)
##f.close()






###Read a portion of the file
##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##f_contents = f.read(5)
##print(f_contents)
##f.close()





##f = open(r"C:\Users\JOHN\Desktop\python.txt", "r")
##line1 = f.readline()
##line2 = f.readline()
##print("Line 1:", line1)
##print("Line 2:", line2)
##f.close()
