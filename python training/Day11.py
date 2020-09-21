##relic = 34
##varus=(' Sunday', 29, 'I am 12 years old', 'welcome', ' we know you are', ' years old...')
##def myName(*varus):
##    return varus[3] + str(varus[0]) + varus[-2] + ' ' + str(varus[1]) + varus[-1]
##var_me = myName(*varus)
##print(var_me)

varus = ('slik', 34)
def insertvarus(*var, x=22):
    valala = 'she is ' + str(var[0])+ ' on day '+ str(var[1]) + ' but she is '
    vala = valala + str(x) + ' years old'
    return vala
meout = insertvarus(*varus)
print(meout)
