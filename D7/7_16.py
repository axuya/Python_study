scores = {'A':93,'B':87,'C':23,}
print(scores)

items1 = dict(one = 1,two = 2,three = 3,four = 4)
items2 = dict(zip(['a','b','c'],'123'))

items3 = {num:num ** 2 for num in range(1,10)}
print(items1,items2,items3)

print(scores['A'])
print(scores['C'])

for key in scores:
    print(f'{key}: {scores[key]}')

scores['元芳'] = 65
scores['诸葛'] = 71
scores.update(冷面=67,雨燕=85)

print(scores)

if 'Jay' in scores:
    print(scores['Jay'])
print(scores.get('Jay'))

print(scores.get('Jay',100))

print(scores.popitem())
print(scores.popitem())
print(scores.pop('xu',100))

scores.clear()
print(scores)