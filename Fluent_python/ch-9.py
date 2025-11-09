# def deco(func):
#     def inner():
#         print('Running inner()')
#     return inner

# @deco
# def target():
#     print('Running target()')

# target = deco(target)


# target()

# print(target)

# ------------------------------------

# registry = []

# def register(func):
#     print(f'Running register({func})')
#     registry.append(func)
#     return func

# @register
# def f1():
#     print('Running f1()')

# @register
# def f2():
#     print('Running f2()')

# def f3():
#     print('Running f3()')

# def main():
#     print('Running main()')
#     print('Registry ->', registry)
#     f1()
#     f2()
#     f3()

# main()

# ------------------------------------

# def add_five(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs) + 5
#     return wrapper

# @add_five
# def sum_two_numbers(a,b):
#     return a+b

# result = sum_two_numbers(10,15)
# print(result)

# @add_five
# def add_zero(num):
#     return num

# result2 = add_zero(10)
# print(result2)

# ----------------------------------------
# closures


# import time
# from functools import lru_cache

# #
# # This is the @lru_cache decorator
# # It will "wrap" the function below and give it a "memory."
# #
# @lru_cache(maxsize=128) # We set a max "memory" size
# def slow_database_call(user_id):
#     """
#     This is our "slow" function.
#     Imagine it's fetching data from a database, which takes 2 seconds.
#     """
#     print(f"--- RUNNING: Fetching data for user {user_id} (This will take 2 seconds)...")
#     time.sleep(2)
#     print(f"--- COMPLETED: Fetch for {user_id}")
#     return f"User Data for {user_id}"

# # --- Main execution ---
# if __name__ == "__main__":
    
#     print("Welcome! Let's test our cached function.\n")
    
#     # --- First Call ---
#     print("Calling with user_id=1 (FIRST time):")
#     start = time.time()
#     data = slow_database_call(1)
#     end = time.time()
#     print(f"Result: {data}")
#     print(f"Time taken: {end - start:.2f}s\n")
    
#     # --- Second Call (Cached) ---
#     print("Calling with user_id=1 (SECOND time):")
#     start = time.time()
#     data = slow_database_call(1)
#     end = time.time()
#     print(f"Result: {data}")
#     print(f"Time taken: {end - start:.2f}s  <-- INSTANT!\n")
    
#     # --- Third Call (New Argument) ---
#     print("Calling with user_id=2 (FIRST time):")
#     start = time.time()
#     data = slow_database_call(2)
#     end = time.time()
#     print(f"Result: {data}")
#     print(f"Time taken: {end - start:.2f}s\n")
    
#     # --- Fourth Call (Cached) ---
#     print("Calling with user_id=2 (SECOND time):")
#     start = time.time()
#     data = slow_database_call(2)
#     end = time.time()
#     print(f"Result: {data}")
#     print(f"Time taken: {end - start:.2f}s  <-- INSTANT!\n")

#     # --- Fifth Call (Cached again) ---
#     print("Calling with user_id=1 (THIRD time):")
#     start = time.time()
#     data = slow_database_call(1)
#     end = time.time()
#     print(f"Result: {data}")
#     print(f"Time taken: {end - start:.2f}s  <-- Still instant!\n")

#     print("--- Cache Info ---")
#     # We can even check the cache's status!
#     print(slow_database_call.cache_info())

# ------------------------------

#fastapi decorator example

# from fastapi import FastAPI
# import uvicorn
# # import time

# app = FastAPI()

# @app.get('/')
# def home():
#     "Landing page"
#     return {"message": "hello world"}

# -------------------------------------------



