a = list(range(2,8))

for i in a:
    print(i)

a.append('Python')
print(len(a))

print(a[0], a[-1], a[1:3])
a.remove('Python')
