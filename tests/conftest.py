import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Restore the in-memory activities state before each test."""
    original_state = copy.deepcopy(activities)
    try:
        yield
    finally:
        activities.clear()
        activities.update(copy.deepcopy(original_state))
