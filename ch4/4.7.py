# [4.7] Build Order: You are given a list of projects and
# a list of dependencies (which is a list of pairs of projects,
# where the second project is dependent on the first project).
# All of a project's dependencies must be built before the 
# project is. Find a build order that will allow the projects
# to be built. If there is no valid build order, return an
# error.

# Input:
#   projects: a, b, c, d, e, f
#   dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

# Output: f, e, a, b, d, c

import unittest


def find_build_order(projects, dependencies):
    build_order = []
    project_graph = create_graph(projects, dependencies)

    while project_graph:
        projects_with_depen = get_projects_with_dependencies(project_graph)
        projects_wo_depen = get_projects_wo_dependencies(
            projects_with_depen, 
            project_graph
        )

        if len(projects_wo_depen) == 0 and project_graph:
            raise ValueError('There is a cycle in the build order')

        for independent_project in projects_wo_depen:
            build_order.append(independent_project)
            del project_graph[independent_project]

    return build_order

def get_projects_with_dependencies(graph):
    projects_with_depen = set()
    for project in graph:
        projects_with_depen = projects_with_depen.union(set(graph[project]))
    
    return projects_with_depen

def get_projects_wo_dependencies(projects_with, graph):
    projects_wo_dependencies = set()

    for project in graph:
        if not project in projects_with:
            projects_wo_dependencies.add(project)

    return projects_wo_dependencies

def create_graph(projects, dependencies):
    project_graph = {}

    for project in projects:
        project_graph[project] = []

    for pairs in dependencies:
        project_graph[pairs[0]].extend(pairs[1])
    return project_graph


class Test(unittest.TestCase):

    def setUp(self):
        self.projects = ['A', 'B', 'C', 'D', 'E', 'F']
        self.dependencies = [('A','D'), ('F', 'B'), ('B','D'), ('F','A'), ('D','C')]

        self.projects2 = ['A', 'B', 'C']
        self.dependencies2 = [('B','A'), ('C','B'), ('A','C')]
    
    #@unittest.skip("next step")
    def test_find_build_order(self):
        build = find_build_order(self.projects, self.dependencies)
        self.assertEqual(set(build[0:2]), set(['E','F']))
        self.assertEqual(set(build[2:4]), set(['A','B']))
        self.assertEqual(build[4], 'D')
        self.assertEqual(build[5], 'C')
        self.assertRaises(
            ValueError, 
            find_build_order, 
            self.projects2,
            self.dependencies2
        )

    def test_create_graph(self):
        graph = create_graph(self.projects, self.dependencies)
        self.assertEqual(set(graph.keys()), set(self.projects))
        self.assertEqual(set(graph['F']), set(['A','B']))

    def test_get_projects_with_dependencies(self):
        graph = {
            'A': ['D'], 
            'C': [], 
            'B': ['D'], 
            'E': [], 
            'D': ['C'], 
            'F': ['B', 'A']
        }
        self.assertEqual(
            get_projects_with_dependencies(graph),
            set(['A','B','C','D'])
        )

    def test_get_projects_wo_dependencies(self):
        graph = {
            'A': ['D'], 
            'C': [], 
            'B': ['D'], 
            'E': [], 
            'D': ['C'], 
            'F': ['B', 'A']
        }
        project_with = set(['A','B','C','D'])
        self.assertEqual(
            get_projects_wo_dependencies(project_with, graph),
            set(['F','E'])
        )
        
if __name__ == '__main__':
    unittest.main()

