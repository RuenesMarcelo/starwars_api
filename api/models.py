# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Movie(models.Model):
    id_movie = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=40)
    opening_crawl = models.TextField()
    release_year = models.IntegerField()
    fan_score = models.IntegerField()
    id_director = models.ForeignKey('Person', models.DO_NOTHING, db_column='id_director')
    id_producer = models.ForeignKey('Person', models.DO_NOTHING, db_column='id_producer', related_name='movie_id_producer_set')

    class Meta:
        #managed = True
        db_table = 'movie'


class MoviePerson(models.Model):
    pk = models.CompositePrimaryKey('id_movie', 'id_person')
    id_movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='id_movie')
    id_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='id_person')

    class Meta:
        #managed = True
        db_table = 'movie_person'


class MoviePlanet(models.Model):
    pk = models.CompositePrimaryKey('id_movie', 'id_planet')
    id_movie = models.ForeignKey(Movie, models.DO_NOTHING, db_column='id_movie')
    id_planet = models.ForeignKey('Planet', models.DO_NOTHING, db_column='id_planet')

    class Meta:
        #managed = True
        db_table = 'movie_planet'


class Person(models.Model):
    id_person = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15, blank=True, null=True)
    id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role', blank=True, null=True)

    class Meta:
        #managed = True
        db_table = 'person'


class Planet(models.Model):
    id_planet = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)

    class Meta:
        #managed = True
        db_table = 'planet'


class Role(models.Model):
    id_role = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        #managed = True
        db_table = 'role'
