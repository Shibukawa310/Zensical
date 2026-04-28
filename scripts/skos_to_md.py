import os
import re
from rdflib import Graph
from rdflib.namespace import SKOS

print("💡 Extraction des définitions SKOS (Anglais) en blocs séparés...")

skos_file = "ontology/glossary.ttl"
md_file = "includes/glossary.md"

if not os.path.exists(skos_file):
    print(f"⚠️ Fichier introuvable : {skos_file}")
    exit(0)

g = Graph()
g.parse(skos_file, format="turtle")

os.makedirs(os.path.dirname(md_file), exist_ok=True)
with open(md_file, "w", encoding="utf-8") as f:
    f.write("\n\n")
    
    for subject, predicate, obj in g.triples((None, SKOS.prefLabel, None)):
        if getattr(obj, 'language', '') == 'en':
            term = str(obj) 
            for def_obj in g.objects(subject, SKOS.definition):
                if getattr(def_obj, 'language', '') == 'en':
                    definition = str(def_obj).replace('\n', ' ')
                    concept_name = str(subject).split('/')[-1].split('#')[-1]
                    # On transforme CamelCase en snake_case pour correspondre aux logs
                    snippet_id = re.sub(r'(?<!^)(?=[A-Z])', '_', concept_name).lower()
                    
                    print(f"   -> Concept trouvé : '{term}' | Snippet ID : :{snippet_id}")
                    f.write(f"--8<-- [start:{snippet_id}]\n")
                    f.write(f"**{term}** : {definition}\n")
                    f.write(f"--8<-- [end:{snippet_id}]\n\n")
