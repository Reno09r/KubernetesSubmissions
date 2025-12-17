import os
import fastapi
from fastapi.responses import PlainTextResponse
import logging
import dotenv
import uvicorn
dotenv.load_dotenv()
PORT = int(os.getenv("PORT"))
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = fastapi.FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    logger.info("Root endpoint called")
    return "Server started in port {}".format(PORT)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=PORT)