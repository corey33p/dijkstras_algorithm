import copy

class Node:
    def __init__(self,name,neighbors):
        # neighbor = {name: distance,...}
        self.neighbors = neighbors
        self.name = name

class Dijkstra:
    def __init__(self,nodes=[]):
        self.nodes = nodes
    def addNode(self,newNode):
        self.nodes.append(newNode)
    def go(self,beginning,destination):
        
        # initialize paths
        paths = {}
        for node in self.nodes:
            if node.name == beginning:
                paths[node.name]=[node,0,[]]
            else:
                paths[node.name]=[node,"inf",[]]
        
        newPaths = []
        iteration = 0
        while newPaths != paths:
            iteration+=1
            if iteration == 1: newPaths = copy.deepcopy(paths)
            paths = copy.deepcopy(newPaths)
            for node in paths.keys():
                neighbors = newPaths[node][0].neighbors
                neighborNames = list(neighbors.keys())
                for neighbor in neighborNames:
                    if paths[neighbor][1] != 'inf':
                        distFromNeighbor = neighbors[neighbor]
                        distToNeighborFromOrigin = paths[neighbor][1]
                        if newPaths[node][1] != 'inf':
                            if distFromNeighbor + distToNeighborFromOrigin < newPaths[node][1]:
                                newPaths[node][1] = distFromNeighbor + distToNeighborFromOrigin
                                newPaths[node][2] = copy.deepcopy(paths[neighbor][2]) + copy.deepcopy([paths[neighbor][0].name])
                        else:
                            newPaths[node][1] = copy.deepcopy(distFromNeighbor + distToNeighborFromOrigin)
                            newPaths[node][2] = copy.deepcopy(paths[neighbor][2]) + copy.deepcopy([paths[neighbor][0].name])
            print("steps: " + str(iteration))
            for node in newPaths.keys():
                print(str(node)+":"+str(newPaths[node][1])+str(newPaths[node][2]),end = "; ")
            input("\n")
            

if __name__ == '__main__':
    nodes = [Node('a', {'b':2,'c':3}),
             Node('b', {'a':2,'d':5,'e':2}),
             Node('c', {'a':3,'e':5}),
             Node('d', {'b':5,'e':1,'z':2}),
             Node('e', {'b':2,'c':5,'d':1,'z':4}),
             Node('z', {'d':2,'e':4})]
    a=Dijkstra(nodes)
    a.go('a','z')
