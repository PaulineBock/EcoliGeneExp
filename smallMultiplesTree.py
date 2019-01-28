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

def buildSmallMultiples(smallMultiplesTree,geneInteractions,timepoints,metric):
  for i in range(1,len(timepoints)+1):
    tp=smallMultiplesTree.addSubGraph("tp"+str(i)+" s")
  
    inGraph=graph.getSubGraph("Genes interactions")
    tlp.copyToGraph(tp,inGraph, inSelection=None, outSelection=None)
#    metric = tp.getLocalDoubleProperty("viewMetric")
  for time in timepoints:
    for sg in smallMultiplesTree.getSubGraphs():
      metric = sg.getLocalDoubleProperty("viewMetric")
      for n in sg.getNodes():
        timePropertyName = str(time).split(" ")
        timeName = timePropertyName[2]+" s"
        if(timeName == sg.getName()):
          metric[n] = time[n]

def colorMapping(graph, doubleProperty):
  params = tlp.getDefaultPluginParameters('Color Mapping', graph)
  params['input property'] = doubleProperty
      
def colorSmallMultiples(smallMultiplesTree,metric):
  for sg in smallMultiplesTree.getSubGraphs():
    params = tlp.getDefaultPluginParameters('Color Mapping', sg)
    colorScale = tlp.ColorScale([])
    newColors = [tlp.Color.Green, tlp.Color.Black,tlp.Color.Red]
    colorScale.setColorScale(newColors,True)
    params['color scale'] = colorScale
    sg.applyColorAlgorithm('Color Mapping',params)

def placeSmallMultiples(smallMultiplesTree, nbCol):
  bb = tlp.computeBoundingBox(smallMultiplesTree)
  xmin = bb[0][0]
  xmax = bb[1][0]
  ymin = bb[0][1]
  ymax = bb[1][1]
  
  smallLayout = smallMultiplesTree.getLayoutProperty("viewLayout")
  for sg in smallMultiplesTree.getSubGraphs():
    sgNames = sg.getName().split(" ")
    sgName = sgNames[0]
    nbSG = int(sgName[2:len(sgName)])
    print nbSG
    if (nbSG <= nbCol):
      for node in sg.getNodes():
        newPos = tlp.Coord(smallLayout[node][0] + xmax * nbSG, smallLayout[node][1], smallLayout[node][2])
        smallLayout.setNodeValue(node, newPos)  
      newEdgePos = []
      for edge in sg.getEdges():
        for pos in smallLayout[edge]: 
          newPos = tlp.Coord(pos[0] + xmax * nbSG, pos[1], pos[2])
          newEdgePos.append(newPos)
        smallLayout.setEdgeValue(edge, newEdgePos)  

    if (nbSG <= nbCol* 2 and nbSG > nbCol):
      for node in sg.getNodes():
        newPos = tlp.Coord(smallLayout[node][0] + xmax * (nbSG - nbCol), smallLayout[node][1] - ymax, smallLayout[node][2])
        smallLayout.setNodeValue(node, newPos)  
      newEdgePos = []
      for edge in sg.getEdges():
        for pos in smallLayout[edge]: 
          newPos = tlp.Coord(pos[0] + xmax * (nbSG - nbCol) , pos[1] -ymax , pos[2])
          newEdgePos.append(newPos)
        smallLayout.setEdgeValue(edge, newEdgePos)  
        
    if (nbSG <= nbCol*3 and nbSG > nbCol * 2):
      for node in sg.getNodes():
        newPos = tlp.Coord(smallLayout[node][0] + xmax * (nbSG - nbCol*2), smallLayout[node][1] - ymax*2, smallLayout[node][2])
        smallLayout.setNodeValue(node, newPos)  
      newEdgePos = []
      for edge in sg.getEdges():
        for pos in smallLayout[edge]: 
          newPos = tlp.Coord(pos[0] + xmax * (nbSG - nbCol*2) , pos[1] - ymax*2 , pos[2])
          newEdgePos.append(newPos)
        smallLayout.setEdgeValue(edge, newEdgePos)  
        
    if (nbSG <= nbCol*4 and nbSG > nbCol * 3):
      for node in sg.getNodes():
        newPos = tlp.Coord(smallLayout[node][0] + xmax * (nbSG - nbCol*3), smallLayout[node][1] - ymax*3, smallLayout[node][2])
        smallLayout.setNodeValue(node, newPos)  
      newEdgePos = []
      for edge in sg.getEdges():
        for pos in smallLayout[edge]: 
          newPos = tlp.Coord(pos[0] + xmax * (nbSG - nbCol*3) , pos[1] - ymax*3 , pos[2])
          newEdgePos.append(newPos)
        smallLayout.setEdgeValue(edge, newEdgePos)  
      

def main(graph): 
  Locus = graph.getStringProperty("Locus")
  Negative = graph.getBooleanProperty("Negative")
  Positive = graph.getBooleanProperty("Positive")
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
  viewColor = graph.getColorProperty("viewColor")
  viewFont = graph.getStringProperty("viewFont")
  viewFontSize = graph.getIntegerProperty("viewFontSize")
  viewIcon = graph.getStringProperty("viewIcon")
  viewLabel = graph.getStringProperty("viewLabel")
  viewLabelBorderColor = graph.getColorProperty("viewLabelBorderColor")
  viewLabelBorderWidth = graph.getDoubleProperty("viewLabelBorderWidth")
  viewLabelColor = graph.getColorProperty("viewLabelColor")
  viewLabelPosition = graph.getIntegerProperty("viewLabelPosition")
  viewLayout = graph.getLayoutProperty("viewLayout")
  viewMetric = graph.getDoubleProperty("viewMetric")
  viewRotation = graph.getDoubleProperty("viewRotation")
  viewSelection = graph.getBooleanProperty("viewSelection")
  viewShape = graph.getIntegerProperty("viewShape")
  viewSize = graph.getSizeProperty("viewSize")
  viewSrcAnchorShape = graph.getIntegerProperty("viewSrcAnchorShape")
  viewSrcAnchorSize = graph.getSizeProperty("viewSrcAnchorSize")
  viewTexture = graph.getStringProperty("viewTexture")
  viewTgtAnchorShape = graph.getIntegerProperty("viewTgtAnchorShape")
  viewTgtAnchorSize = graph.getSizeProperty("viewTgtAnchorSize")

  #timepoints=[tp1_s,tp2_s,tp3_s,tp4_s,tp5_s,tp6_s,tp7_s,tp8_s,tp9_s,tp10_s,tp11_s,tp12_s,tp13_s,tp14_s,tp15_s,tp16_s,tp17_s]
  timepoints = [tp1_s, tp2_s, tp3_s, tp4_s, tp5_s, tp6_s]
  rootGraph=graph.getRoot()
  geneInteractions = rootGraph.getDescendantGraph('Genes interactions')
  #Partie 3
  smallMultiplesTree=rootGraph.addSubGraph(name='Small Multiples')
  buildSmallMultiples(smallMultiplesTree,geneInteractions,timepoints,viewMetric)
  
  nbCol = 4
  colorSmallMultiples(smallMultiplesTree,viewMetric)
  placeSmallMultiples(smallMultiplesTree, nbCol)
