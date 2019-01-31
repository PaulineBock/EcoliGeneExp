# -*- coding: utf-8 -*-
#Tulip project, part 4, Annotates genes in the graph to make further analyses.
#Method with sql import to request a database file, results are shown in Tulip Console.
#18-01-2019
#Pauline Bock, Guillaume Sotton


from sqlite3 import *
import sqlite3
from sqlite3 import OperationalError
from tulip import tlp


conn = sqlite3.connect('tulip.db')
  
cursor = conn.cursor()
fd = open('data.sql', 'r')
sqlFile = fd.read()
fd.close()
  
sqlCommands = sqlFile.split(';')
  
locusInput =input("Veuillez saisir le numéro de locus dont vous souhaitez obtenir les informations:")

# Execute chaque commande du fichier entrée
for command in sqlCommands:
  # Va sauter et noter les erreurs rencontrés
  try:
    cursor.execute(command)
  except (OperationalError):
    print ("Commande sautées")
  
for table in ['GENE_HEAD_FC']:
  # Request
  result = cursor.execute("SELECT * FROM %s WHERE gene_id=?;" % table,(locusInput,))
  
  rows = result.fetchall()
  names = [description[0] for description in cursor.description]
  print ("\n--- TABLE ", table, "\n")
  print (names)
  for row in rows:
    print('{0} , {1}, {2},{3},{4},{5},{6},{7},{8},{9}'.format(row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
      
cursor.close()
conn.close()
 
