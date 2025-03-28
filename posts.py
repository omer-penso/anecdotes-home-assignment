import logging
import requests

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

POSTS_URL = "https://dummyjson.com/posts"

def get_posts(limit: int = 60):
    try:
        response = requests.get(f"{POSTS_URL}?limit={limit}")

        if response.status_code == 200:
            data = response.json()
            return data.get("posts", [])
        else:
            logger.error("Failed to fetch posts. StatusCode: %s - %s", response.status_code, response.text)
            return None

    except Exception:
        logger.exception("Exception occurred while fetching posts.")
        return None
