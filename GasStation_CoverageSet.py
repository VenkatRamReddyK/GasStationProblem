from collections import namedtuple
import operator

def writesetstofile(set):
    name="output.txt";    
    with open(name, 'w') as f:
        for item in set:
            f.write("{}x".format(item))        

def printSolSet():
    print "Solution set: ";
    for item in solSet:
        print (item,)
        
def printDict():
    for (item,edgelist) in inputdict.items():
        print item,edgelist
        
def getNeighbours(edgelist):# returns neighbours with sorted weight parsed from input file 
    namedNeighbours=[]
    tupleneighbours=[]
    j=0
    for edge in edgelist.split(','):
            if(int(edge)>0 and int(edge)<=k): 
                neighbour=Neighbour(edge=j,weight=int(edge))  # 2:[3:6,5:4,7:3]
                namedNeighbours.append(neighbour)#(j,int(edge))                            
            j=j+1
    namedNeighbours.sort(key=lambda x:x.weight)
    for neighbour in namedNeighbours:            
        tupleneighbours.append((neighbour.edge,neighbour.weight))# [(7,3),(5,4),(3,6)]
    return tupleneighbours                                         

def readFromFile(filename,k):
    inputfile=open(filename,"r");
    input=inputfile.read();
    inputlist=input.rstrip("x").split("x"); # splits input ( set of edgelist seperated by x    
    i=0    
    for edgelist in inputlist: # for each vertex populate edge list        
        neighbours=[]    # neighbours for vertex i  
        neighbours=getNeighbours(edgelist)
        inputdict[i]=neighbours        
        i=i+1;                        
                       
# finding next minimum vertex to be added to the covered list                                       
def nextTraversingVertex(coveredDict):
    final_minW=10000
    final_minV=-1
    final_minPV=-1
    for (parent_V,parent_W) in coveredDict.items():#finding minimum vertex for each covered vertex 
        t_MinW=900000
        t_MinV=-1
        t_MinPV=-1
        if parent_V in inputdict:
# For current parent we are finding the a current vertex which has minimum weight
# optimize this step             
            for (current_V,current_W) in inputdict[parent_V]:
                if(not coveredDict.has_key(current_V) and int(current_W+parent_W)<=k):
                    (t_MinV,t_MinPV,t_MinW)=(current_V,parent_V,current_W+parent_W) # total weight of current vertex;
                    break # found the minimum vertex                             
            if t_MinW < final_minW: 
                (final_minV,final_minPV,final_minW)=(t_MinV,t_MinPV,t_MinW) # finalizing the minimum vertex, to be traversed next
    return (final_minV,final_minPV,final_minW)

def primsAlgorithm(_sourceVertex):
    coveredEdgeList={}
    coveredDict={}
    _minweight=100000;
    _minvertex=0    
    currentIndex=0
    coveredDict[_sourceVertex]=0 # adding first node to covered dictionary
    nextV=200000
    nextPV=100000
    nextW=-1
    
    while len(coveredDict) < len(inputdict):
        (nextV,nextPV,nextW)=nextTraversingVertex(coveredDict)        
        if nextV ==-1:
            break
        print "next vertex to be added: ",nextV
        coveredDict[nextV]=nextW
        # adding a newly added vertex to parent vertex 
        if coveredEdgeList.has_key(nextV):
            coveredEdgeList[nextV].extend([nextPV])
        else:
            coveredEdgeList[nextV]=[nextPV]       
        # adding parent vertex to vertex    
        if coveredEdgeList.has_key(nextPV):
            coveredEdgeList[nextPV].extend([nextV])
        else:
            coveredEdgeList[nextPV]=[nextV]
                                
        currentIndex=currentIndex+1        
    return coveredDict.keys()


k=50;
INPUTFILENAME="graph_final.txt"
Neighbour = namedtuple("Neighbour", ["edge", "weight"])

inputdict={};
readFromFile(INPUTFILENAME,k);
# printDict();
vertexCover=0
coverDict={}
while vertexCover<len(inputdict):
    print "- - - - Prims Algorithm for vertex :",vertexCover,"- - - - "
    maxcoverset=primsAlgorithm(vertexCover)
#     print "max cover set for vertex : ",vertexCover,": ",maxcoverset
    coverDict[vertexCover]=maxcoverset
    vertexCover=vertexCover+1

# print "cover dict: old"
for vertex,list in  coverDict.items():
#     print vertex, list
    list.remove(vertex)

# print "cover dict: "
# for vertex,list in  coverDict.items():
#     print vertex, list

solSet=[]

while len(coverDict)>0:
    print "- - - - - - -- - -  iteration ",len(solSet),"- - - - - -"
    maxCover=-1
    removalvertex=-1
    
    for vertex,list in  coverDict.items():
        
        if maxCover< len(list):
            maxCover = len(list)
            removalvertex=vertex
            
    if removalvertex!=-1:
        if removalvertex in coverDict:
            removallist=coverDict[removalvertex]
            # removing the neighbour of mac count vertex
            for _rv in removallist:
                if _rv in coverDict and _rv !=removalvertex:
#                     print " - removing the neighbour of [ ",removalvertex," ] : i.e ",_rv
                    del coverDict[_rv]
            # removing the max cover vertex        
            if removalvertex in coverDict:
#                 print "- - Removing  Mac Count vertex: ",removalvertex,coverDict[removalvertex]
                del coverDict[removalvertex]                
                solSet.append(removalvertex)
                
            # removing the neighbour from other coverage set
            for _vertex,_edgelist in coverDict.iteritems():                
#                 print "removing these vertices in all other vertices ",coverDict[removalvertex]
                for _removeEdge in _edgelist:                    
                    if _removeEdge in removallist:
#                         print "Vertex ",_vertex,":  edge list ",coverDict[_vertex]
#                         print "- - - removing neighbour's - -  ",_vertex,"- removing the edge -[ ",_removeEdge," ] "
                        coverDict[_vertex].remove(_removeEdge)
                                
#     print "cover dict: "
#     print coverDict

print "Solution set size"
print len(solSet)
# print solSet
writesetstofile(solSet)



     