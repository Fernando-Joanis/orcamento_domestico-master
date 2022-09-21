import pytest
from api import create_app


@pytest.fixture(scope='module')
def app():
    """Test instance flask app"""
    return create_app()
