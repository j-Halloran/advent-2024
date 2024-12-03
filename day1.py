import heapq
from collections import Counter

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [line.strip().split() for line in file]
    return [(int(x), int(y)) for x, y in data]

def main():
    
    file_path = 'input_data/day_1.txt'
    data = read_data(file_path)
    
    column_1_queue = []
    column_2_queue = []
    
    for x, y in data:
        heapq.heappush(column_1_queue, x)
        heapq.heappush(column_2_queue, y)
    
    running_sum = 0
    column_1_queue.sort()
    column_2_queue.sort()

    column2_counter = Counter(y for _, y in data)
    similarity_scores = [x * column2_counter[x] for x, _ in data]
    total_similarity_score = sum(similarity_scores)
    print(f"Total similarity score: {total_similarity_score}")
    
    while column_1_queue and column_2_queue:
        col1_val = heapq.heappop(column_1_queue)
        col2_val = heapq.heappop(column_2_queue)
        running_sum += abs(col1_val - col2_val)
    
    print(f"Running sum: {running_sum}")

if __name__ == "__main__":
    main()