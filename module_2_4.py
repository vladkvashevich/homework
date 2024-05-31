numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = True
for i in range(len(numbers)):
    a = True
    for j in range(2, numbers[i]):
        if numbers[i] >= j:
            if numbers[i] % j == 1 and a == True and i == j:
                primes.append(numbers[i])
            elif numbers[i] % j == 1 and a == False and i == j:
                not_primes.append(numbers[i])
            else:
                if numbers[i] % j == 0 and i != j and a == True:
                    a = True
                elif numbers[i] % j == 1:
                    a = False
print(" Primes: ", primes)
print(" Not primes: ", not_primes)