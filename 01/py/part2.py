# Find the top three Elves carrying the most Calories. How many
# Calories are those Elves carrying in total?

from pathlib import Path


def max_sums_top_3_blocks(input_txt):
    block_sums = []
    for block in input_txt.split('\n\n'):
        block_sum = sum(map(int, block.split('\n')))
        block_sums.append(block_sum)
    block_sums.sort()
    return sum(block_sums[-3:])


input_txt = Path('input').read_text()[:-1]
print(max_sums_top_3_blocks(input_txt))
