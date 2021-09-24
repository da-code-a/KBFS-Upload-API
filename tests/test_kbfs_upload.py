from kbfs_upload import __version__


def test_version():
    assert __version__ == "0.1.0"  # nosec Bandit should ignore this.
