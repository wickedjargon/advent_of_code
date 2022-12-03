# Find the Elf carrying the most Calories. How many total Calories is
# that Elf carrying?

from pathlib import Path


def max_sum_block(input_txt):
    block_sums = []
    for block in input_txt.split('\n\n'):
        block_sum = sum(map(int, block.split('\n')))
        block_sums.append(block_sum)
    return max(block_sums)


input_txt = Path('input').read_text()[:-1]
print(max_sum_block(input_txt))