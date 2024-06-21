from celery.result import AsyncResult
from common.messaging import celery

if __name__ == "__main__":
    async_result = AsyncResult("92d9f330-b504-4be7-b9af-83bab4e04d22", app=celery)
    result = async_result.result
 
    print(result)
