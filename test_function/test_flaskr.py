import pytest
from app import create_article



@pytest.fixture
def client():
    create_article.app.config['DATABASE'] = True
    create_article.app.config['TESTING'] = True

    with create_article.app.test_client() as client:
        with create_article.app.app_context():
            create_article.init_db()
        yield client


