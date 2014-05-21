import random
for i in range(100):
    m =random.randint(1,10)
    print"random integer:", m
    n = raw_input("Enter a number:")
    x = 0
    if n > m:
        x=1
        print x
        print '**************************'
    if n < m:
        x = -1
        print x

    if n == m:
        x =0
        print x,"you guessed correctly"
        break;

