import sys


def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    return True


def isGenerator(g, p, showProgress = True):

    lReturn = True

    should = [i for i in range(1,p)]

    arr = [0 for i in range(p-1)]
    i = 1
    arr[0] = (g**i) % p
    for row in range(1,p-1):
        arr[row] = (arr[row-1]*g) % p
        i += 1
    #print(should)
    #print(arr)


    j = 0
    while j < p-1 and lReturn:
        if showProgress: progressBar(j,p)
        if should[j] not in arr:
            lReturn = False
        j += 1

    if showProgress: print('\r')
    return lReturn


def getGenerators(p):

    aReturn = [0 for i in range(p-1)]
    j = 0
    for i in range(1,p-1):
        progressBar(i, p-1)
        if isGenerator(i,p,False):
            aReturn[j] = i;
            j += 1

    aReturn = aReturn[:j]
    print('\r')
    return aReturn


def gcd(x, y):
    #using Euclidean Algorithm
    while (y):
        x, y = y, x % y
    return x


def getDenominator(n):
    c = 0
    lReturn = 0
    while c < 1:
        c += n
        lReturn += 1

    return lReturn


def inverseMod(a, b):
    #a = denominator

    lReturn = 0
    lExit = False

    i = 1
    while i < b and not lExit:
        if ((a*i)%b) == (1%b):
            lReturn = i
            lExit = True;
        i += 1

    return lReturn

def negativeMod(a, b):
    lReturn = b - (a*(-1) % b)
    return lReturn



def progressBar(value, endvalue, bar_length=20):

    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()







#map size (p) and generator (g)
p = 541 #65497 #41 #should be a prime
g = 128 #134 #7

#private key of Alice
alpha = 105 #17 #5

#a)
if isPrime(p):
    print(str(p) + ' is a prime')

    if isGenerator(g, p):
        print(str(g) + ' is a generator')
    else:
        print(str(g) + ' is not a generator')

    #may takes a looong time
    #print('generators are: ' + str(getGenerators(p)))

else:
    print(str(p) + ' is not a prime')





#b)
publicKey = (g**alpha) % p
print('public key of Alice = ' + str(publicKey))


#c)
r = 31 #45625 #3 #ephemerical  key
if gcd(r,p-1) == 1:
    print('gcd(' + str(r) + ', ' + str(p) + '-1) = 1')


#d)
m = 95 #11123 #13
x = (g**r) % p
y = negativeMod(  (m - alpha *x) * inverseMod(r,p-1)  , p-1)
print('signature: ' + str(y) + ' (x = ' + str(x) + ')')


#e)
leftside = (publicKey**x * x**y) % p
rightside = (g**m) % p
print('verification: ' + str(leftside) + ' = ' + str(rightside) + ' (' + str(leftside==rightside) + ')')


#f)
m = 221
x = 111
y = 333
leftside = (publicKey**x * x**y) % p
rightside = (g**m) % p
print('verification: ' + str(leftside) + ' = ' + str(rightside) + ' (' + str(leftside==rightside) + ')')



