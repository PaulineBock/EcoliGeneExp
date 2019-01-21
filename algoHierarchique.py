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
      newLeaf = tree.addNode(propertiesValues)
      tree.addEdge(newLeaf, node)
    print "leaves added"
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

def bundleBuild(tree, gene):
  for edge in gene.getEdges():
    src =  gene.source(edge)
    tgt = gene.target(edge)
    srcPath = tlp.dfs(tree, src)
    tgtPath = tlp.dfs(tree, tgt)
    print str(src) + "  to  " + str(tgt)
    print "src path" + str(srcPath[0]) + str(srcPath[len(srcPath)-1])
    print "tgt path" + str(tgtPath[0]) + str(tgtPath[len(tgtPath)-1])
    
def main(graph): 
  '''
  rootGraph=graph.getRoot()
  tree=rootGraph.addSubGraph(name='Hierarchical Tree')
  topCluster = rootGraph.getDescendantGraph('Genes interactions')
  root = tree.addNode()
  makeHierarchicalTree(tree,root,topCluster)
  applyRadialLayout(tree)
  tp1_s = graph.getDoubleProperty("tp1 s")
  colorMapping(tree, tp1_s)'''
  rootGraph=graph.getRoot()
  tree=rootGraph.getDescendantGraph('Hierarchical tree')
  geneInteractions=rootGraph.getDescendantGraph('Genes interactions')
  bundleBuild(tree, geneInteractions)

