#!/usr/bin/python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Nom: check.py
# Objectif: Check le statut d'un port en fonction d'une IP
# Author: Maxime Berthault (Maxou56800)
# Created: 17/07/2012
# Licence: Gnu Public Licence (Richard Stallman)
#-----------------------------------------------------------------------------

### IMPORT DES LIBRARIES ###
import socket		# Lib pour checking()
from os import system	# Lib pour system() et lancer la procedure de remboursement
from time import sleep	# Lib pour sleep() afin de mettre des pauses

#xip = "x.x.x.x"	# IP du serveur.
#xport = xxxxx		# PORT du serveur.
duree_checking = 10	# Durée de verification pour verification du statut du serveur
duree_start_server = 120# Durée de lancement du serveur Garry.   
############################

### Message d'entête ###
print 'Début du script.'
########################

### Définition de la procédure de checking du statut du serveur ### 
def checking(dip,dport):
	x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
	    x.connect((dip, int(dport)))
	    x.shutdown(2)
	    return True
	    rembourssement()
	except:
	    return False
	    rembourssement()
###################################################################

### Définition de la procédure de remboursement ###
def rembourssement():
	while checking(xip,xport) == True: 	# Tant que notre fonction checkin renvois "True"
    	    print "Serveur Online"		# Affiche string
	    sleep( duree_checking ) 		# Dans ce cas attendre X temps pour recommencer la boucle
	else:
    	    system("curl google.com")		# Sinon, on lance la procédure de rembourssement (Curl pour tester)
    	    sleep( duree_start_server )		# On attend 2 minutes (120 secondes), le temps que le serveur se relance pour relancer la procédure de vérification
	    print "Relancement de la vérification"
	    rembourssement()			# On relance la vérification
##################################################

### On lance notre script ###
rembourssement()
#############################