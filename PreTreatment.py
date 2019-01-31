# Powered by Python 2.7

#Tulip project, part 1, visualisation and pre-processing of data
#18-01-2019
#Pauline Bock, Guillaume Sotton

from tulip import tlp
from tulipgui import tlpgui

  
"""
Initializes position of the graph and change nodes size, giving a graph, viewSize and viewLayout property.
"""
def initLayout(graph, size, layout):  
  new_size = tlp.Size(1.0,1.0,1.0)
  size.setAllNodeValue(new_size, graph)
  
  graph.applyLayoutAlgorithm('Circular', layout)
 
"""
Initializes labels, giving label properties, locus property and a graph.
"""
def initLabels(graph, locus, label, labelBorderWidth, labelPosition):
  params=tlp.getDefaultPluginParameters('To labels',graph)
  params['input'] = locus
  graph.applyStringAlgorithm('To labels',label ,params)
  
  labelBorderWidth.setAllNodeValue(0)

  center = 0
  labelPosition.setAllNodeValue(center)
  
"""
Colors edges according to negative and positive regulation properties of a graph, giving these lasts, a graph, and color property."
"""
def initEdges(graph, negative, positive, color):
  red = tlp.Color(255,0,0)
  green = tlp.Color(0,255,0)
  darkBlue = tlp.Color(0,0,80)
  orange = tlp.Color(255,150,0)
  
  for e in graph.getEdges():
    if (negative[e] == True and positive[e] == False):
      color.setEdgeValue(e, red)
    if (negative[e] == False and positive[e] == True):
      color.setEdgeValue(e, green)
    if (negative[e] == False and positive[e] == False):
      color.setEdgeValue(e, darkBlue)
    if (negative[e] == True and positive[e] == True):
      color.setEdgeValue(e, orange)
      
  
def main(graph): 
  negative = graph.getBooleanProperty("Negative")
  positive = graph.getBooleanProperty("Positive")
  locus = graph.getStringProperty("locus")
  color = graph.getColorProperty("viewColor")
  label = graph.getStringProperty("viewLabel")
  labelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  labelColor = graph.getColorProperty("viewLabelColor")
  labelPosition = graph.getIntegerProperty("viewLabelPosition")
  layout = graph.getLayoutProperty("viewLayout")
  size = graph.getSizeProperty("viewSize")
  
  genesInteractions = graph.getDescendantGraph("Genes interactions")
  initLayout(genesInteractions, size, layout)
  initLabels(genesInteractions, locus, label, labelBorderWidth, labelPosition)
  initEdges(genesInteractions, negative, positive, color)
  nodeLinkView = tlpgui.createView("Node Link Diagram view", genesInteractions, dataSet = {}, show=True)
  glGraphRenderingParams = nodeLinkView.getRenderingParameters()
  glGraphRenderingParams.setEdgeColorInterpolate(False)
  
