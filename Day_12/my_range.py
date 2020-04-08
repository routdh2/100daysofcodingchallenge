'''Implementing a custom range() function in Python'''
if __name__=="__main__":
    class MyRange:
        def __init__(self,start,end):
            self.value=start
            self.end=end
        def __iter__(self):
            return self
        def __next__(self):
            if self.value >= self.end:
                raise StopIteration
            else:
                current=self.value
                self.value+=1
                return current
    # nums=MyRange(1,10)
    for i in MyRange(1,10):
        print(i)
