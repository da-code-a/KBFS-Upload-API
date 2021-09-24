"""
KBFS Upload API
---------------

Copyright 2021 Dakota Brown

This is an API for receiving notes or files through and
storing them in an encrypted KBFS folder. Can be used to
send sensitive information to Keybase users when the sender
does not have/want a Keybase account.
"""

__version__ = "0.1.0"


def main():
    """
    Runs the API server.
    """
    from kbfs_upload.server import app
    from dotenv import load_dotenv

    load_dotenv()
    app.run(host="0.0.0.0")  # nosec
