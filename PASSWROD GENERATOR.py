def random_pass(length, no_num, no_sym):
    import random as r
    import string
    alpha = list(string.ascii_letters)
    num = [str(i) for i in range(0,10)]
    sym = ['!', '#', '$', '%', '&', "'", '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
           '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    ranalpha, rannum, ransym = [], [], []

# random alphabets
    for i in range(length-(no_num+no_sym)):
        if len(ranalpha) > length-(no_num+no_sym):
            break
        else:
            al = r.randint(0, len(alpha) - 1)
            x = alpha[al]
            ranalpha.append(x)

    # random symbols
    for j in range(no_sym):
        if len(ransym) > no_sym:
            break
        else:
            rs = r.randint(0, len(sym) - 1)
            s = sym[rs]
            ransym.append(s)

    # random numbers
    for j in range(no_num):
        if len(rannum) > no_num:
            break
        else:
            rn = r.randint(0, len(num) - 1)
            n = num[rn]
            rannum.append(n)

    for k in r.sample(ranalpha+ransym+rannum, length):
        print(k, end='')

length = int(input('How long do you want your password to be: '))
no_num = int(input('How many numbers should your password contain: '))
no_sym = int(input('How many symbols should your password contain: '))
random_pass(length, no_num, no_sym)
