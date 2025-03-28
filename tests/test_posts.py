import pytest
from posts import get_posts, get_posts_with_comments

def test_get_posts_should_success():
    posts = get_posts()
    assert posts is not None
    assert len(posts) == 60
    assert "title" in posts[0]

def test_get_posts_custom_limit():
    posts = get_posts(limit=10)
    assert posts is not None
    assert len(posts) == 10

def test_posts_with_comments_structure():
    posts = get_posts_with_comments(limit=5)
    assert posts is not None
    for post in posts:
        assert "id" in post
        assert "title" in post
        assert "comments" in post
        if post["comments"]:
            assert "body" in post["comments"][0]
            assert "user" in post["comments"][0]
