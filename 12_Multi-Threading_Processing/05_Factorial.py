import multiprocessing.pool
import multiprocessing, math, sys, time

sys.set_int_max_str_digits(1000000)

# Function to compute factorial of a given number
def factorial(num):
    print(f"Compute factorial of {num}")
    result = math.factorial(num)
    return result

if __name__ == '__main__':
    numbers = [50000, 6000, 7000, 8000]
    start_time = time.time()
    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial,numbers)
    
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Total time taken is: {end_time-start_time}")