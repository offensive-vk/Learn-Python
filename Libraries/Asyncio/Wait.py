import asyncio

# Define a coroutine that prints a message after a delay
async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

# Define a coroutine that waits for multiple tasks to complete
async def main():
    # Create tasks
    task1 = asyncio.create_task(greet("Alice", 2))
    task2 = asyncio.create_task(greet("Bob", 1))

    # Wait for any task to complete
    done, pending = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)

    # Cancel pending tasks
    for task in pending:
        task.cancel()

# Run the event loop to execute the asynchronous tasks
asyncio.run(main())
