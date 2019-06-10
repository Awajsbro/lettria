import sys, re
from ressource.table import tree1, tree2, tree3

#########################################
def main() :							#
	lst = []							#
	for arg in sys.argv :				#
		for word in arg.split(' ') :	#
			if word != '' :				# Creation de la liste
				lst.append(word)		#
										#
	del lst[0]							#
	print(lst)							#
	return (reperWord(lst))				#
#########################################


def reperWord(lst=[]) :
	# ---TODO--- verifier que l'on me donne quelque chose de valide
	tmp = " ".join(lst)
	lst = re.split("([^a-z])", tmp, flags=re.IGNORECASE)	#decoupage de la ponctuation et des nombres
	phone = []
	for word in lst :
		if word == "" :				#supression des chaine vide creer par split
			continue

		elif re.search("[^a-z]", word) != None :
			phone.append(word)		#sauvegarde de la ponctuation et des nombres

		else :
			phone.append(prepareWord(word))	#appel de la fonction qui arrange les mots avant "l'ecoute"

	print(phone)#############################
	# ---TODO--- fonction qui suis le chemin phonetique jusqu'aux mots corrects


def prepareWord(word) :
	errorWord = word##############################
	word = word.lower()
	pluri = 0
	if word[-1] == ('s' or 'x') :	#retrait des pluriels
		pluri = 1
		word = word.rstrip('s' or 'x')

	try :
		word = word.rstrip('t' or 'd')	#retrait de charactere non prononce
		word = word.lstrip('h')			#retrait du 1er h muet pour doubler le 1er s si existe
		if word[1] == 's' and word[1] != word[2] :
			word = 's' + word

	except :
		print("Error with word : {}".format(errorWord))
		return("ERROR with word : {}".format(errorWord))

	word = word.replace("gi", "ji")
	word = word.replace("ge", "je")	#remplacement de charactere pour simuler des regles
	word = word.replace("il", "xyz")
	print(word)##################################
	tmp = findingPhone(word)		#appel de la fonction qui transforme en phonetique
	if pluri == 1 :
		tmp.append('s')				#mise d'un marquer pluriel si necessaire

	return (tmp)


def findingPhone(word) :
	tmp = []
	while word  != "" :
		try :
			if word[1] == word[2] and word[0] == 'e' :	#regle paticuliere pout e suivis d'une double consonnes
				tmp.append(tree2[val('a')][val('i')])
				word = word[1:]

			elif word[1] == word[2] :	#si double consonnes la lettre avant est forcemnt seul
				raise OnlyOne()

			elif tree3[val(word[0])][val(word[1])][val(word[2])] == None :	#si il ni a pas de code phonetique c'est une syllable d'une ou 2 lettres
				raise TooLong()

			else :
				tmp.append(tree3[val(word[0])][val(word[1])][val(word[2])])	#sylable de 3 lettres trouve
				word = word[3:]												#decalage sur les lettres suivantes

		except (TooLong, IndexError) :
			try :
				if tree2[val(word[0])][val(word[1])] == None : #si il ni a pas de code phonetique c'est une syllable d'une seul lettre
					raise OnlyOne()

				else :
					tmp.append(tree2[val(word[0])][val(word[1])])	#syllable a 2 lettres trouve
					word = word[2:]									#decalage sur les lettres suivantes

			except IndexError :								#arrive ici seulement si il reste une seul lettre
				if word[0] == 'e' :							#si c'est un e finale on le prononce 'eu'
					tmp.append(tree2[val("e")][val("u")])
					word = word[1:]							#fin du mot on passera au suivant

				else :
					tmp.append(tree1[val(word[0])])	#
					word = word[1:]					#
													#
			except OnlyOne :						#
				tmp.append(tree1[val(word[0])])		#seul posibiliter restante une syllable d'une lettre
				word = word[1:]						#decalage sur la lettre suivante
													#
		except OnlyOne :							#
			tmp.append(tree1[val(word[0])])			#
			word = word[1:]							#

	return (tmp)		#return du code phonetique


##########-TOOL-##########################

def val(c='a') :				#a default de macro
	return (ord(c) - 97)


class TooLong(Exception) :		#execption quand la sylable fait moins de 3 characteres
	pass


class OnlyOne(Exception) :		#exception quand la sylable fait forcement 1 charactere
	pass


if __name__ == "__main__" :
	main()


#	1-lire 2-ecouter 3-rechercher

# probleme potentielle :
#		impossible de distinguer 2 mots homophones
#		mauvaise liste -> verifier la liste en entree
#		erreur dans les sons proches ->todo fonction de recherche elargi
#???	pluriel -> ?? retirer les s et x a chaque fin de mot pour les remettre ??
# 		conjugaison
#		accord au feminin
#DONE	ponctuation ->todo couper autour et laisser passer
#		les accents	->todo remplacer les charactere accentue par ceux avant dans la table ascii
#~~		les sons differents pour certain cas particulier ->todo 'e', 'eu' 't' 's' 'c' et 'g'
#		#	-rediriger les cas particulier / rectifier suivant les suites phonetique ?
#
#		double consonnes n fois repete

#### mots a probleme ####
# cantine
