# Finds the minimal path sum in external_files/083_matrix.txt from the top-left
# to the bottom-right
# Movement in any direction is allowed

# This is solved using the A* search algorithm, which is described here:
# https://en.wikipedia.org/wiki/A*_search_algorithm

from time import clock
import csv

def get_data():
    rows = []
    with open('external_files/083_matrix.txt') as f:
        reader = csv.reader(f)
        for line in reader:
            rows.append([int(x) for x in line])
    return rows

def cost_estimate(beginning,goal):
    xs = beginning[0]
    ys = beginning[1]
    xg = goal[0]
    yg = goal[1]
    output = ((xg-xs)+(yg-ys))*min_value
    return output

def neighbours(node):
    output = []
    x = node[0]
    y = node[1]
    if x+1 < len(row):
        output.append([x+1,y])
    if x-1 > -1:
        output.append([x-1,y])
    if y+1 < len(row):
        output.append([x,y+1])
    if y-1 > -1:
        output.append([x,y-1])
    return output

def reconstruct_path(came_from,current_node):
    total_path = [current_node]
    while repr(current_node) in came_from:
        current_node = came_from[repr(current_node)]
        total_path.insert(0,current_node)
    return total_path

def a_star(beginning,goal):
    closed_set = []
    open_set = [beginning]
    came_from = {}
    infinity = float("inf")
    gscore = {}
    fscore = {}

    for x in range(len(rows)):
        for y in range(len(rows)):
            gscore[repr([x,y])] = infinity
            fscore[repr([x,y])] = infinity
    gscore[repr(beginning)] = 0
    fscore[repr(beginning)] = cost_estimate(beginning,goal)

    while bool(open_set):
        min_fscore = infinity

        for node in open_set:
            if fscore[repr(node)] < min_fscore:
                min_fscore = fscore[repr(node)]
                current_node = node

        if current_node == goal:
            return reconstruct_path(came_from,current_node)

        open_set.remove(current_node)
        closed_set.append(current_node)

        for neighbour in neighbours(current_node):
            if neighbour in closed_set:
                continue

            tentative_gscore = gscore[repr(current_node)] + \
                    rows[neighbour[1]][neighbour[0]]

            if neighbour not in open_set:
                open_set.append(neighbour)
            elif tentative_gscore >= gscore[repr(neighbour)]:
                continue

            came_from[repr(neighbour)] = current_node
            gscore[repr(neighbour)] = tentative_gscore
            fscore[repr(neighbour)] = gscore[repr(neighbour)] + \
                    cost_estimate(neighbour,goal)

start = clock()

rows = get_data()

min_value = 9999
for row in rows:
    for item in row:
        if item < min_value:
            min_value = item

beginning = [0,0]
goal = [len(rows)-1,len(rows)-1]

optimal = a_star(beginning,goal)
score = sum([rows[node[1]][node[0]] for node in optimal])

end = clock()

print score
print "Time taken: ", end-start, " s"
