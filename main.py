import uvicorn
from elasticsearch import AsyncElasticsearch
from fastapi import APIRouter, FastAPI


from routes import routes

app = FastAPI(
    title="ES posts API",
)
elastic_client = AsyncElasticsearch("http://localhost:9200")
app.state.elastic_client = elastic_client


app.include_router(APIRouter(routes=routes))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
