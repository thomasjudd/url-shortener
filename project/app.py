from flask import Flask, Blueprint, render_template, request, redirect
from flask_wtf import FlaskForm
from urllib.parse import ParseResult, urlparse
from wtforms import StringField
from wtforms.validators import DataRequired
import random

# Create blueprint to allow us to use Flask App Factory Pattern
urlshortener = Blueprint("urlshortener", __name__)


def create_app():
    app = Flask(__name__)
    app.config.update(dict(
        SECRET_KEY="pineappleyogafrenchpresscottoncandy",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    app.register_blueprint(urlshortener)
    return app


@urlshortener.route('/', methods=['POST', 'GET'])
def index():
    """
    Index page for the application. shows a form to submit a url

    Args:
        None

    Returns:
        A Rendered jinja template containing the form

    Raises:
        None
    """
    form = URLForm()

    if request.method == 'GET':
        return render_template('index.html', form=form)

    if request.method == 'POST':
        long_url = request.form.get('url')
        if form.validate_on_submit() and is_valid_url(str(long_url), str(request.url)):
            short_url = generate_short_path(long_url)
            return f"<a href=\"{request.url}{short_url}\">{request.url}{short_url}</a>"
        else:
            return "not a valid url"


# temporary, probably want to move this to backend storage
shortcode_mappings = {}


@urlshortener.route("/<shortcode>")
def shortcode(shortcode: str):
    """
    Route that handles shortcodes

    Args:
        shortcode in path

    Returns:
        Redirection to shortcode's mapping

    Raises:
        Nothing
    """
    url = shortcode_mappings[shortcode].geturl()
    print(f"Redirecting to {url}")
    return redirect(url, 301)


def get_parsed_url(url: str) -> ParseResult:
    """
    Parses the url argument into a urlparse object

    Args:
        String containing the long url

    Returns:
        URLParse

    Raises:
        Exception
    """
    try:
        if "http" not in url:
            # inject missing protocol to play nicely with urlparse
            url = f"http://{url}"
        parsed = urlparse(url)
    except Exception as e:
        print(e)
        return None
    return parsed


def is_valid_url(url: str, source_url: str) -> bool:
    """
    Validates that the user input has valid url syntax

    Args:
        String containing the long url

    Returns:
        boolean

    Raises:
        Nothing
    """
    try:
        if "http" not in url:
            # inject missing protocol to play nicely with urlparse
            url = f"http://{url}"
        parsed = urlparse(url)
    except Exception as e:
        print(e)
        return False

    try:
        parsed_source_url = urlparse(source_url)
    except Exception as e:
        print(e)
        return False

    return True


def generate_short_path(url: str):
    """
    Generates a short URL from the passed url argument

    Args:
       String containing the long path 

    Returns:
        Shortened url

    Raises:
        None
    """

    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    shortcode_length = 6

    shortcode = "".join(random.choice(charset)
                        for i in range(shortcode_length))

    # store mapping in a dictionary for now
    print("URL: ", url)
    shortcode_mappings[shortcode] = get_parsed_url(url)
    return shortcode


class URLForm(FlaskForm):
    """ A class representing our URLForm. Extends FlaskForm """
    url = StringField('url', validators=[DataRequired()])


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
