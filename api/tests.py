import pytest
from strawberry.django.test import GraphQLTestClient
from api.schema import schema
from strawberry.django.test import GraphQLTestClient
from django.test import Client as DjangoClient
from api.models import Movie, Planet, MoviePlanet, Person, Role

@pytest.mark.django_db
def test_moviesviews_query_integration():
    
    role_director = Role.objects.create(id_role=2, name="Director")
    role_producer = Role.objects.create(id_role=3, name="Producer")

    director = Person.objects.create(
        id_person="DIR2",
        name="George",
        lastname="Walton",
        id_role=role_director
    )
    producer = Person.objects.create(
        id_person="PROD3",
        name="Rick",
        lastname="McCallum",
        id_role=role_producer
    )


    movie = Movie.objects.create(
        id_movie="Episode_I",
        name="The Phantom Menace",
        release_year=1999,
        fan_score=59,
        opening_crawl="Turmoil has engulfed the Galactic Republic...",
        id_director=director,
        id_producer=producer
    )

    planet1 = Planet.objects.create(id_planet=1, name="Naboo")
    planet2 = Planet.objects.create(id_planet=2, name="Tatooine")
    MoviePlanet.objects.create(id_movie=movie, id_planet=planet1)
    MoviePlanet.objects.create(id_movie=movie, id_planet=planet2)

    client = GraphQLTestClient(DjangoClient(), url="/graphql/")
    response = client.query("""
        query {
          moviesviews {
            idMovie
            name
            releaseYear
            fanScore
            openingCrawl
            planets {
              name
            }
            idDirector {
              idPerson
              name
            }
          }
        }
    """)

    data = response.data["moviesviews"][0]
    assert data["idMovie"] == "Episode_I"
    assert data["name"] == "The Phantom Menace"
    assert data["releaseYear"] == 1999
    assert data["fanScore"] == 59
    assert data["openingCrawl"].startswith("Turmoil")
    assert {p["name"] for p in data["planets"]} == {"Naboo", "Tatooine"}
    assert data["idDirector"]["idPerson"] == "DIR2"
    assert data["idDirector"]["name"] == "George"
