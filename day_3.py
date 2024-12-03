import re

def calculate_sum(file_path):
    pattern = r"(mul|do|don\'t)\((\d*),?\s*(\d*)\)"
    total = 0
    include = True
    with open(file_path, 'r') as file:
        text = file.read()
        matches = re.findall(pattern, text)
        for operation, x, y in matches:
            if operation == 'do':
                include = True
            elif operation == "don't":
                include = False
            elif operation == 'mul' and include and x and y:
                total += int(x) * int(y)
    return total

# Test the regex pattern
test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"(mul|do|don\'t)\((\d*),?\s*(\d*)\)"
matches = re.findall(pattern, test_string)
print(matches)  # Expected output: [('mul', '2', '4'), ('mul', '3', '7'), ("don't", '', ''), ('mul', '5', '5'), ('mul', '32', '64'), ('mul', '11', '8'), ('do', '', ''), ('mul', '8', '5')]

if __name__ == "__main__":
    file_path = 'input_Data/day_3.txt'
    result = calculate_sum(file_path)
    print(result)
