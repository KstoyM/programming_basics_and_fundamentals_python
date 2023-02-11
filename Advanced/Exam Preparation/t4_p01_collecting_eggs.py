from collections import deque

eggs = deque(map(int, input().split(", ")))
papers = deque(map(int, input().split(", ")))

filled_boxes = 0
box_size = 50
boxed_eggs = 0

while eggs and papers:

    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()
    wrapped_egg = current_egg + current_paper

    if wrapped_egg <= box_size:
        boxed_eggs += 1

if boxed_eggs:
    print(f"Great! You filled {boxed_eggs} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(el) for el in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(el) for el in papers)}")

