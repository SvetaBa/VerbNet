import os
#from py2neo import neo4j
from py2neo import Graph
from py2neo import Path, authenticate
from py2neo import Node,Relationship
import json
# set up authentication parameters
JSON_FILE = 'awesome_synsets.json'

authenticate("localhost:7474", "neo4j", "admin")

# connect to authenticated graph database
#graph = Graph("http://localhost:7474/db/data/")

# Connect to graph and add constraints.
neo4jUrl = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data/")
graph = Graph(neo4jUrl,secure=False)

# Connect to graph and add constraints.
#neo4jUrl = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data/")
#graph = neo4j.GraphDatabaseService(neo4jUrl)

# Send GET request.
json = json.load(open(JSON_FILE))

#print(json);

# Build query.
#tx = graph.begin()
for synset in json:
    if "Лексические варианты модели" not in synset:
        continue
    ss = Node("SSETS",
            name=synset.get("Основные предикаты", "Noname"),
            model=synset.get("Базовая модель", "Nomodel"),
            semantics=synset.get("Типовая семантика", "Nosemantics"))
    graph.create(ss)

    samples = synset['Лексические варианты модели']
    for verb in samples:
        v = Node("VERBS",
                name=verb.get("Глагол", "Noname"),
                definition=verb.get("МСС", "Nodefinition"),
                sample=verb.get("Илл.", "Nosample"),
                synonyms=verb.get("Пред.", "Nosynonyms"))
        graph.create(v)
        graph.create(Relationship(ss, "Содержит", v))
