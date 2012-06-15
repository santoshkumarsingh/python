import sys
import itertools
from collections import deque

class Node(object):
    def __init__(self, parent, last_move, config_str):
        self.parent = parent
        self.last_move = last_move
        self.config_str = config_str
    
    def next_configs(self, k_pegs, permutations):
        pegs = config_to_pegs(self.config_str, k_pegs)
        nexts = []

        for frm, to in permutations:
            if pegs[frm] != [] and (pegs[to] == [] or pegs[frm][-1] < pegs[to][-1]):
                moved = pegs[frm][-1]
                next = self.config_str.split(' ')
                next[moved - 1] = str(to + 1)
                nexts.append(Node(self, (frm + 1, to + 1), " ".join(next)))

        return nexts
    
    def __hash__(self):
        return hash(self.config_str)
    
    def __eq__(self, other):
        return self.config_str == other.config_str

def config_to_pegs(config_str, n_pegs):
    config = [int(x) for x in config_str.split(' ')]
    pegs = [[] for _ in range(n_pegs)]
    ints = range(1, len(config) + 1)
    for i in reversed(range(len(config))):
        pegs[config[i] - 1].append(ints[i])
    return pegs

def pegs_to_config(pegs):
    config = [None] * len(pegs)
    for i in range(len(pegs)):
        peg = pegs[i]
        for x in peg:
            config[x - 1] = i + 1
    return " ".join(map(str, config))

def bfs(s_config, e_config, k_pegs):
    permutations = list(itertools.permutations(range(k_pegs), 2))
    visited_nodes = set()
    queue = deque([Node(None, None, s_config)])
    
    while queue:
        node = queue.popleft()
        if node not in visited_nodes:
            visited_nodes.add(node)
            if node.config_str == e_config:
                break
            nexts = node.next_configs(k_pegs, permutations)
            queue.extend(nexts)
        
    moves = []
    while node:
        if node.last_move:
            moves.append(node.last_move)
        node = node.parent
    moves.reverse()

    return moves
    
while True:
    try:
        line = raw_input()
        n, k = [int(x) for x in line.split(' ')]
        s_config = raw_input()
        e_config = raw_input()

        moves = bfs(s_config, e_config, k)

        print len(moves)
        for x, y in moves:
            print x, y
    except EOFError:
        break
