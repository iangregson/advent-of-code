from pathlib import Path

input = Path("i.txt").read_text()
# input = Path("ex.txt").read_text()

def max_idx(bank):
    m = max(bank)
    i = bank.index(m)
    return i, m

def max_joltage(bank, n_batteries = 2):
    if n_batteries == 1:
        return max(bank)
    
    n = len(bank)
    i, m = max_idx(bank[0:n-n_batteries+1])
    return m + max_joltage(bank[i+1:], n_batteries-1)
    

total_output_joltage_a = 0
total_output_joltage_b = 0
for bank in input.splitlines():
    j = max_joltage(bank, 2)
    k = max_joltage(bank, 12)
    total_output_joltage_a += int(j)
    total_output_joltage_b += int(k)

print(total_output_joltage_a)
print(total_output_joltage_b)

