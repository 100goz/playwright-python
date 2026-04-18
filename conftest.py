import pytest

def pytest_addoption(parser):
    parser.addoption("--browser-name", action="store", default="chromium")