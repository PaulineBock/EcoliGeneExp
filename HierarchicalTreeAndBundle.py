# Powered by Python 2.7

# To cancel the modifications performed by the script
# on the current graph, click on the undo button.

# Some useful keyboards shortcuts : 
#   * Ctrl + D : comment selected lines.
#   * Ctrl + Shift + D  : uncomment selected lines.
#   * Ctrl + I : indent selected lines.
#   * Ctrl + Shift + I  : unindent selected lines.
#   * Ctrl + Return  : run script.
#   * Ctrl + F  : find selected text.
#   * Ctrl + R  : replace selected text.
#   * Ctrl + Space  : show auto-completion dialog.

from tulip import tlp

# The updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views

# The pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# The runGraphScript(scriptFile, graph) function can be called to launch
# another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# The main(graph) function must be defined 
# to run the script on the current graph


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

def applyRadialLayout(tree):
  #Changing layout
  tree.applyLayoutAlgorithm('Tree Radial')
  
def colorMapping(graph, doubleProperty):
  params = tlp.getDefaultPluginParameters('Color Mapping', graph)
  params['input property'] = doubleProperty

  success = graph.applyColorAlgorithm('Color Mapping', params)

def bundleBuild(tree, gene, root, geneLayout, treeLayout, shape):
  for edge in gene.getEdges():
    srcToTargetPath = shortestPath(tree, gene.source(edge), gene.target(edge))
    edgeControlPoints(tree, edge, srcToTargetPath, geneLayout, treeLayout)
  shape.setAllEdgeValue(16)
  
    
def edgeControlPoints(tree, edge, path, geneLayout, treeLayout):
  nodePos = []
  for node in path:
    nodePos.append(geneLayout[node])
  geneLayout.setEdgeValue(edge, nodePos)
  
def shortestPath(tree, src, tgt):
  
  sourcePath = findParents(tree, src)
  targetPath = findParents(tree, tgt)
  targetPath.pop(len(targetPath)-1)
  
  #Find the common ancestors and delete the parents of common ancestors
  for srcnode in sourcePath:
    for tgtnode in targetPath:
      if (srcnode == tgtnode):
        srcdeleted = sourcePath.pop(len(sourcePath)-1)
        tgtdeleted = targetPath.pop(len(targetPath) -1)
        while(srcdeleted!=srcnode and tgtdeleted!=tgtnode ):
          srcdeleted = sourcePath.pop(len(sourcePath)-1)
          tgtdeleted = targetPath.pop(len(targetPath) -1)
                 
        sourcePath.append(srcnode)
        targetPath.append(tgtnode)
        
  
  targetPath.reverse()
  sourcePath = sourcePath + targetPath
  return sourcePath
  
def findParents(tree, node):
  path = []
  return inferiorLevel(tree, node, path)
 
def inferiorLevel(tree, node, path):
  for parent in tree.getInNodes(node):
    path.append(parent)
    inferiorLevel(tree, parent, path)
  return path
   
    
def main(graph): 
  
  rootGraph=graph.getRoot()
  tree=rootGraph.addSubGraph(name='Hierarchical Tree')
  geneInteractions = rootGraph.getDescendantGraph('Genes interactions')
  
  geneLayout = geneInteractions.getLayoutProperty("viewLayout")
  treeLayout = tree.getLayoutProperty("viewLayout")
  viewShape = geneInteractions.getIntegerProperty("viewShape")
  root = tree.addNode()
  makeHierarchicalTree(tree,root,geneInteractions)
  applyRadialLayout(tree)
  tp1_s = graph.getDoubleProperty("tp1 s")
  colorMapping(tree, tp1_s)
  print root
  bundleBuild(tree, geneInteractions, root, geneLayout, treeLayout, viewShape)

