"""
Fibonacci Number
"""
def fibo_iter(n):
    n1 = 0
    n2 = 1

    fibo_numbers = [n1, n2]

    for i in range(n+1):
        n3 = n1 + n2
        if n3 % 2 == 0:
            fibo_numbers.append(n3)
        n1 = n2
        n2 = n3

    return fibo_numbers


def fibi_re(n):
   if n == 0 or n == 1:
     return 1

   n2 = n + fibi_re(n-1)
   print(n2)


# fibi_re(20)

def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(n):
  for i in range(n):
    print(fibonacci(i), end=", ")

print_fibonacci_series(10)
