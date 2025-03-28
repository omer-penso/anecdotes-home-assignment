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
COMMENTS_URL = "https://dummyjson.com/posts/{}/comments"

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


def get_posts_with_comments(limit: int = 60):
    posts = get_posts(limit)
    if not posts:
        return posts

    for post in posts:
        try:
            post_id = post.get("id")
            if not post_id:
                continue
            response = requests.get(COMMENTS_URL.format(post_id))
            if response.status_code == 200:
                comments = response.json().get("comments", [])
                post["comments"] = comments
            else:
                logger.error("Failed to fetch comments for post %s. Status Code: %s - %s", post_id, response.status_code, response.text)
                post["comments"] = []
        except Exception:
            logger.exception("Exception occurred while fetching comments for post %s", post_id)
            post["comments"] = []

    return posts