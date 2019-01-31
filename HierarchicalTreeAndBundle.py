# Powered by Python 2.7

#Tulip project, part 2, building hierarchical tree to change Genes Interactions graph topology.
#18-01-2019
#Pauline Bock, Guillaume Sotton

from tulip import tlp
from tulipgui import tlpgui


"""
Creates a hierarchical tree from genes interactions graph, giving a tree, a parent node and a cluster from genes interactions graph.
"""
def makeHierarchicalTree(tree, node, cluster):
  if cluster.numberOfSubGraphs() == 0:
    for clusterNode in cluster.getNodes():
      propertiesValues = cluster.getNodePropertiesValues(clusterNode)
      tree.addNode(clusterNode)
      tree.addEdge(node, clusterNode)
    return
    
  for subgraphs in cluster.getSubGraphs():
    newChild = tree.addNode()
    tree.addEdge(node, newChild)
    makeHierarchicalTree(tree, newChild, subgraphs)

"""
Changing graph layout to Tree Radial.
"""
def applyRadialLayout(tree):
  tree.applyLayoutAlgorithm('Tree Radial')

"""
Colors a graph according to a doubleProperty given.
"""
def colorMapping(graph, doubleProperty):
  params = tlp.getDefaultPluginParameters('Color Mapping', graph)
  params['input property'] = doubleProperty

  success = graph.applyColorAlgorithm('Color Mapping', params)

"""
Bundles edges of a graph according to a hierarchical tree, giving the tree and its root, the graph to change, their layout properties and shape property.
"""  
def bundleBuild(tree, geneInteractions, root, geneLayout, treeLayout, shape):
  for edge in geneInteractions.getEdges():
    srcToTargetPath = shortestPath(tree, geneInteractions.source(edge), geneInteractions.target(edge))
    edgeControlPoints(edge, srcToTargetPath, geneLayout)
  shape.setAllEdgeValue(16)

"""
Computes the shortest path between two nodes in the hierarchical tree and returns it.
"""
def shortestPath(tree, src, tgt):  
  sourcePath = findParents(tree, src)
  targetPath = findParents(tree, tgt)
  #Removes the root from one half path
  targetPath.pop(len(targetPath)-1)
  
  #Finds the common ancestors and deletes the parents of common ancestors
  for srcnode in sourcePath:
    for tgtnode in targetPath:
      if (srcnode == tgtnode):
        srcdeleted = sourcePath.pop(len(sourcePath)-1)
        tgtdeleted = targetPath.pop(len(targetPath) -1)
        while(srcdeleted!=srcnode and tgtdeleted!=tgtnode):
          srcdeleted = sourcePath.pop(len(sourcePath)-1)
          tgtdeleted = targetPath.pop(len(targetPath) -1)
         
        #Gets back the common ancestor        
        sourcePath.append(srcnode)
        targetPath.append(tgtnode)
        
  targetPath.reverse()
  sourcePath = sourcePath + targetPath
  return sourcePath

"""
Returns a path containing visited nodes during tree traversal from a node to the root of the tree.
"""
def findParents(tree, node):
  path = []
  return inferiorLevel(tree, node, path)

"""
Recursively tree traversal, adding nodes visited into a reteurned path, giving the tree to travel in, node visited, and the path list.
"""
def inferiorLevel(tree, node, path):
  for parent in tree.getInNodes(node):
    path.append(parent)
    inferiorLevel(tree, parent, path)
  return path

"""
Gives to a graph edge the positions of the nodes in the hierarchical tree path between the source and target nodes of this edge.
Giving the edge, the path between the edge bounds, and genes interactions layout property.
"""
def edgeControlPoints(edge, path, geneLayout):
  nodePos = []
  for node in path:
    nodePos.append(geneLayout[node])
  geneLayout.setEdgeValue(edge, nodePos)
  
  
def main(graph): 
  
  rootGraph=graph.getRoot()
  tree=rootGraph.addSubGraph(name='Hierarchical Tree')
  geneInteractions = rootGraph.getDescendantGraph('Genes interactions')
  
  geneLayout = geneInteractions.getLayoutProperty("viewLayout")
  treeLayout = tree.getLayoutProperty("viewLayout")
  viewShape = geneInteractions.getIntegerProperty("viewShape")
  tp1_s = graph.getDoubleProperty("tp1 s")
  
  root = tree.addNode()
  makeHierarchicalTree(tree,root,geneInteractions)
  applyRadialLayout(tree) 
  colorMapping(tree, tp1_s)
  bundleBuild(tree, geneInteractions, root, geneLayout, treeLayout, viewShape)

  nodeLinkTreeView = tlpgui.createView("Node Link Diagram view", tree, dataSet = {}, show=True)
  glGraphRenderingParams = nodeLinkTreeView.getRenderingParameters()
  glGraphRenderingParams.setEdgeColorInterpolate(False)
