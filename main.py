from fastapi import FastAPI, HTTPException
from models import InputLoad
from utils import process_data
from datetime import datetime
app = FastAPI()

@app.post("/addition/")
async def perform_addition(input_data: InputLoad):
    now = datetime.now()
    started_time = now.strftime("%H:%M:%S")
    results = process_data(input_data)
    if None in results:
        raise HTTPException(status_code=500, detail="Error occurred during adding numbers")
    else:
        now = datetime.now()
        completed_time = now.strftime("%H:%M:%S")
        result = [sum(arr) for arr in results[1][1]]
        return {"batchid": results[0][1], "response": result, "status": "Complete", "started_at": started_time, "completed_at": completed_time}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)