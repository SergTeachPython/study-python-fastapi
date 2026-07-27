def prime_generator(end):
    if end > 1:
        for i in range(2, end + 1):
            error_key = False
            for j in range(2, i):
                if i % j == 0:
                    error_key = True
                    break
            if not error_key:
                yield i
    else:
        return True

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
