# -*- coding: utf-8 -*-

from sqlite3 import *
import sqlite3
from sqlite3 import OperationalError
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





conn = sqlite3.connect('tulip.db')
  
cursor = conn.cursor()
fd = open('data.sql', 'r')
sqlFile = fd.read()
fd.close()
  
sqlCommands = sqlFile.split(';')
  
saisie=input("Veuillez saisir le numéro de locus dont vous souhaitez obtenir les informations:")

# Execute chaque commande du fichier entrée
for command in sqlCommands:
  # Va sauter et noter les erreurs rencontrés
  try:
    cursor.execute(command)
  except (OperationalError):
    print ("Commande sautées")
  
for table in ['GENE_HEAD_FC']:
  # Requête
  result = cursor.execute("SELECT * FROM %s WHERE gene_id=?;" % table,(saisie,))
  
# Avoir chaque ligne
  rows = result.fetchall()
  names = [description[0] for description in cursor.description]
  print ("\n--- TABLE ", table, "\n")
  print (names)
  for row in rows:
    print('{0} , {1}, {2},{3},{4},{5},{6},{7},{8},{9}'.format(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

      
cursor.close()
conn.close()
  
