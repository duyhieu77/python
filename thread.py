import asyncio

async def add(a, b):
    await asyncio.sleep(1)
    return a + b

async def subtract(a, b):
    await asyncio.sleep(1)
    return a - b

async def multiply(a, b):
    await asyncio.sleep(1)
    return a * b

async def divide(a, b):
    await asyncio.sleep(1)
    if b == 0:
        return "Cannot divide by zero"
    return a / b

async def main():
    a = 16
    b = 8

    add_task = asyncio.create_task(add(a, b))
    subtract_task = asyncio.create_task(subtract(a, b))
    multiply_task = asyncio.create_task(multiply(a, b))
    divide_task = asyncio.create_task(divide(a, b))

    results = await asyncio.gather(add_task, subtract_task, multiply_task, divide_task)
    
    print(f"Addition: {results[0]}")
    print(f"Subtraction: {results[1]}")
    print(f"Multiplication: {results[2]}")
    print(f"Division: {results[3]}")

asyncio.run(main())