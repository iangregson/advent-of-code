from pathlib import Path

# file = Path(__file__).parent / "test_input.txt"
file = Path(__file__).parent / "input.txt"
lines = file.read_text()
# lines = '1,2,3,6,5,4'

nums = [int(x) for x in lines.split(',')]
block_tile_count = 0

i = 2
n = len(nums)
while i < n:
    x,y,id = nums[i-2], nums[i-1], nums[i]
    if id == 2:
        block_tile_count += 1
    i += 1

print(block_tile_count)