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
      tree.addEdge(clusterNode, node)
    return
    
  for subgraphs in cluster.getSubGraphs():
    newChild = tree.addNode()
    tree.addEdge(newChild, node)
    makeHierarchicalTree(tree, newChild, subgraphs)

def applyRadialLayout(tree):
  #Changing layout
  tree.applyLayoutAlgorithm('Tree Radial')
  
def colorMapping(graph, doubleProperty):
  params = tlp.getDefaultPluginParameters('Color Mapping', graph)
  params['input property'] = doubleProperty

  success = graph.applyColorAlgorithm('Color Mapping', params)

def bundleBuild(tree, gene, root):
  print root
  print "root " + str(root)
  for edge in gene.getEdges():
    print "source "+ str(gene.source(edge)) + "   edge  " + str(gene.target(edge))
    srcpath = [ gene.source(edge)]
    sourcePath = depthFirstSearch(tree, root, gene.source(edge), srcpath)
    #targetPath = depthFirstSearch(tree, root, gene.target(edge))
    #print sourcePath
    #print targetPath    
    
def depthFirstSearch(tree, root, target, path):
  if target == root:
    return path
  
  for child in tree.getInNodes(target):
    path.append(child)
    depthFirstSearch(tree, root, child)
   
  print path
  
def buildSmallMultiples(smallMultiplesTree,graph,timepoints):
  for i in range(1,len(timepoints)+1):
    tp=smallMultiplesTree.addSubGraph("tp"+str(i)+"_s")
    inGraph=graph.getSubGraph("Genes interactions")
    tlp.copyToGraph(tp,inGraph, inSelection=None, outSelection=None)
  
  property1=smallMultiplesTree.getDoubleProperty("viewMetric")
  property2=smallMultiplesTree.getDoubleProperty("tp1 s")  
  property1=property2
  
    
def main(graph): 
  tp1_s = graph.getDoubleProperty("tp1 s")
  tp10_s = graph.getDoubleProperty("tp10 s")
  tp11_s = graph.getDoubleProperty("tp11 s")
  tp12_s = graph.getDoubleProperty("tp12 s")
  tp13_s = graph.getDoubleProperty("tp13 s")
  tp14_s = graph.getDoubleProperty("tp14 s")
  tp15_s = graph.getDoubleProperty("tp15 s")
  tp16_s = graph.getDoubleProperty("tp16 s")
  tp17_s = graph.getDoubleProperty("tp17 s")
  tp2_s = graph.getDoubleProperty("tp2 s")
  tp3_s = graph.getDoubleProperty("tp3 s")
  tp4_s = graph.getDoubleProperty("tp4 s")
  tp5_s = graph.getDoubleProperty("tp5 s")
  tp6_s = graph.getDoubleProperty("tp6 s")
  tp7_s = graph.getDoubleProperty("tp7 s")
  tp8_s = graph.getDoubleProperty("tp8 s")
  tp9_s = graph.getDoubleProperty("tp9 s")
  timepoints=[tp1_s,tp10_s,tp11_s,tp12_s,tp13_s,tp14_s,tp15_s,tp16_s,tp17_s,tp2_s,tp3_s,tp4_s,tp5_s,tp6_s,tp7_s,tp8_s,tp9_s]
  size = graph.getSizeProperty("viewSize")
  color = graph.getColorProperty("viewColor")
  label = graph.getStringProperty("viewLabel")
  shape = graph.getIntegerProperty("viewShape")
  layout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  rootGraph=graph.getRoot()
  tree=rootGraph.addSubGraph(name='Hierarchical Tree')
  geneInteractions = rootGraph.getDescendantGraph('Genes interactions')
  root = tree.addNode()
  makeHierarchicalTree(tree,root,geneInteractions)
  applyRadialLayout(tree)
  tp1_s = graph.getDoubleProperty("tp1 s")
  colorMapping(tree, tp1_s)
  print root
  bundleBuild(tree, geneInteractions, root)
  
  #Partie 3
  smallMultiplesTree=rootGraph.addSubGraph(name='Small Multiples')
  buildSmallMultiples(smallMultiplesTree,graph,timepoints)

