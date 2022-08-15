#使用元组
t = ('小明',22,True,'浙江杭州')
print(t)

print(t[0])
print(t[3])

for member in t:
    print(member)

t = ('小蒋',21,True,'上海上海')
print(t)

person = list(t)
print(person)

fruits_list = ['apple','banana','orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)