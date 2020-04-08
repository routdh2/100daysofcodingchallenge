'''Program to create sentence iterator'''
if __name__=="__main__":
    class Sentence:
        def __init__(self,str):
            self.sentence=str
            self.index=0
        def __iter__(self):
            return self
        def __next__(self):
            words=self.sentence.split()
            if self.index>=len(words):
                raise StopIteration
            else:
                current=words[self.index]
                self.index+=1
                return current

    my_sentence=Sentence("This is a test. I am Dhananjay Rout. How are you boy?")
    for word in my_sentence:
        print(word)
