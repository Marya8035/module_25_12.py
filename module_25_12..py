numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # начальный список
primes = []# простые числа
not_primes = [] # не простые числа
for i in numbers:
    print (i)
    if i > 1:
        for k in range(2, i):
            print(i % k)
            if i % k == 0:
                not_primes.append(i)
                break
        else:
            primes.append(i)


print (primes)
print(not_primes)