import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}


@pytest.fixture(scope="session")
def base_url():
    return "https://effective-mobile.ru"
