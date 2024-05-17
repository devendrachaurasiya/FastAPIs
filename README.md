Project Title
FastAPIs

Table of Contents
Main.py
Models.py
Tests.py
utils.py

About
Passing Payload to find the sum of nested array
Getting Started!

# 
To Run 
uvicorn main:app --reload
POST: http://localhost:8000/addition/



Input load: {
  "batchid": "id0101",
  "payload": [[1,2],[3,4]]

}

output_load:
{
    "batchid": "id0101",
    "response": [3,7],
    "status": "Complete",
    "started_at": "08:54:00",
    "completed_at": "08:54:00"
}