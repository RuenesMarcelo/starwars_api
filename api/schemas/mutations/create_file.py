import strawberry
from typing import Optional

from ...models import Person, Planet, Role, Movie, MoviePerson, MoviePlanet
from ..types import PersonType, PlanetType, MovieType, MoviePersonType, MoviePlanetType, RoleType
from asgiref.sync import sync_to_async

@strawberry.type
class CreateMutation:

    
    @strawberry.mutation
    async def create_role(self, id_role: int, name: str) -> RoleType:
        role= await sync_to_async(Role.objects.create)(
            id_role=id_role,
            name=name
        )
        return RoleType(
            id_role=role.id_role,
            name=role.name
        )

    @strawberry.mutation
    async def create_person(self, id_person: str, name: str, lastname: Optional[str], id_role: int) -> PersonType:
        role = await sync_to_async(Role.objects.get)(id_role=id_role)
        person = await sync_to_async(Person.objects.create)(
            id_person=id_person,
            name=name,
            lastname=lastname,
            id_role=role
        )
        return PersonType(
            id_person=person.id_person,
            name=person.name,
            lastname=person.lastname,
            _instance=person
        )

    @strawberry.mutation
    async def create_planet(self, id_planet: int, name: str) -> PlanetType:
        planet = await sync_to_async(Planet.objects.create)(
            id_planet=id_planet,
            name=name,
        )
        return PlanetType(
            id_planet=planet.id_planet,
            name=planet.name
        )

    @strawberry.mutation
    async def create_movie(self, id_movie: str, name: str, opening_crawl: str, release_year: int, 
                           fan_score: int, id_director: str, id_producer:str ) -> MovieType:
        director = await sync_to_async(Person.objects.get)(id_person=id_director)
        producer = await sync_to_async(Person.objects.get)(id_person=id_producer)


        movie = await sync_to_async(Movie.objects.create)(
            id_movie=id_movie,
            name=name,
            opening_crawl=opening_crawl,
            release_year=release_year,
            fan_score=fan_score,
            id_director=director,
            id_producer=producer
        )
        return MovieType(
            id_movie=movie.id_movie,
            name=movie.name,
            opening_crawl=movie.opening_crawl,
            release_year=movie.release_year,
            fan_score=movie.fan_score,
            _instance=movie,             
        )
    
    @strawberry.mutation
    async def create_movie_person(self, id_movie: str, id_person: str) -> MoviePersonType:
        movie = await sync_to_async(Movie.objects.get)(id_movie=id_movie)
        person = await sync_to_async(Person.objects.get)(id_person=id_person)
        movie_person = await sync_to_async(MoviePerson.objects.create)(
            id_movie=movie,
            id_person=person
        )
        return MoviePersonType(
            id_movie=movie.id_movie,
            id_person=person.id_person,
            _instance=movie_person
        )

    @strawberry.mutation
    async def create_movie_planet(self, id_movie: str, id_planet: int) -> MoviePlanetType:
        movie = await sync_to_async(Movie.objects.get)(id_movie=id_movie)
        planet = await sync_to_async(Planet.objects.get)(id_planet=id_planet)
        movie_planet = await sync_to_async(MoviePlanet.objects.create)(
            id_movie=movie,
            id_planet=planet
        )
        return MoviePlanetType(
            id_movie=movie.id_movie,
            id_planet=planet.id_planet,
            _instance=movie_planet
        )
