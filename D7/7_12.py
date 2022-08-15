#生成式和生成器
import sys

f = [x for x in range(1,100)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

f = [x ** 2 for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)

f = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)