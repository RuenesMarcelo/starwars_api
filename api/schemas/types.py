import strawberry
from typing import List
from typing import Optional
from ..models import Person, Role, Movie, Planet, MoviePerson, MoviePlanet
from asgiref.sync import sync_to_async

@strawberry.type
class RoleType:
    id_role: int
    name: str

@strawberry.type
class PersonType:
    id_person: str
    name: str
    lastname: Optional[str]
    _instance: strawberry.Private[Person]

    @strawberry.field
    async def id_role(self) -> RoleType:
        role = await sync_to_async(lambda: self._instance.id_role)()
        return RoleType(id_role=Role.id_role, name=Role.name)

@strawberry.type
class MovieType:
    id_movie: str
    name: str
    opening_crawl: str
    release_year: int
    fan_score: int
    _instance: strawberry.Private[Movie]

    @strawberry.field
    async def id_director(self) -> PersonType:
        director = await sync_to_async(lambda: self._instance.id_director)()
        return PersonType(
            id_person=director.id_person,
            name=director.name,
            lastname=director.lastname,
            _instance=director
        )

    @strawberry.field
    async def id_producer(self) -> PersonType:
        producer = await sync_to_async(lambda: self._instance.id_producer)()
        return PersonType(
            id_person=producer.id_person,
            name=producer.name,
            lastname=producer.lastname,
            _instance=producer
        )

@strawberry.type
class PlanetType:
    id_planet: int
    name: str

@strawberry.type
class MovieViewType:
    id_movie: str
    name: str
    opening_crawl: str
    release_year: int
    fan_score: float
    _instance: strawberry.Private[Movie] 
    

    @strawberry.field
    async def id_director(self) -> PersonType:
        director = await sync_to_async(lambda: self._instance.id_director)()
        return PersonType(
            id_person=director.id_person,
            name=director.name,
            lastname=director.lastname,
            _instance=director
        )
    
    @strawberry.field
    async def id_producer(self) -> PersonType:
        producer = await sync_to_async(lambda: self._instance.id_producer)()
        return PersonType(
            id_person=producer.id_person,
            name=producer.name,
            lastname=producer.lastname,
            _instance=producer
        )

    @strawberry.field
    async def planets(self) -> List[PlanetType]:
        movie_id = self.id_movie
        movie_planets = await sync_to_async(lambda: list(
            MoviePlanet.objects.filter(id_movie=movie_id).select_related("id_planet")
        ))()

        return [PlanetType(id_planet=mp.id_planet.id_planet, name=mp.id_planet.name) for mp in movie_planets]


@strawberry.type
class MoviePlanetType:
    id_movie: str
    id_planet: str
    _instance: strawberry.Private[MoviePlanet]

    @strawberry.field
    async def movie(self) -> MovieType:
        movie = await sync_to_async(lambda: self._instance.movie)()
        return MovieType(
            id_movie=movie.id_movie,
            name=movie.name,
            opening_crawl=movie.opening_crawl,
            release_year=movie.release_year,
            fan_score=movie.fan_score,
            _instance=movie
        )

    @strawberry.field
    async def planet(self) -> PlanetType:
        planet = await sync_to_async(lambda: self._instance.planet)()
        return PlanetType(id_planet=planet.id_planet, name=planet.name)

@strawberry.type
class MoviePersonType:
    id_movie: str
    id_person: str
    _instance: strawberry.Private[MoviePerson]

    @strawberry.field
    async def movie(self) -> MovieType:
        movie = await sync_to_async(lambda: self._instance.movie)()
        return MovieType(
            id_movie=movie.id_movie,
            name=movie.name,
            opening_crawl=movie.opening_crawl,
            release_year=movie.release_year,
            fan_score=movie.fan_score,
            _instance=movie
        )

    @strawberry.field
    async def person(self) -> PersonType:
        person = await sync_to_async(lambda: self._instance.person)()
        return PersonType(
            id_person=person.id_person,
            name=person.name,
            lastname=person.lastname,
            _instance=person
        )

@strawberry.type
class CharacterType:
    name: str
    lastname: Optional[str]

@strawberry.type
class CharacterInMovieType:
    character_name: str
    movie_id: str
    movie_name: str
