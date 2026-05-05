import os
from rdflib import Graph
from rdflib.namespace import SKOS

print("💡 Generating SKOS definitions (one file per term)...")

skos_file = "ontology/glossary.ttl"
output_dir = "includes/glossary"

if not os.path.exists(skos_file):
    print(f"⚠️ File not found: {skos_file}")
    exit(0)

# Create the subdirectory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

g = Graph()
g.parse(skos_file, format="turtle")

for subject, predicate, obj in g.triples((None, SKOS.prefLabel, None)):
    # Target English labels
    if getattr(obj, 'language', '') == 'en':
        term = str(obj) 
        for def_obj in g.objects(subject, SKOS.definition):
            # Target English definitions
            if getattr(def_obj, 'language', '') == 'en':
                definition = str(def_obj).replace('\n', ' ')
                
                # Create ID (e.g., DataSpace -> dataspace)
                concept_name = str(subject).split('/')[-1].split('#')[-1]
                snippet_id = concept_name.lower() 
                
                # Create individual file (e.g., includes/glossary/dataspace.md)
                file_path = os.path.join(output_dir, f"{snippet_id}.md")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"**{term}** : {definition}\n")
                
                print(f"   -> File generated: {file_path}")

print("✅ Generation completed successfully!")
