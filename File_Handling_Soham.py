'''
1. WAP to find the number of words in the given text file
Hints:Use the split() method to separate words.
'''
with open("./myfile.txt","r") as f:
    file=f.read()
    print(file)
    words=file.split()
    wordcount=len(words)
    print('The word count of the file is:',wordcount)


'''2. Write a program to write “Happy Programming” in a text file and read it'''
with open("./question2.txt","r") as fi:
    filee=fi.read()
    print(filee)


'''
3. WAP to demonstrate the working of the following functions:
    i) read()
    ii) read(n)
    iii) readline()
    iv) readlines()
'''
with open("./myfile.txt","r") as f:
    print(f.read())
    f.seek(0)
    print(f.read(10))
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())


'''
4. WAP that exhibits the working of the following functions:
    i. write()
    ii. writelines()
'''
with open("./newfile.txt","w") as w:
    line="This is my new file.\n"
    lines=["Hello Sir\n","How was Diwali?\n","Belated Happy Diwali"]
    w.write(line)
    w.writelines(lines)


'''5. Write a Python program to read first n lines of a file.'''
with open("./myfile.txt","r") as f:
    count=int(input("Enter the number of line you want to read: "))
    while count>=1:
        line=f.readline()
        count-=1
        if line:
            print(line,end='')
        else:
            break


'''6. Write a Python program to append text to a file and display the text.'''
with open("./append.txt","a") as a:
    a.write('And hello again, this is append.\n')
with open("./append.txt","r") as r:
    print(r.read())


'''7. Write a Python program to read last n lines of a file.'''
with open("./myfile.txt","r") as f:
    count=int(input("Enter the number of line you want to read from last: "))
    lines=f.readlines()
    last_line=lines[-count:]
    for i in last_line:
        print(i,end='')

'''8. Write a Python program to read a file line by line and store it into a list.'''
with open("./myfile.txt",'r') as file:
    lines_list = []
    for line in file:
        lines_list.append(line.strip())
print("\nLines stored in the list:")
print(lines_list)