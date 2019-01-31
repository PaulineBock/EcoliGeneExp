# Powered by Python 2.7


#Tulip project, part 4, Annotates genes in the graph to make further analyses.
#Method with Tulip AppImage, without specific import, results are stored in a new property.
#18-01-2019
#Pauline Bock, Guillaume Sotton

from tulip import tlp

"""
Reads a file containing annotations data for several E.coli gene locus, adding these data in a Gene Ontology property for the right locus.
"""
def annotation(Locus, go, geneInteractions):  
  file=open("data.txt","r")
  l = file.readline()
  cpt = 0
  while l!= "":
    words = l.split(",")
    lineLocus = words[0].split("(")
    idLocus = lineLocus[1]
  
    for n in geneInteractions.getNodes():
      nodeLocus = Locus[n]
      compNodeLocus = "\'" + str(nodeLocus) + "\'" 
      if (compNodeLocus == idLocus):
        goTerm = words[7]
        go[n] = go[n] + goTerm
    cpt+=1
    l = file.readline()
 
def main(graph): 
  geneInteractions = graph.getDescendantGraph("Genes interactions")
  Locus = graph.getStringProperty("Locus")
  go = graph.getStringProperty("Gene Ontology")
  
  annotation(Locus, go, geneInteractions)

 



