# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    s = str(num)
    n = ''
    b = str()
    if s == '0':
        return n
    for i in range(len(s) - 1, -1, -1):
        if s[i] != '0':
            n = s[i:]
            s = str(int(num) - int(n))
            return ''.join(expanded_form(s) + n)


print(expanded_form(70304))


