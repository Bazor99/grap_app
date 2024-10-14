import uvicorn
from fastapi import FastAPI
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pprint import pprint
from graph.graph import app
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

load_dotenv()

fastapi_app = FastAPI()
# Set all CORS enabled origins
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Define Pydantic model for request body
class QuestionRequest(BaseModel):
    question: str

# Add a route to test the generate node directly
@fastapi_app.post("/generate")
async def generate_route(data: QuestionRequest):
    received_string = data.question
    input_dict = {"question": received_string}
    try:
        outputs = []
        for output in app.stream(input_dict, config={"configurable": {"thread_id": "2"}}):
            for key, value in output.items():
                pprint(f"Finished running: {key}:")
                outputs.append({key: value})
                print(outputs)

        pprint(value["generation"])
        return {"result": outputs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="0.0.0.0", port=5000)