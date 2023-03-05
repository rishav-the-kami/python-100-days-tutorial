def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(3))

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return recur_fibo(n-1) + recur_fibo(n-2)

print(recur_fibo(3))
