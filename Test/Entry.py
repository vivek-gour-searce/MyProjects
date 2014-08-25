def result():
    try:
        a = int(raw_input('Enter a number : '))
        b = int(raw_input('Enter a number : '))
        c = raw_input('Enter your Choice : A for Add : B for Substract : \
C for Multiply : D for Divide\n')
        while True:
            if c in ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd']:
                print 'Your choice is :', c
                m = math(a, b, c)
                print 'Result is :: ', m
                break
            else:
                print 'Please enter correct choice'
                c = raw_input('Enter your Choice : A for Add : B for Substract : \
C for Multiply : D for Divide\n')
    except:
        print 'Please enter a number', result()


def math(x, y, z):
    if z in ['A', 'a']:
        return x + y
    elif z in ['B', 'b']:
        return x - y
    elif z in ['C', 'c']:
        return x * y
    else:
        return float(x / y)
    

result()
