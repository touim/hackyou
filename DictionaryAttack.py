import itertools

s = ['toi', 'meno', '1109', '1998']

anagram_list = [''.join(v) for v in itertools.permutations(s)]

print(anagram_list)

#import itertools

#i = 0

#password_list = {"Toi", "Meno", "1109"}

#all = itertools.combinations_with_replacement(password_list, 8)
#for x in all:
#    print(x)
#    #i=+1

#print(i)