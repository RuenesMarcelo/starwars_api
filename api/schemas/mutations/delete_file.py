import strawberry
from asgiref.sync import sync_to_async
from api.models import Movie, Planet, Person, MoviePerson, MoviePlanet

@strawberry.type
class DeleteMutation:
    @strawberry.mutation
    async def delete_movie(self, id_movie: str) -> bool:
        try:
            movie = await sync_to_async(Movie.objects.get)(id_movie=id_movie)
            await sync_to_async(movie.delete)()
            return True
        except Movie.DoesNotExist:
            return False
    
    @strawberry.mutation
    async def delete_planet(self, id_planet: int) -> bool:
        try:
            planet = await sync_to_async(Planet.objects.get)(id_planet=id_planet)
            await sync_to_async(planet.delete)()
            return True
        except Planet.DoesNotExist:
            return False

    
    @strawberry.mutation
    async def delete_person(self, id_person: int) -> bool:
        try:
            person = await sync_to_async(Person.objects.get)(id_person=id_person)
            await sync_to_async(person.delete)()
            return True
        except Person.DoesNotExist:
            return False

    
    @strawberry.mutation
    async def delete_role(self, id_role: int) -> bool:
        try:
            role = await sync_to_async(Person.objects.get)(id_person=id_role)
            await sync_to_async(role.delete)()
            return True
        except Person.DoesNotExist:
            return False
        
    @strawberry.mutation
    async def delete_movie_person(self, id_movie: str, id_person: str) -> bool:
        try:
            obj = await sync_to_async(MoviePerson.objects.get)(id_movie_id=id_movie, id_person_id=id_person)
            await sync_to_async(obj.delete)()
            return True
        except MoviePerson.DoesNotExist:
            return False

    @strawberry.mutation
    async def delete_movie_planet(self, id_movie: str, id_planet: int) -> bool:
        try:
            obj = await sync_to_async(MoviePlanet.objects.get)(id_movie_id=id_movie, id_planet_id=id_planet)
            await sync_to_async(obj.delete)()
            return True
        except MoviePlanet.DoesNotExist:
            return False

