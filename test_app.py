def test_import():
    try:
        from app import app
        assert app is not None
    except Exception as e:
        assert False, f"Import failed: {e}"
