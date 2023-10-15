from django.db import models

class Subject (models.Model):

    GROUP_CHOICES = (
        ("Math", "Math"),
        ("Experimental Sciences", "Experimental Sciences"),
        ("LanguageA", "Language Liturature"),
        ("LanguageB", "Language acquisition"),
        ("Social Sciences", "Social Sciences"),
        ("The Arts", "the arts"),
        ("General", "General"),
        ("DP core", "DP core"),
    )

    Subjects = models.CharField(max_length=30)
    Group = models.CharField(max_length=30,choices=GROUP_CHOICES)

    def __str__(self):
        return self.Subjects
