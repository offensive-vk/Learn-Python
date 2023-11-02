import asyncio

# Define two asynchronous functions that simulate I/O-bound tasks.
async def fetch_data(url):
    print(f"Fetching data from {url}")
    await asyncio.sleep(2)  # Simulate a network request
    print(f"Data fetched from {url}")

async def process_data(data):
    print(f"Processing data: {data}")
    await asyncio.sleep(1)  # Simulate data processing
    print("Data processing complete")

async def main():
    # Create two tasks to fetch and process data concurrently.
    task1 = asyncio.create_task(fetch_data("example.com"))
    task2 = asyncio.create_task(process_data("Sample Data"))

    # You can also run other code here that doesn't need to be asynchronous.

    # Wait for both tasks to complete.
    await task1
    await task2

if __name__ == "__main__":
    asyncio.run(main())
