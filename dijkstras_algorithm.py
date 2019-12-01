import copy

class Dijkstra:
    def __init__(self,nodes={}):
        self.nodes = nodes
    def addNode(self,name,neighbors):
        self.nodes[name]=neighbors
    def go(self,beginning,destination):
        
        # initialize paths
        paths = {}
        for node in self.nodes.keys():
            if node == beginning:
                paths[node]=[0,[]]
            else:
                paths[node]=["inf",[]]
        
        newPaths = []
        iteration = 0
        theStr=" ,"
        for node in nodes.keys():
            theStr+=node+","
        theStr+="\n"
        while newPaths != paths:
            theStr+=str(iteration+1)+","
            iteration+=1
            if iteration == 1: newPaths = copy.deepcopy(paths)
            paths = copy.deepcopy(newPaths)
            for node in paths.keys():
                neighbors = self.nodes[node]
                neighborNames = list(neighbors.keys())
                for neighbor in neighborNames:
                    if paths[neighbor][0] != 'inf':
                        distFromNeighbor = neighbors[neighbor]
                        distToNeighborFromOrigin = paths[neighbor][0]
                        if newPaths[node][0] != 'inf':
                            if distFromNeighbor + distToNeighborFromOrigin < newPaths[node][0]:
                                newPaths[node][0] = distFromNeighbor + distToNeighborFromOrigin
                                newPaths[node][1] = copy.deepcopy(paths[neighbor][1]) + [neighbor]
                        else:
                            newPaths[node][0] = copy.deepcopy(distFromNeighbor + distToNeighborFromOrigin)
                            newPaths[node][1] = copy.deepcopy(paths[neighbor][1]) + [neighbor]
            print("steps: " + str(iteration))
            for node in newPaths.keys():
                newEntry = str(newPaths[node][0])+str(newPaths[node][1])
                newEntry = newEntry.replace(",","").replace("'","")
                theStr+=newEntry+","
                print(str(node)+":"+str(newPaths[node][0])+str(newPaths[node][1]),end = "; ")
            input("\n")
            theStr+="\n"
        with open("result.csv","w+") as f:
            f.write(theStr)


if __name__ == '__main__':
    # nodes = [Node('a', {'b':2,'c':3}),
             # Node('b', {'a':2,'d':5,'e':2}),
             # Node('c', {'a':3,'e':5}),
             # Node('d', {'b':5,'e':1,'z':2}),
             # Node('e', {'b':2,'c':5,'d':1,'z':4}),
             # Node('z', {'d':2,'e':4})]
    # nodes = {'a': {'b':2,'c':3},
             # 'b': {'a':2,'d':5,'e':2},
             # 'c': {'a':3,'e':5},
             # 'd': {'b':5,'e':1,'z':2},
             # 'e': {'b':2,'c':5,'d':1,'z':4},
             # 'z': {'d':2,'e':4}}
    nodes = {'a': {'b':2,'d':1},
             'b': {'a':2,'c':3,'e':1},
             'c': {'a':4,'b':3,'e':2,'f':2},
             'd': {'a':1,'f':5,'g':4},
             'e': {'b':1,'c':2,'h':3},
             'f': {'c':2,'d':5,'g':3,'h':3,'i':2,'j':4},
             'g': {'d':4,'f':3,'k':2},
             'h': {'e':3,'f':3,'l':1,'o':8},
             'i': {'f':2,'j':3,'l':3,'m':2},
             'j': {'f':4,'i':3,'k':6,'m':6,'n':3},
             'k': {'g':2,'j':6,'n':4,'r':2},
             'l': {'h':1,'i':3,'m':3,'o':6},
             'm': {'i':2,'j':6,'l':3,'n':5,'o':4,'p':2},
             'n': {'j':3,'k':4,'m':5,'q':2,'r':1},
             'o': {'h':8,'l':6,'m':4,'p':2,'s':6},
             'p': {'m':2,'o':2,'q':1,'s':2,'t':1},
             'q': {'n':2,'p':1,'r':8,'t':3},
             'r': {'k':2,'n':1,'q':8,'t':5},
             's': {'o':6,'p':2,'z':2},
             't': {'p':1,'q':3,'r':5,'z':8},
             'z': {'s':2,'t':8}}
    a=Dijkstra(nodes)
    a.go('a','z')
