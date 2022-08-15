#F = float(input('请输入华氏温度 = '))
#C = (F - 32) / 1.8
#print('摄氏温度为 = ',C)

#r = int(input('请输入圆的半径 = '))
#c = 2 * 3.14 * r
#s = 3.14 * r * r
#print('周长: %.2f' % c)
#print('面积: %.2f'% s)

year = int(input('请输入年份：'))
if_year =  year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(if_year)
    
