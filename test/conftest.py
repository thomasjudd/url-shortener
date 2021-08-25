from project.app import create_app
import pytest


@pytest.fixture
def app():
    """
    Defines a test fixture and instantiates variables used in functional tests

    Args:
        None

    Returns:
        instance of the flask object

    Raises:
        Nothing
    """
    app = create_app()
    return app
