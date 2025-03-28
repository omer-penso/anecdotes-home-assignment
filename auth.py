import logging
import requests

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

LOGIN_URL = "https://dummyjson.com/auth/login"
ME_URL = "https://dummyjson.com/auth/me"

def login(username: str, password: str, expires_in_mins: int = 30):
    try:
        response = requests.post(
            LOGIN_URL,
            headers={"Content-Type": "application/json"},
            json={
                "username": username,
                "password": password,
                "expiresInMins": expires_in_mins
            }
        )

        if response.status_code == 200:
            data = response.json()
            logger.info("Login successful for user: %s", username)
            return data
        else:
            logger.error("Login failed for user: %s. Status: %s - %s", username, response.status_code, response.text)
            return None

    except Exception as e:
        logger.exception("Exception occurred during login for user: %s", username)
        return None


def get_authenticated_user(access_token: str):
    try:
        response = requests.get(
            ME_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )

        if response.status_code == 200:
            user_data = response.json()
            logger.info("Fetched authenticated user details successfully.")
            return user_data
        else:
            logger.error("Failed to fetch authenticated user. Status: %s - %s", response.status_code, response.text)
            return None

    except Exception:
        logger.exception("Exception occurred while fetching authenticated user.")
        return None