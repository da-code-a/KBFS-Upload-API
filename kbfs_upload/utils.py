"""
Utilities for the actual functioning of the app
itself.
"""


def send_chat_notification(
    file_name: str, sender: str, recipient: str, _type: str, _sha256: str
) -> None:
    """
    Send a notification to the chat
    about a new file being uploaded.
    """
    from kbfs_upload.config import build_channel, KBCHAT_TYPE
    from pykeybase import KeybaseChat

    if KBCHAT_TYPE == "silent":
        return

    chat = KeybaseChat()
    message = f"New {_type} upload from {sender}\nFile Name: {file_name}\nSHA256 Checksum: {_sha256}"
    if recipient:
        message += f"\nIntended Recipient: {recipient}"
    channel = build_channel()
    notification_payload = {
        "method": "send",
        "params": {"options": {"channel": channel, "message": {"body": message}}},
    }
    chat._send_chat_api(notification_payload)


def write_file_to_kbfs(file_name: str, contents: bytes) -> None:
    """
    Write the file to KBFS
    """
    from kbfs_upload.config import KBCHAT_TYPE, KBFS_SUBDIR
    from pykeybase import KeybaseFS

    kbfs = KeybaseFS()
    if KBCHAT_TYPE == "team":
        from kbfs_upload.config import KBCHAT_TEAM

        kbfs._mkdir_team(KBFS_SUBDIR, KBCHAT_TEAM)
        kbfs._write_team_file(file_name, contents, KBCHAT_TEAM)
    else:
        from kbfs_upload.config import KBCHAT_USER

        if KBCHAT_USER != kbfs._get_username():
            kbfs._mkdir_shared(KBFS_SUBDIR, [KBCHAT_USER])
            kbfs._write_shared_file(file_name, contents, [KBCHAT_USER])
        else:
            kbfs._mkdir_private(KBFS_SUBDIR)
            kbfs._write_private_file(file_name, contents)


def get_file_sha56(_bytes: bytes) -> str:
    from hashlib import sha256
    from io import BytesIO

    stream = BytesIO(_bytes)
    _sha256 = sha256()
    for block in iter(lambda: stream.read(4096), b""):
        _sha256.update(block)
    return _sha256.hexdigest()


def timestamp_file(filename: str) -> str:
    """
    Returns the filename with a timestamp
    in front of it to prevent duplicate
    filenames from overwriting each other.
    """
    from datetime import datetime

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_")
    return timestamp + filename
