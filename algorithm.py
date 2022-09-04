from enum import Enum
from copy import deepcopy
from collections import deque


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class HamiltonianPath:

    def __init__(self, graph_width, graph_height):
        self.path = deque()
        self.adj_dict = {}
        self.initial_adj_dict = {}
        self.graph_width = graph_width
        self.graph_height = graph_height
        self.num_vertices = graph_width*graph_height
        self.visited = None
        self.path_detected = False
        self.snake_vertices = None

        self.graph_init()

    def get_cycle(self, start_vertex):
        self.path.clear()
        self.path_detected = False
        self.visited = [False]*self.num_vertices
        self.path.append(start_vertex)
        self.calculate(start_vertex)

    def calculate(self, actual_vertex):

        if actual_vertex == self.path[0] and len(self.path) == self.num_vertices + 1 \
           and not self.path_detected:
            self.path_detected = True
            return

        for vertex, direction in self.adj_dict[actual_vertex].items():

            if len(self.path) == 1:
                if vertex not in self.snake_vertices:
                    self.add_path(vertex, direction)
                continue

            self.add_path(vertex, direction)

    def add_path(self, vertex, direction):
        if self.visited[vertex] is False:
            self.visited[vertex] = True
            self.path.append(direction)

            self.calculate(vertex)

            if self.path_detected is False:
                self.visited[vertex] = False
                self.path.pop()

    def graph_init(self):
        for i in range(self.num_vertices):
            left, right = i-1, i+1
            up, down = i-self.graph_width, i+self.graph_width
            adjacents = {}

            if (left // self.graph_width == i // self.graph_width) \
                    and (0 <= left < self.num_vertices):
                adjacents[left] = Direction.LEFT
            if (right // self.graph_width == i // self.graph_width) \
                    and (0 <= right < self.num_vertices):
                adjacents[right] = Direction.RIGHT
            if up >= 0:
                adjacents[up] = Direction.UP
            if down < self.num_vertices:
                adjacents[down] = Direction.DOWN

            self.adj_dict[i] = adjacents

        self.initial_adj_dict = deepcopy(self.adj_dict)

    def change_adjacents(self, vertices_arr):
        self.snake_vertices = vertices_arr

        self.remove_adjacents(self.snake_vertices[1])
        if self.adj_dict[self.snake_vertices[-1]] != self.initial_adj_dict[self.snake_vertices[-1]]:
            self.restore_adjacents(self.snake_vertices[-1])

    def remove_adjacents(self, vertex):
        for ver in self.adj_dict[vertex].copy():
            if ver not in self.snake_vertices:
                self.adj_dict[vertex].pop(ver)
                self.adj_dict[ver].pop(vertex)

    def restore_adjacents(self, vertex):
        for ver in self.initial_adj_dict[vertex]:
            if ver not in self.adj_dict[vertex] and ver not in self.snake_vertices:
                self.adj_dict[vertex][ver] = self.initial_adj_dict[vertex][ver]
                self.adj_dict[ver][vertex] = self.initial_adj_dict[ver][vertex]
