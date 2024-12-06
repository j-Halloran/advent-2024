from collections import defaultdict, deque

def read_input(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def parse_rules_and_updates(lines):
    # Separate rules from updates
    rules = []
    updates = []
    reading_rules = True

    for line in lines:
        if '|' in line and reading_rules:
            rules.append(line)
        else:
            reading_rules = False
            updates.append(line)

    return rules, updates

def check_order(update_pages, rules):
    # Check if given update_pages is correct according to the rules
    page_set = set(update_pages)
    pos = {p: i for i, p in enumerate(update_pages)}

    for rule in rules:
        X, Y = rule.split('|')
        if X in page_set and Y in page_set:
            if pos[X] > pos[Y]:
                return False
    return True

def topological_sort_update(update_pages, rules):
    # Restrict rules to just those pages in update_pages
    page_set = set(update_pages)
    # Build graph
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for p in update_pages:
        indegree[p] = 0  # ensure each page is accounted for

    for rule in rules:
        X, Y = rule.split('|')
        if X in page_set and Y in page_set:
            graph[X].append(Y)
            indegree[Y] += 1

    # Kahn's algorithm for topological sort
    q = deque([p for p in update_pages if indegree[p] == 0])
    sorted_pages = []
    while q:
        node = q.popleft()
        sorted_pages.append(node)
        for nei in graph[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # If there's a cycle (no valid topological ordering), 
    # sorted_pages won't have all pages. 
    # For the puzzle, we assume there is always a valid ordering.
    return sorted_pages

def solve(filename):
    lines = read_input(filename)
    rules, updates = parse_rules_and_updates(lines)

    incorrect_updates = []
    for u in updates:
        update_pages = [p.strip() for p in u.split(',')]
        if not check_order(update_pages, rules):
            incorrect_updates.append(update_pages)

    total = 0
    for u_pages in incorrect_updates:
        corrected = topological_sort_update(u_pages, rules)
        mid_index = len(corrected) // 2
        mid_page = int(corrected[mid_index])
        total += mid_page

    print(total)

if __name__ == "__main__":
    solve("input_data/day_5.txt")
