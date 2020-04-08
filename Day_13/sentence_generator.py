'''Python program to implement sentence generator'''
if __name__=="__main__":
    def str_gen(str):
        words=str.split()
        for word in words:
            yield word

    sentence="How are you?"
    gen_ob=str_gen(sentence)
    print(gen_ob,type(gen_ob))
    # for i in gen_ob:
    #     print(i)
    print(next(gen_ob))
    print(next(gen_ob))
