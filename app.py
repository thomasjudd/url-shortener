from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from urllib.parse import urlparse
from wtforms import StringField
from wtforms.validators import DataRequired
import random

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
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
            short_url = generate_short_url(long_url)
            return f"{ short_url }"
        else:
            return "not a valid url"


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
        parsed = urlparse(url)
    except Exception as e:
        print(e)
        return False

    print(parsed)
    if parsed.path is None:
        return False

    return True


def generate_short_url(url: str):
    """
    Generates a short URL from the passed url argument

    Args:
       String containing the long URL 

    Returns:
        Shortened url

    Raises:
        None
    """

    return url

    # retrieve slug
#
#    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    shortcode_length = 6
#
#    shortcode = ""
#    for i in range(shortcode_length):
#        shortcode.append(random.choice(charset))
#
#    return f"{url.split('/')[0]}{ shortcode }"


class URLForm(FlaskForm):
    """
    A class representing our URLForm. Extends FlaskForm
    """
    url = StringField('url', validators=[DataRequired()])


if __name__ == "__main__":
    app.config.update(dict(
        SECRET_KEY="pineappleyogafrenchpresscottoncandy",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    app.run()
