# URL: https://www.codewars.com/kata/520b9d2ad5c005041100000f/python
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
def pig_it(text):
    #your code here
    x = text.split()
    n = []
    for i in x:
        t = i[0]
        if i == "!" or i == "?":
            n.append(i)
        else:
            i = i.replace(i[0],'',1)
            i += t
            i += "ay"

            n.append(i)
    return (' '.join(n))
            




print(pig_it('This is my string ! ?'))


# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])