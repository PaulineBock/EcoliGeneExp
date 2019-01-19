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


def  makeHierarchicalTree(tree, node, cluster):
  #print node
  if cluster.numberOfSubGraphs() == 0:
    for clusterNode in cluster.getNodes():
      newLeaf = tree.addNode(clusterNode)
      tree.addEdge(newLeaf, node)
    
    
  for subgraphs in cluster.getSubGraphs():
    newChild = tree.addNode()
    print newChild
    tree.addEdge(newChild, node)
    return makeHierarchicalTree(tree, newChild, subgraphs)

    
'''
def makeHierarchicalAlgorithmRecursively(tree,root,graph):
  for i in range(graph.numberOfSubGraphs()):
    print i
    newNode=tree.addNode()
    root=tree.getSuperGraph()
#    print root
#    info=root.getNodes()
#    newEdge=graph.addEdge(newNode,info)
      
      
#  sub=graph.getSubGraph(0)
#  print sub
#  nbSub=graph.numberOfSubGraphs()
#  print nbSub
  '''

def main(graph): 
  
  rootGraph=graph.getRoot()
  tree=rootGraph.addSubGraph(name='Hierarchical Tree')
  topCluster = rootGraph.getDescendantGraph('Genes interactions')
  root = tree.addNode()
  makeHierarchicalTree(tree,root,topCluster)
