#program to copy the contents of a file
if __name__=="__main__":
    with open("test.txt",'r') as rf:
        with open("test_copy.txt","w") as wf:
            for line in rf.read():
                wf.write(line)
    """read a file using file.read() method"""
    with open("test_copy.txt","r") as rf:
        print(rf.read())
    """read a file using file.readlines() method"""
    with open("test_copy.txt","r") as rf:
        for line in rf.readlines():
            print(line,end="")
        print()
    """read a file using file.readline() method"""
    with open("test_copy.txt","r") as rf:
        line=rf.readline()
        while len(line)>0:
            print(line,end="")
            line=rf.readline()
