# Fibonacci sequence is as follows: 0, 1, 1, 2, 3, 5, 8, 13, ...

# Lucas Numbers: 2, 1, 3, 4, 7, 11, 18, 29, ...
print("""
fibonacci sequence:
n is the nth value in the series, 0th term and negative numbers are not allowed
0 is the first number in the sequence
1 is the second number in the sequence
Any number after the second term is calculated using the formula below:
fibonacci(n-1) + fibonacci(n-2) = nth term
""")

def fibonacci(n):
  if n <= 0:
    print('0 and negative numbers are not allowed!')
  elif n==1:
    return 0
  elif n==2:
    return 1 
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print("""
Lucas Sequence:
n is the nth value in the series, 0th term and negative numbers are not allowed 
2 is the first number in the sequence
1 is the second number in the sequence
Any number after the second term is calculated using the formula below:
lucas(n-1) + lucas(n-2) = nth term
""")

def lucas(n):
  if n <= 0:
    print('0 and negative numbers are not allowed!')
  elif n==1:
    return 2
  elif n==2:
    return 1 
  else:
    return lucas(n-1) + lucas(n-2)

print("""
sum_series(i, x, y):
The sum series takes in 1 required argument, where it gives us the nth term. 
The second and third arguments gives us the first and second term respectively.
Having no arguments for the second and third arguments will default to the fibonacci series. 
n is the nth value in the series, 0th term and negative numbers are not allowed.
2 is the first number in the sequence
1 is the second number in the sequence

Any number after the second term is calculated using the formula below:
sum_series(i - 1, x, y) + sum_series(i - 2, x, y) = nth term
""")

def sum_series(i, x=0, y=1):

  if (x == 0 and y == 1):
    if i - 1 == 0:
      return x
    if i - 1 == 1:
      return y
    return sum_series(i - 1, x, y) + sum_series(i - 2, x, y)
  else:
    if i == 1:
      return x
    if i == 2:
      return y
    return sum_series(i - 1, x, y) + sum_series(i - 2, x, y)
  