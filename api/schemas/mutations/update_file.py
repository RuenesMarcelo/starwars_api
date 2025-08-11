from typing import Optional
from django.core.exceptions import ObjectDoesNotExist
import strawberry
from asgiref.sync import sync_to_async

from api.models import Movie, Person
from api.schemas.types import MovieType, Planet, PersonType, PlanetType

from typing import Optional

@strawberry.input
class MovieUpdateInput:
    id_movie: str  
    name: Optional[str] = None
    opening_crawl: Optional[str] = None
    release_year: Optional[int] = None
    fan_score: Optional[int] = None
    id_director: Optional[str] = None
    id_producer: Optional[str] = None

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def update_movie(self, input: MovieUpdateInput) -> MovieType:
        movie = await sync_to_async(Movie.objects.get)(id_movie=input.id_movie)
        
        if input.name is not None:
            movie.name = input.name
        if input.opening_crawl is not None:
            movie.opening_crawl = input.opening_crawl
        if input.release_year is not None:
            movie.release_year = input.release_year
        if input.fan_score is not None:
            movie.fan_score = input.fan_score
        if input.id_director is not None:
            director = await sync_to_async(Person.objects.get)(id_person=input.id_director)
            movie.id_director = director
        if input.id_producer is not None:
            producer = await sync_to_async(Person.objects.get)(id_person=input.id_producer)
            movie.id_producer = producer
        
        await sync_to_async(movie.save)()
        return MovieType(
            id_movie=movie.id_movie,
            name=movie.name,
            opening_crawl=movie.opening_crawl,
            release_year=movie.release_year,
            fan_score=movie.fan_score,
            _instance=movie
        )
    


@strawberry.input
class PersonUpdateInput:
    id_person: str  
    name: Optional[str] = None
    lastname: Optional[str] = None
    id_role: Optional[int] = None  

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def update_person(self, input: PersonUpdateInput) -> PersonType:
        person = await sync_to_async(Person.objects.get)(id_person=input.id_person)
        
        if input.name is not None:
            person.name = input.name
        if input.lastname is not None:
            person.lastname = input.lastname
        if input.id_role is not None:
           
            from api.models import Role
            role = await sync_to_async(Role.objects.get)(id_role=input.id_role)
            person.id_role = role
        
        await sync_to_async(person.save)()
        
        return PersonType(
            id_person=person.id_person,
            name=person.name,
            lastname=person.lastname,
            _instance=person
        )
    




@strawberry.input
class PlanetUpdateInput:
    id_planet: int  
    name: Optional[str] = None

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def update_planet(self, input: PlanetUpdateInput) -> PlanetType:
        planet = await sync_to_async(Planet.objects.get)(id_planet=input.id_planet)

        if input.name is not None:
            planet.name = input.name

        await sync_to_async(planet.save)()

        return PlanetType(
            id_planet=planet.id_planet,
            name=planet.name
        )


