def dictionaryAdd(dictionary, key, value):
    dictionary.update({key: value})

listOfNumbers = {}
def collatz(n):
   steps = 0
   while n != 1:
       if n & 1: # n is odd
           n = 3*n + 1
       else: # n is even
           n >>= 1
       steps += 1
   return steps, n 

for each_number in range(1152921504607486125, 2**61):
    resultOfCollatz = collatz(each_number)
    print(f"Number:, {each_number} Total steps: {resultOfCollatz}")
    dictionaryAdd(listOfNumbers, each_number, resultOfCollatz)
print(listOfNumbers)