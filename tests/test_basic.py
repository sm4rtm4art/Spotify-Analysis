"""Basic tests to verify CI pipeline functionality."""


def test_imports():
    """Test that main imports work correctly."""
    try:
        import spotify

        assert spotify is not None
    except ImportError as err:
        raise AssertionError("Failed to import the spotify package") from err


def test_basic_functionality():
    """A placeholder test for basic functionality."""
    assert True, "This test should always pass"
