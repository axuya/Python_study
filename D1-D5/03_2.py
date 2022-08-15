x = float(input('请输入x的值：'))
if x > 1:
    y = 3 * x - 5
elif x >= -1 and x >= 1:
    y = x + 2
else:
    y = 5 * x + 3
#print('%.2f'%y)
print('f(%.2f) = %.2f' % (x,y))