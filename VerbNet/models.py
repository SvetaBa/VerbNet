from django.db import models

class Synset(models.Model):
    semantics = models.CharField(max_length=300, null=True)
    model = models.CharField(max_length=100, null=True)
    predicates = models.CharField(max_length=150, null=True)


class SubSynset(models.Model):
	definition = models.CharField(max_length=300, null=True)
	verb = models.CharField(max_length=30, null=True)
	sample = models.CharField(max_length=300, null=True)
	synonyms = models.CharField(max_length=300, null=True)
	synset = models.ForeignKey(Synset)