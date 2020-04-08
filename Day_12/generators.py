'''Program to understand generators in Python'''
if __name__=="__main__":
    def my_range(start,end):
        while start<end:
            # current=start
            yield start #this command generates the generator
            start+=1
    for i in my_range(1,10):
        print(i)
    gen_ob = my_range(1,10)
    print(gen_ob,type(gen_ob))
    print(dir(gen_ob)) #generators are iterators. it has both __iter__() and __next__()
    print(next(gen_ob))
