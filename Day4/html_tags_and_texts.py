'''This example shows a case where first order functions
can be applied in practice.'''
if __name__=="__main__":
    def html_tag(tag):
        def wrap_text(text):
            return "<{0}>{1}</{0}>".format(tag,text)
        return wrap_text
    func1=html_tag("title")
    print(func1("Welcome to Python Programming"))
    print(func1("Hello World"))
    func2=html_tag("div")
    print(func2("<h2>first order function</h2>"))
