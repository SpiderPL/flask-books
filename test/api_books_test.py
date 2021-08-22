import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# test default limit - 10 rows
def test_limit_results_to_10_by_default(client):
    pass
