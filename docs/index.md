---
hide:
  - navigation
  - toc
---

# 🚀 Bibliothèque des Standards DECADE-X

Bienvenue sur le portail officiel de la documentation technique et d'interopérabilité de l'écosystème **DECADE-X**.

Ce référentiel centralise l'ensemble des spécifications, modèles d'échange de données et vocabulaires nécessaires pour garantir une communication fluide, sécurisée et standardisée au sein de notre Data Space et de nos infrastructures V2X.

---

## 📚 Nos Standards Actifs

Voici les standards actuellement en vigueur. Cliquez sur un lien pour consulter les spécifications détaillées :

* **[DX-0001 : Data Exchange Base Pattern](active/AX-001.md)**
  *Spécifications fondamentales pour l'architecture des API et les échanges de données.*

---

## 🧠 Architecture Sémantique (SKOS)

!!! info "Une documentation intelligente et connectée"
    Ce portail n'est pas une simple documentation textuelle. Toutes nos définitions techniques sont pilotées par notre **Ontologie SKOS centrale**. 
    
    Les termes techniques présents dans nos standards (comme *API*, *Data Space*...) sont automatiquement extraits et injectés depuis notre référentiel sémantique lors de la compilation du site.

---

## 🛠️ Comment contribuer à ce portail ?

Ce site est généré automatiquement (CI/CD) à chaque modification sur notre dépôt GitHub. Pour participer :

1. **Créer ou modifier un standard :** Rédigez votre document en Markdown (`.md`) et placez-le dans le sous-dossier correspondant (ex: `docs/active/`). N'oubliez pas d'inclure les métadonnées (Front Matter) et d'appeler le `header.md`.
2. **Ajouter un terme au glossaire :** Ne modifiez pas les pages web ! Ajoutez simplement votre définition dans le fichier source `ontology/glossary.ttl` au format Turtle.
3. **Valider :** Poussez vos modifications sur la branche `main`. Les scripts automatisés s'occupent du reste.
