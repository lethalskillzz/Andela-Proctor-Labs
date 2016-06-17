def get_algorithm_result(listNum):
  largest = listNum[0]
  for i in range(1, len(listNum)):
    if largest < listNum[i]:
      largest = listNum[i]
  return (largest)
  
  
def prime_number(x):
    if x < 2:
        return False
    else:
        n = 2
        while n < x:
            if x % n == 0:
                return False
                break
            n = n + 1
        else:
            return True  