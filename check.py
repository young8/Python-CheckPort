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
duree_checking = 10	# Dur�e de verification pour verification du statut du serveur
duree_start_server = 120# Dur�e de lancement du serveur Garry.   
############################

### Message d'ent�te ###
print 'D�but du script.'
########################

### D�finition de la proc�dure de checking du statut du serveur ### 
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

### D�finition de la proc�dure de remboursement ###
def rembourssement():
	while checking(xip,xport) == True: 	# Tant que notre fonction checkin renvois "True"
    	    print "Serveur Online"		# Affiche string
	    sleep( duree_checking ) 		# Dans ce cas attendre X temps pour recommencer la boucle
	else:
    	    system("curl google.com")		# Sinon, on lance la proc�dure de rembourssement (Curl pour tester)
    	    sleep( duree_start_server )		# On attend 2 minutes (120 secondes), le temps que le serveur se relance pour relancer la proc�dure de v�rification
	    print "Relancement de la v�rification"
	    rembourssement()			# On relance la v�rification
##################################################

### On lance notre script ###
rembourssement()
#############################