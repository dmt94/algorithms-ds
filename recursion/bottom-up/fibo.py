# Bottom up approach to Fibonacci calculation

def fib(n):
    if n == 0:
        return 0
    
    a = 0
    b = 1

    print(f"We are looking for {n}th term")

    #loop from 1 until n
    for i in range(1, n):
        temp = a
        a = b
        b = temp + a
        print(f"This is loop {i}, temp is {temp}, a is {a}, and b is {b}")
    return b

print(fib(6))