#("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
#a speech sound that you make with your lips and teeth open, shown in English by the letters
# 'a', 'e', 'i', 'o' or 'u'

def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")



a_ = "This website is for losers LOL!"
print(disemvowel(a_))
