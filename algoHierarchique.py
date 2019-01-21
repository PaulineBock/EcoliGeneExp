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
    makeHierarchicalTree(tree, newChild, subgraphs, cpt)
    

    
def main(graph): 
  
  rootGraph=graph.getRoot()
  tree=rootGraph.addSubGraph(name='Hierarchical Tree')
  topCluster = rootGraph.getDescendantGraph('Genes interactions')
  root = tree.addNode()
  makeHierarchicalTree(tree,root,topCluster)

