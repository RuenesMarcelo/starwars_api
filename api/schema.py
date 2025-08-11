import strawberry
from .schemas.queries import Query
from .schemas.mutations.create_file import CreateMutation
from .schemas.mutations.update_file import Mutation
from .schemas.mutations.delete_file import DeleteMutation

@strawberry.type
class Mutation(CreateMutation, Mutation, DeleteMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)