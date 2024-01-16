from tqdm import tqdm
from time import sleep

for i in tqdm(range(100)):
    sleep(0.05)

# Example loop with tqdm progress bar
for i in tqdm(range(100), desc="Processing"):
    # Simulating some time-consuming operation
    sleep(0.1)

# Example loop with a styled tqdm progress bar
for i in tqdm(range(10), desc="Processing", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"):
    # Simulating some time-consuming operation
    sleep(0.1)