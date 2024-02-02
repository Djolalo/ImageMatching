# TP D'AIV 1 Correpondances d'images

## Exercice 1

<details>
<summary>Cliquez pour voir</summary>

### Question 1:
Cette représentation des points-clés donne le rayon utilisé lors de la différence des gaussiennes.
Ce rayon nous permet de savoir s'il s'agit vraisemblablement d'un bord ou non (grossièrement, plus le rayon est gros,
moins on a de change qu'il s'agisse d'un bord). L'angle rerprésenté nous donne l'orientation du point d'intérêt;
cette orientation est l'orientation du gradient dominant l'espace étudié (on peut parfois en trouver un 2ème)

## Question 2:
Dans un objet point-clé (KeyPoint sous openCV), on retrouve diverses propriétés comme l'angle, un entier représentant
l'octave (nous y reviendrons sous peu), le score dans un entier "Response", et size, le Rayon. 

Dans l'entier octave, on a les informations nécessaires pour retrouver la couche à laquelle la point clé a été trouvé.
Les 8 premiers bits de cet entier gardent le numéro d'octave, les 8 bits suivant la couche, et si l'octave est négative,
c'est que l'image a été aggrandie, sinon, c'est qu'elle a été réduite. 

## Question 3: 


</details>

