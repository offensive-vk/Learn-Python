import asyncio

async def greet(name, delay):
    await asyncio.sleep(delay)  # Simulate a non-blocking delay
    print(f"Hello, {name}!")

async def main():
    # Define tasks
    task1 = asyncio.create_task(greet("Alice", 2))
    task2 = asyncio.create_task(greet("Bob", 1))

    # Wait for tasks to complete
    await task1
    await task2

# Run the event loop to execute the asynchronous tasks
asyncio.run(main())
