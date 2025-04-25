import os

import pytest
from ninja.testing import TestClient

from payment_system_service.api.main import app


def pytest_generate_tests(metafunc):
    os.environ['NINJA_SKIP_REGISTRY'] = 'yes'


@pytest.fixture
def client():
    app.urls_namespace = 'test'
    return TestClient(app)
