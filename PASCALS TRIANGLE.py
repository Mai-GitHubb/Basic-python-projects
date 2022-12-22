def fact(x):
    factorial = 1
    if x == 0 or x == 1:
        return 1
    else:
        return x*fact(x-1)


def ncr(n, r):
    return fact(n)/(fact(n-r)*fact(r))


def binomial(num_line):
    flag = 0
    l1 = []
    l2 = []
    while flag < num_line:
        for i in range(0, num_line + 1):
            l1.append(round(ncr(flag, i)))
        flag += 1
    for j in l1:
        if j > 0:
            l2.append(j)
    a = 1
    b = 1
    l3 = []
    for i in range(1, num_line + 1):
        a += i
        l3.append(l2[b:a])
        b = a
    for y in l3:

        for z in y:
            print(z, end=' ')
        print('\n')


binomial(int(input('Enter the line number: ')))
