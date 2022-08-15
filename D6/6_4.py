def foo():
    b = 'hello'

    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()

if __name__ == '__main__':
    a = 100
    foo()

##局部作用域 嵌套作用域 全局作用域 内置作用域