from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app_utils import ModelHandler, get_search_from_str
from dotenv import load_dotenv
import os
# If you still need these, keep them:
# from app_utils import get_data_from_ids, get_data_to_id
# but based on the snippet, they're not explicitly referenced.

load_dotenv()

API_KEY = os.getevn("API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_HANDLER = ModelHandler()

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    request_api_key = request.headers.get("X-API-Key")
    if request_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return await call_next(request)

@app.post("/recommend/from_id")
async def recommend_from_id(request: Request):
    """
    {
        "id": "my_id"
    }
    """
    try:
        data = await request.json()
        
        if not data:
            return JSONResponse({'error': 'No JSON data received'}, status_code=400)
        
        id: str = data['id']
        return_data: dict = MODEL_HANDLER.get_recommendation_from_id(id)

        return JSONResponse({'processed_data': return_data}, status_code=200)
    
    except Exception as e:
        # any internal error
        return JSONResponse({'error': str(e)}, status_code=500)

@app.post("/recommend/from_id_list")
async def recommend_from_id_list(request: Request):
    """
    {
        "ids": [
            "id_1",
            "id_2",
            "id_3"
        ]
    }
    """
    try:
        data = await request.json()
        
        if not data:
            return JSONResponse({'error': 'No JSON data received'}, status_code=400)

        # parse data
        ids: list = data['ids']
        return_data: dict = MODEL_HANDLER.get_recommendation_from_id_list(ids)
        return JSONResponse(return_data, status_code=200)
    
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

@app.post("/search/from_str")
async def search_from_str(request: Request):
    """
    api call: 
    {
        "search_input": "the songs I'm searching"
    }
    """
    try:
        data = await request.json()
        if not data:
            return JSONResponse({'error': 'No JSON data received'}, status_code=400)
        
        search_str: str = data['search_input']
        return_data: dict = get_search_from_str(search_str)
        
        return JSONResponse(return_data, status_code=200)
    
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

# To run locally:
#   uvicorn main:app --host 0.0.0.0 --port 5000 --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=5000, 
        reload=True
    )
