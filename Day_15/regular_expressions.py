'''Program to explore "re" module in python'''
if __name__=="__main__":
    import re
    text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
    '''
    sentence="Start a sentence here and complete in the end"
    pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
    matches = pattern.finditer(text_to_search)
    for match in matches:
        print(match)

    pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
    matches=pattern.finditer(text_to_search)
    for match in matches:
        print(match)

    pattern=re.compile(r"Ha\B")
    print(pattern,type(pattern))
    matches=pattern.finditer(text_to_search)
    for match in matches:
        print(match)

    pattern=re.compile(r"^Start[\w\s]*end$")
    matches=pattern.finditer(sentence)
    for match in matches:
        print(match)
