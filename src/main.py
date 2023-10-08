from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.file_uploads import Upload
import typing

app = FastAPI()

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def upload_file(self, file: Upload) -> str:
        print(file)
        return "ok"
    
    @strawberry.mutation
    def upload_files(self, files: typing.List[Upload]) -> str:
        print(files)
        return "ok"
    
async def get_context(request: Request):
    return {
        "test": 123
    }

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)
graphql_app2 = GraphQLRouter(schema, context_getter=get_context)

app.include_router(graphql_app, prefix="/graphql")
app.include_router(graphql_app2, prefix="/graphql2")