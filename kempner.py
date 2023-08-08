import math

def kempner(num, limit=1, factorial=1):
    #first we check if the number is prime
    prime = 0
    for i in range(2, int(math.sqrt(num))+1):
      if (num % i == 0):
        prime = 1
        break
    if (prime == 0):
      return num
    else:
      if factorial%num == 0:
        return max(1, limit-1)
      elif factorial%num!=0:
        return kempner(num, limit+1, factorial*limit)

kempner(10)


