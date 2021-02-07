# Q1
score = {'korean': 80, 'english': 75, 'math': 55}
print(sum(score.values()))

# Q2
num = 13
if num%2 == 0:
    print('even')
else:
    print('odd')

# Q3
pin = '881120-1068234'
print(pin.split('-')[0])
print(pin.split('-')[1])

# Q4
if pin[7] == '1':
    print('man')
elif pin[7] == '2':
    print('woman')
else:
    print('unknown')

# Q5
a = 'a:b:c:d'
print(a.replace(':','#'))

# Q6
arr = [1,3,5,4,2]
arr.sort()
arr.reverse()
print(arr)

# Q7
arr2 = ['Life', 'is', 'too', 'short']
str = ' '.join(arr2)
print(str)

# Q8
b = (1,2,3)
c = (4,)
d = b+c
# print('address of b : ', id(b))
# print('address of c : ', id(c))
# print('address of d : ', id(d))
print(d)

# Q10
a = {'A':90, 'B':80, 'C':70}
print(a['B'])
print(a.pop('B'))

# Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a = set(a)
a = list(a)
print(a)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)