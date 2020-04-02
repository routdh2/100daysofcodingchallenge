#program to copy the contents of a large file in small chunk size
if __name__=="__main__":
    with open("test.txt","r") as rf:
        with open("test_copy.txt","w") as wf:
            chunk_size=200 #chunk size of 200 chars
            content=rf.read(chunk_size)
            while len(content)>0: #read till you reach EOF
                wf.write(content)
                wf.write("*") #just to be sure that it copies in chunks
                content=rf.read(chunk_size)
    '''output the content one line at a time instead of printing whole content,
    as there is a possibility of memory being full'''
    with open("test_copy.txt","r") as rf:
        for line in rf:
            print(line,end='')