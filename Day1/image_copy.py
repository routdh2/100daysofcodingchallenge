#program to copy an image file
if __name__=="__main__":
    count=0
    with open("Dhananjay Rout.jpg","rb") as rf:
        with open("Dhananjay Rout_copy.jpg","wb") as wf:
            chunk_size=2000
            content=rf.read(chunk_size)
            while len(content)>0:
                wf.write(content)
                count+=1
                content=rf.read(chunk_size)
    # with open("Dhananjay Rout_copy.jpg","rb") as rf:
    #     for line in rf:
    #         print(line)
    print(count)