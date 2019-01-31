# Powered by Python 2.7

#Tulip project, part 3, building smallMultiples tree to see gene expressions at different time points in one view.
#18-01-2019
#Pauline Bock, Guillaume Sotton

from tulip import tlp
from tulipgui import tlpgui



"""
Creates smallMultiples Trees, colors them and displaces them.
"""
def createSmallMultiples(smallMultiplesTree, geneInteractions, timepoints, viewMetric):
  buildSmallMultiples(smallMultiplesTree,geneInteractions,timepoints,viewMetric)
  nbCol = 4
  colorSmallMultiples(smallMultiplesTree)
  placeSmallMultiples(smallMultiplesTree, nbCol)
  
"""
Builds smallMultiples graphs for each step of experiment time, and giving them the appropriate gene expression property into viewMetric property of each graph.
Giving smallMultiples parent graph, gene interactions graph, a list of the timepoint properties, and ciewMetric property.
"""
def buildSmallMultiples(smallMultiplesTree,geneInteractions,timepoints,metric):
  for i in range(1,len(timepoints)+1):
    tp=smallMultiplesTree.addSubGraph("tp"+str(i)+" s")
  
    inGraph=graph.getSubGraph("Genes interactions")
    tlp.copyToGraph(tp,inGraph, inSelection=None, outSelection=None)

  for time in timepoints:
    for sg in smallMultiplesTree.getSubGraphs():
      metric = sg.getLocalDoubleProperty("viewMetric")
      for n in sg.getNodes():
        timePropertyName = str(time).split(" ")
        timeName = timePropertyName[2]+" s"
        #Check if the name of the graph (associated to one timepoint) is equal to the right timepoint property
        if(timeName == sg.getName()):
          metric[n] = time[n]

"""
Colors all little graphs according to their viewMetric property, containing gene expression data.
"""
def colorSmallMultiples(smallMultiplesTree):
  for sg in smallMultiplesTree.getSubGraphs():
    sgMetric = sg.getLocalDoubleProperty("viewMetric")
    params = tlp.getDefaultPluginParameters('Color Mapping', sg)
    params['input property'] = sgMetric

    colorScaleManager = tlpgui.ColorScalesManager
    colorScale = colorScaleManager.getColorScale("BiologicalHeatMap")
    params['color scale'] = colorScale
    sg.applyColorAlgorithm('Color Mapping',params)

"""
Displaces all the little graphs by order of time points, in several rows and columns, given a number of columns.
"""
def placeSmallMultiples(smallMultiplesTree, nbCol):
  bb = tlp.computeBoundingBox(smallMultiplesTree)
  #Multiply by 2 to have a shift between all the graphs
  xmax = bb[1][0] *2
  ymax = bb[1][1] *2
  
  #Shifts all the graphs according to the number of their associated timepoint, the number of columns choosen and the bounding box
  for sg in smallMultiplesTree.getSubGraphs():
    smallLayout = sg.getLayoutProperty("viewLayout")
    sgNames = sg.getName().split(" ")
    sgName = sgNames[0]
    nbSG = int(sgName[2:len(sgName)])

    for i in range(0,nbCol+1):
      if (nbSG <= nbCol * (i+1) and nbSG > nbCol * i):
        for node in sg.getNodes():
          newPos = tlp.Coord(smallLayout[node][0] + xmax * (nbSG - nbCol *i), smallLayout[node][1] - ymax * i, smallLayout[node][2])
          smallLayout.setNodeValue(node, newPos)  
        
        for edge in sg.getEdges():
          newEdgePos = []
          for pos in smallLayout[edge]:
            newPos = tlp.Coord(pos[0] + xmax * (nbSG - nbCol *i) , pos[1] - ymax * i, pos[2])
            newEdgePos.append(newPos)
          smallLayout.setEdgeValue(edge, newEdgePos)

  
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
  viewMetric = graph.getDoubleProperty("viewMetric")
 
 
  timepoints=[tp1_s,tp2_s,tp3_s,tp4_s,tp5_s,tp6_s,tp7_s,tp8_s,tp9_s,tp10_s,tp11_s,tp12_s,tp13_s,tp14_s,tp15_s,tp16_s,tp17_s]
  rootGraph=graph.getRoot()
  geneInteractions = rootGraph.getDescendantGraph('Genes interactions')

  smallMultiplesTree=rootGraph.addSubGraph(name='Small Multiples')
  createSmallMultiples(smallMultiplesTree, geneInteractions, timepoints, viewMetric)

  smallMultiplesView = tlpgui.createView("Node Link Diagram view", smallMultiplesTree, dataSet = {}, show=True)
  glGraphRenderingParams = smallMultiplesView.getRenderingParameters()
  glGraphRenderingParams.setEdgeColorInterpolate(True)


  
