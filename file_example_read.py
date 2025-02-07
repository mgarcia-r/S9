fp=open("text.txt","r")
print(fp.read())
fp.close()

#more pythonic
with open("text.txt", "r") as fp: #this creates a context
    print(fp.read())
print("we are done, the context closed by the index")

#read from file line by line
with open("text.txt","r") as fp:
    line_number=1
    for line in fp:
        #print(line, end="")#the end to not have space between each line
        print(f"{line_number}:{line.rstrip()}") #f string introduces value of line number in the string
        line_number+=1 #increments