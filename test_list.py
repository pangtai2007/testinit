list=[1,2,3,4,5]

for x in list:
    x = 1

print(list)

for i in range(0,len(list)):
    list[i] = 2

print(list)

#test order
# 就是按照索引顺序
list=[1,2,3,4,5]
for x in list:
    print(x)