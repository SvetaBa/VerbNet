import json
import sqlite3

JSON_FILE = 'awesome_synsets.json'
DB_FILE   = 'db.sqlite3'

traffic = json.load(open(JSON_FILE))
conn = sqlite3.connect(DB_FILE)

id = 0
c = conn.cursor()
for i in range(len(traffic)):
    synset = traffic[i]
    c.execute("insert into VerbNet_synset (id, model, predicates, semantics) values ({}, '{}', '{}', '{}');".format(i, synset.get('Базовая модель', ''), synset.get('Основные предикаты', ''), synset.get('Типовая семантика', '')))

    if 'Лексические варианты модели' not in synset:
        continue
    samples = synset['Лексические варианты модели']
    for j in range(len(samples)):
        print(j)
        verb = samples[j]
        c.execute("insert into VerbNet_subsynset (id, definition, sample, synonyms, synset_id, verb) values ({}, '{}', '{}', '{}', {}, '{}');".format(id, verb.get('МСС', ''), verb.get('Илл.', ''), verb.get('Пред.', ''), i, verb.get('Глагол', '')))
        id += 1

conn.commit()
c.close()
