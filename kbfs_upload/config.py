"""
Load in constants from the environment
variables so that they can be referenced
in the application later.
"""
from os import environ

KBCHAT_TYPE = environ.get("KBFSU_CHAT_TYPE", "silent")
KBCHAT_TEAM = environ.get("KBFSU_CHAT_TEAM")
KBCHAT_TEAM_CHANNEL = environ.get("KBFSU_CHAT_TEAM_CHANNEL", "general")
KBCHAT_USER = environ.get(
    "KBFSU_CHAT_USER", environ.get("KEYBASE_USERNAME")
)  # Send to the user running the app if config unset
if KBCHAT_TYPE not in ["private", "team", "silent"]:
    raise AssertionError(
        "KBFSU_CHAT_TYPE must be one of 'private', 'team', or 'silent'."
    )
if KBCHAT_TYPE == "team" and not KBCHAT_TEAM:
    raise AssertionError("KBFSU_CHAT_TEAM must be set if chat type is team.")
KBFS_SUBDIR = environ.get("KBFSU_FILE_DIR", "")


def build_channel() -> dict:
    """
    Build the appropriate chat API params
    to send to the proper channel based on
    above values.
    """
    from pykeybase import KeybaseChat

    channel = {}
    if KBCHAT_TYPE == "team":
        channel = {
            "name": KBCHAT_TEAM,
            "members_type": "team",
            "topic_name": KBCHAT_TEAM_CHANNEL,
        }
    else:
        channel = {"name": f"{KBCHAT_USER},{KeybaseChat()._get_username()}"}
    return channel
