import pytest
from posts import get_posts

def test_get_posts_should_success():
    posts = get_posts()
    assert posts is not None
    assert len(posts) == 60
    assert "title" in posts[0]

def test_get_posts_custom_limit():
    posts = get_posts(limit=10)
    assert posts is not None
    assert len(posts) == 10