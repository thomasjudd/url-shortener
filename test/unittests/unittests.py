import json
import pytest
import re


def test_index_get(app):
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200


def test_index_post(app):
    client = app.test_client()

    long_url = "www.google.com/search?q=thequickbrownfoxjumpedoverthelazydog",
    data = json.dumps({"url": long_url})
    resp = client.post("/", data=data, follow_redirects=True)

    assert resp.status_code == 200
