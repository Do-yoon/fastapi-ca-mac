from datetime import datetime
import time
import uvicorn
 
from fastapi import APIRouter
 
router = APIRouter(prefix="/sync-test")
 
def sync_task(num):
    print("sync_task: ", num)
    time.sleep(1)
    return num
 
@router.get("")
def sync_example():
    now = datetime.now()
    results = [sync_task(1), sync_task(2), sync_task(3)]
    print(datetime.now() - now)
 
    return {"results": results}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)