# [4.1] Route Between Nodes: Given a directed graph, 
# design an algorithm to find out whether there is 
# a route between two nodes. 

import unittest


def path_bfs(node1, node2, graph):
    path = [node1]
    visted = [node1]

    while path:
        current_node = path.pop(0)
        for child in graph.get(current_node, []):
            if child == node2:
                return True

            if not child in visted:
                visted.append(child)
                path.append(child)

    return False

def path_dfs(node1, node2, graph):
    path = [node1]
    visted = [node1]

    while path:
        current_node = path.pop()
        for child in graph.get(current_node, []):
            if child == node2:
                return True

            if not child in visted:
                visted.append(child)
                path.append(child)

    return False

def path_dfs_r(node1, node2, graph):
    path = path_dfs_r_helper(node1, node2, graph)
    return node2 in path

def path_dfs_r_helper(node1, node2, graph, path=set()):
    for child in graph.get(node1, []):
        if not child in path:
            path.add(child)
            path_dfs_r_helper(child, node2, graph, path)
    
    return path


class Test(unittest.TestCase):
    
    def test_bfs(self):
        graph = {
            'A':['B', 'C', 'D'],
            'B':['E', 'F'],
            'C':['G'],
            'G':['H'],
            'I':['Z']
        }
        self.assertTrue(path_bfs('A', 'H', graph))
        self.assertTrue(path_dfs('A', 'H', graph))
        self.assertTrue(path_dfs_r('A', 'H', graph))

        
if __name__ == '__main__':
    unittest.main()

