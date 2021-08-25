import pytest
import re


def test_url_generation(app):
    long_urls = [
        "www.google.com/search?q=firefox",
        "www.reddit.com/r/all"
    ]

    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
