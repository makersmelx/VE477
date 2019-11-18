import heapq
import os
import time


def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']:
        r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1:
            r = ">"
        if x2 == x1 - 1:
            r = "<"
        if y2 == y1 + 1:
            r = "v"
        if y2 == y1 - 1:
            r = "^"
    if 'weight' in style:
        r = "%d" % graph.cost(id)
    if 'start' in style and id == style['start']:
        r = "S"
    if 'goal' in style and id == style['goal']:
        r = "T"
    if id in graph.walls:
        r = "#"
    return r


def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            r = draw_tile(graph, (x, y), style, width)
            if r == "S" or r == "T":
                print("\033[1;37;40m%%-%ds\033[0m" % width % r, end="")
            elif r == "#":
                print("\033[1;30;47m%%-%ds\033[0m" % width % r, end="")
            elif 'path' in style and (x, y) in style['path']:
                print("\033[5;30;45m%%-%ds\033[0m" % width % r, end="")
            elif 'demo' in style and (x, y) == style['demo']:
                print("\033[5;30;45m%%-%ds\033[0m" % width % r, end="")
            elif 'exist' in style and (x, y) in style['exist']:
                print("\033[5;30;46m%%-%ds\033[0m" % width % r, end="")
            else:
                print("%%-%ds" % width %
                      draw_tile(graph, (x, y), style, width), end="")
        print()


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0:
            results.reverse()  # aesthetics
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results


class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, to_node):
        return self.weights.get(to_node, 1)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def enqueue(self, key, item):
        heapq.heappush(self.elements, (key, item))

    def dequeue_min(self):
        return heapq.heappop(self.elements)[1]


def track_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        if current in came_from:
            current = came_from[current]
        else:
            return ""
    path.append(start)
    path.reverse()
    return path


def heuristic(a, b):
    # Manhattan distance
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start, goal):
    point_queue = PriorityQueue()
    point_queue.enqueue(0, start)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not point_queue.empty():
        current = point_queue.dequeue_min()
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                key = new_cost + heuristic(goal, next)
                point_queue.enqueue(key, next)
                came_from[next] = current
        draw_grid(square_grid, width=3, exist=cost_so_far, demo=current, point_to=came_from,
                  start=start, goal=goal)
        print()
        print("="*30)
        print()
        draw_grid(square_grid, width=3, exist=cost_so_far, demo=current, number=cost_so_far,
                  start=start, goal=goal)
        time.sleep(0.8)
        os.system("clear")
    return came_from, cost_so_far


square_grid = GridWithWeights(10, 10)
square_grid.walls = [(1, 7), (1, 8), (2, 7), (2, 8),
                     (3, 7), (3, 8), (4, 7), (4, 8),
                     (3, 0), (4, 0), (4, 1), (4, 2),
                     (4, 3), (5, 3), (6, 3), (4, 6),
                     (4, 6), (0, 5), (0, 4)]
for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
            (4, 3), (4, 4), (4, 5), (4, 6),
            (4, 7), (4, 8), (5, 1), (5, 2),
            (5, 3), (5, 4), (5, 5), (5, 6),
            (5, 7), (5, 8), (6, 2), (6, 3),
            (6, 4), (6, 5), (6, 6), (6, 7),
            (7, 3), (7, 4), (7, 5)]:
    square_grid.weights[loc] = 5
for loc in [(0, 0), (3, 0), (3, 2), (8, 3)]:
    square_grid.weights[loc] = 9
for loc in [(6, 0), (9, 2), (9, 7), (5, 9)]:
    square_grid.weights[loc] = 3
for loc in [(3, 9)]:
    square_grid.weights[loc] = 2

if __name__ == '__main__':
    start, goal = (1, 4), (9, 0)
    print("Weight distribution")
    draw_grid(square_grid, width=3, weight={},
              start=start, goal=goal)
    print('Type "Enter" to continue')
    tmp = input()
    came_from, cost_so_far = a_star_search(square_grid, start, goal)
    path = track_path(came_from, start, goal)
    draw_grid(square_grid, width=3, path=path,
              point_to=came_from, start=start, goal=goal)
    print()
    draw_grid(square_grid, width=3, path=path,
              number=cost_so_far, start=start, goal=goal)
    print()
