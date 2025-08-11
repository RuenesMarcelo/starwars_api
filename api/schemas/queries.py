import strawberry
from typing import List, Optional
from ..models import Person, Role, Movie, Planet, MoviePerson, MoviePlanet
from .types import  PersonType, RoleType, MovieType, PlanetType, MovieViewType,  MoviePersonType, MoviePlanetType, CharacterType, CharacterInMovieType
from asgiref.sync import sync_to_async

@strawberry.type
class Query:

    @strawberry.field
    async def all_roles(self) -> List[RoleType]:
        roles = await sync_to_async(list)(Role.objects.all())
        return [RoleType(id_role=r.id_role, name=r.name) for r in roles]

    @strawberry.field
    async def all_people(self) -> List[PersonType]:
        people = await sync_to_async(list)(Person.objects.all())
        return [PersonType(
            id_person=p.id_person,
            name=p.name,
            lastname=p.lastname,
            _instance=p
        ) for p in people]

    @strawberry.field
    async def characters(self) -> List[CharacterType]:
        people = await sync_to_async(list)(Person.objects.filter(id_role=1))
        return [CharacterType(
            name=p.name,
            lastname=p.lastname
        ) for p in people]

    @strawberry.field
    async def all_planets(self) -> List[PlanetType]:
        planets = await sync_to_async(list)(Planet.objects.all())
        return [PlanetType(id_planet=pl.id_planet, name=pl.name) for pl in planets]

    @strawberry.field
    async def all_movies(self) -> List[MovieType]:
        movies = await sync_to_async(list)(Movie.objects.all())
        return [MovieType(
            id_movie=m.id_movie,
            name=m.name,
            opening_crawl=m.opening_crawl,
            release_year=m.release_year,
            fan_score=m.fan_score,
            _instance=m
        ) for m in movies]
    
   
    
    @strawberry.field
    async def moviesviews(self) -> List[MovieViewType]:
        movies = await sync_to_async(lambda: list(Movie.objects.all()))()
        return [
            MovieViewType(
                id_movie=m.id_movie,
                name=m.name,
                opening_crawl=m.opening_crawl,
                release_year=m.release_year,
                fan_score=m.fan_score,
                _instance=m
            )
            for m in movies
        ]

    @strawberry.field
    async def all_moviesPeople(self) -> List[MoviePersonType]:
        movies_people = await sync_to_async(list)(MoviePerson.objects.all())
        return [MoviePersonType(
            id_movie=mp.id_movie_id,
            id_person=mp.id_person_id,
            _instance=mp
        ) for mp in movies_people]

    @strawberry.field
    async def all_moviesPlanets(self) -> List[MoviePlanetType]:
        movies_planets = await sync_to_async(list)(MoviePlanet.objects.all())
        return [MoviePlanetType(
            id_movie=mp.id_movie_id,
            id_planet=mp.id_planet_id,
            _instance=mp
        ) for mp in movies_planets]

    @strawberry.field
    async def characters_in_movies(self, character_name: Optional[str] = None) -> List[CharacterInMovieType]:
        qs = MoviePerson.objects.select_related('id_person', 'id_movie')

        if character_name:
            qs = qs.filter(id_person__name__icontains=character_name)

        mp_list = await sync_to_async(list)(qs)

        return [
            CharacterInMovieType(
                character_name=mp.id_person.name,
                movie_name=mp.id_movie.name,
                movie_id=mp.id_movie.id_movie
            ) for mp in mp_list
        ]
