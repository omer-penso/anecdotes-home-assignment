from auth import login, get_authenticated_user
from posts import get_posts_with_comments

def main():
    print("Starting connectivity test...")
    auth_result = login("emilys", "emilyspass")
    if not auth_result:
        print("Login failed. Please check your credentials.")
        return
    print("Successfully logged in.")

    access_token = auth_result.get("accessToken")
    if not access_token:
        print("Access token not found in login response.")
        return

    user = get_authenticated_user(access_token)
    print("\nAuthenticated user details:")
    print(f"ID: {user.get('id')}")
    print(f"Name: {user.get('firstName')} {user.get('lastName')}")
    print(f"Username: {user.get('username')}")
    print(f"Email: {user.get('email')}")
    print(f"Gender: {user.get('gender')}")
    print(f"Image URL: {user.get('image')}")

    print("\nCollecting posts along with their comments...")
    posts = get_posts_with_comments(limit=60)
    if not posts:
        print("Could not retrieve posts. Please try again later.")
        return

    print(f"Collected {len(posts)} posts with comments.")
    print("\nHere's an example:")
    sample = posts[0]
    print(f"Post ID: {sample['id']}")
    print(f"Title: {sample['title']}")
    print(f"Number of comments: {len(sample['comments'])}")

if __name__ == "__main__":
    main()