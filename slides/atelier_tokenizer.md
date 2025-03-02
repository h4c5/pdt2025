---
marp: true
theme: default
lang: fr
paginate: true
header: "![h:60](images/logo_letters.png)"
footer: "Primptemps de la Tech | Comprendre les tokens par la pratique"
---

<style>
/* 
Couleurs : 
    - #69bfbc
    - #e12967
    - #6d6cae
    - #f3956e
    - #fbbb2b
    - #222d4e
*/

:root.lead {
    text-align: center;
}

:root.lead h1,h2,h3 {
    color: white;
}

:root h1,h2,h3 {
    color: #e12967;
}

</style>

<!-- Slide de présentation -->
<!-- _paginate: skip -->
<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _backgroundImage: "linear-gradient(0deg, #ead283, #91c4aa, #6abfbc)"  -->

![Logo Printemps de la Tech h:400](images/logo_colore.png)

# Comprendre les tokens par la pratique

---

<!-- _paginate: skip -->
<!-- _header: "" -->

![bg contain left:30%](images/profil_pdt.png)

## Hakim Cheikh
**Data Scientist chez Valeuriad depuis 3 ans**

_En mission chez France Travail_

---

## Pré-requis

:snake: Python niveau A1

## Déroulé

1. Introduction à la tokenization
2. Implémentation d'un tokenizer
3. Remarques et conclusion

---

### _Quelques notions de NLP_

**NLP** : **N**atural **L**angage **P**rocessing

Exemples de cas d'usage : 

- Catégorisation de contenu
- Extraction d'entités 
- Analyse de sentiments
- Traduction
- Résumé
- Génération de texte

---

### _Quelques notions de NLP_ : Décompositions en mots

Les algorithmes fonctionnent à partir d'une représentation sous forme numérique.

```python
text = "Bienvenu au Printemps de la Tech 2025"
```

**Première approche :** décomposer le texte sur les espaces puis construire un vocabulaire

```python
words = text.split(" ")
# ['Bienvenu', 'au', 'Printemps', 'de', 'la', 'Tech', '2025']

vocab = {word: i for i, word in enumerate(words)}

text_ids = [vocab[word] for word in words]
text_ids
# [0, 1, 2, 3, 4, 5, 6]
```

---

### _Quelques notions de NLP_ : Décompositions en mots

```python
text
# "Bienvenu au Printemps de la Tech 2025"

text_ids
# [0, 1, 2, 3, 4, 5, 6]

vocab
# {'Bienvenu': 0, 'au': 1, 'Printemps': 2, 'de': 3, 'la': 4, 'Tech': 5, '2025': 6}
```

Ce que l'on vient de faire est une **tokenization** : il s'agit de représenter le texte en **tokens**, c'est-à-dire en unités élémentaires.

---

### _Quelques notions de NLP_ : Décompositions en mots

- Le vocabulaire est construit à partir de textes de référence
- Les mots qui ne se trouvent pas dans les textes de références ne pourront pas être interprétés de la même manière
- Les mots qui ont la même racine ont des identifiants complètement différents
  - Exemple : mobile / automobile / mobilité / immobile, immobilier, etc.
- Pour adresser les points précédents, il existe des techniques de pré-traitement (mise en minuscule, lemmatization, élimination des mots trop courants, etc.)
- Pour certains cas d'usage on peut ignorer l'ordre des mots.

---

### _Quelques notions de NLP_ : Décompositions en caractères

```python
text = "Bienvenu au Printemps de la Tech 2025"
```

**Seconde approche :** décomposer le texte en caractères

```python
text_ids = [ord(c) for c in text]
text_ids
#   B,   i,   e,   n,   v,   e,   n,   u,  ·,  a,   u,  ·,  P,   r,   i,   n,   t,
# [66, 105, 101, 110, 118, 101, 110, 117, 32, 97, 117, 32, 80, 114, 105, 110, 116, ...]
```

---

### _Quelques notions de NLP_ : Décompositions en caractères

- Le vocabulaire se résume aux caractères unicode.
- Le problème des mots qui partagent la même racine a disparu mais l'ordre des lettres est important.
- Un même texte compte maintenant bien plus tokens.

---

**Quizz** : Combien y a-t-il de point de code [unicode](https://www.unicode.org/versions/Unicode15.0.0/) ?

---

**Quizz** : Combien y a-t-il de point de code [unicode](https://www.unicode.org/versions/Unicode15.0.0/) ?

**149 186 !** 
_(dans la version 15.0)_

---

### _Quelques notions de NLP_ : N-grams

Une troisième approche est de décomposer le texte en **n-grams** :

```python
text = "Bienvenu au Printemps de la Tech 2025"

N = 3
tokens = [text[i:i+N] for i in range(0, len(text))]
tokens
# ['Bie', 'ien', 'env', 'nve', 'ven', 'enu', 'nu ', 'u a', ' au', 'au ', 'u P', ...]
```

- L'ordre devient moins important
- Mais la taille du vocabulaire explose

---

### Tokenization "moderne"

![bg right:70%](images/screen_tiktokenizer.png)

Aujourd'hui OpenAI utilise l'algorithme _Byte Pair Encoding_ introduit par Philip Gage en 1994 pour ChatGPT.

[Démo](https://tiktokenizer.vercel.app/)

---


# Merci !

Questions & Réponses