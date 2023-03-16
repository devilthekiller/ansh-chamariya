# s="good morning moy jsdjs sdnovjowef dfwfv "
# print(s.rjust(20,'*').ljust(35,'%'))    
# print(s.split('o',-2)) #['g', '', 'd m', 'rning m', 'y jsdjs sdn', 'vj', 'wef dfwfv ']
'''
a=input('Enter a string')
str=a[(len(a)-2)//2]+a[(len(a)-1)//2]+a[(len(a)+1)//2]
print(str)
# print(a[(len(a)+1)//2])
# print(a[(len(a)-2)//2])
'''

a=input('Enter a string')
four=a[:4]
count=0
for i in four:
    if(i.isupper()):
        count+=1
if count>=2:
    print(a.upper())
else:
    print('invalid')

'''
a='1a4as2'
sum=0
for i in a:
    if (i.isnumeric()):
        sum=sum+int(i)
print(sum)
'''
