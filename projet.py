# Powered by Python 2.7

#Tulip project, part 1, visualisation and pre-processing of data
#18-01-2019
#Pauline Bock, Guillaume Sotton


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
from tulipgui import tlpgui

# The updateVisualization(centerViews = True) function can be called
# during script execution to update the opened views
# The pauseScript() function can be called to pause the script execution.
# To resume the script execution, you will have to click on the "Run script " button.

# The runGraphScript(scriptFile, graph) function can be called to launch
# another edited script on a tlp.Graph object.
# The scriptFile parameter defines the script name to call (in the form [a-zA-Z0-9_]+.py)

# The main(graph) function must be defined 
# to run the script on the current graph

#Partie 1 : Pre-traitement
  
'''
@params :
'''
def initLayout(graph, size, layout):
  
  #Changing size
  new_size = tlp.Size(1.0,1.0,1.0)
  size.setAllNodeValue(new_size, graph)
  
  #Changing layout
  graph.applyLayoutAlgorithm('Circular', layout)
 
'''
@params :
'''
def initLabels(graph, locus, label, labelColor, labelBorderWidth, labelPosition):
  
  #Applying and changing labels
  params=tlp.getDefaultPluginParameters('To labels',graph)
  params['input'] = locus
  graph.applyStringAlgorithm('To labels',label ,params)
  
  white = tlp.Color(255,255,255)
  labelColor.setAllNodeValue(white, graph)
  
  labelBorderWidth.setAllNodeValue(0)

  center = 0
  labelPosition.setAllNodeValue(center)
  
  
'''
@params :

'''
def initEdges(graph, negative, positive, color):
  red = tlp.Color(255,0,0)
  green = tlp.Color(0,255,0)
  darkblue = tlp.Color(0,0,80)
  orange = tlp.Color(255,150,0)
  
  for e in graph.getEdges():
    #render.setEdgeColorInterpolate(False)
    if (negative[e] == True and positive[e] == False):
      color.setEdgeValue(e, red)
    if (negative[e] == False and positive[e] == True):
      color.setEdgeValue(e, green)
    if (negative[e] == False and positive[e] == False):
      color.setEdgeValue(e, darkblue)
    if (negative[e] == True and positive[e] == True):
      color.setEdgeValue(e, orange)
      
  
 

  

  
def main(graph): 
  negative = graph.getBooleanProperty("Negative")
  positive = graph.getBooleanProperty("Positive")
  locus = graph.getStringProperty("locus")
  similarity = graph.getDoubleProperty("similarity")
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
  viewBorderColor = graph.getColorProperty("viewBorderColor")
  viewBorderWidth = graph.getDoubleProperty("viewBorderWidth")
  color = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewIcon = graph.getStringProperty("viewIcon")
  label = graph.getStringProperty("viewLabel")
  viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
  labelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  labelColor = graph.getColorProperty("viewLabelColor")
  labelPosition = graph.getIntegerProperty("viewLabelPosition")
  layout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  viewRotation = graph.getDoubleProperty("viewRotation")
  viewSelection = graph.getBooleanProperty("viewSelection")
  shape = graph.getIntegerProperty("viewShape")
  size = graph.getSizeProperty("viewSize")
  viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
  viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
  viewTexture = graph.getStringProperty("viewTexture")
  viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
  viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")
  

  initLayout(graph, size, layout)
  initLabels(graph, locus, label, labelColor, labelBorderWidth, labelPosition)
  initEdges(graph, negative, positive, color)

  
