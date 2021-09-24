# KBFS Upload API

## Purpose

This API can be used to upload either secure notes or files to a secure [KeybaseFS](https://keybase.io) folder. The idea behind it is that files can be stored in a secure, end-to-end encrypted format without having less tech-savvy end users sign up for Keybase. This was created as a work around I needed at work so that coworkers could send me sensitive information in a secure format, but they didn't have Keybase or know how to use GPG. Creating this API and an internal web-page front end for it allowed them to send me this information and have it stored securely without teaching them anything about encryption.

## Usage

### Direct Launch

If you'd like to run this directly using [Poetry](https://python-poetry.org/) to install it. Simply do `poetry install` to install it, then `poetry run kbfsu` to launch it.

### Docker

This is also available as a Docker image. Simply run `docker run -p 5000:5000 -d --restart=always dakotakae/kbfs_upload` to start the server listening on port `5000`.

### Configuration

No matter how you launch it, some configuration will be required. This can all be done with Environment Variables.

|Variable Name          |Data Type|Description                                                                                              |Required                                          |Default                   |
|-----------------------|---------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------|
|KBFSU_CHAT_TYPE        |str      |Type of chat to send notifications to. Can be `private`, `team` or `silent`                              |No                                                |silent                    |
|KBFSU_CHAT_TEAM        |str      |The team that will be used to store the files. The bot must be a member of that team (not just installed)|Yes, if `KBFSU_CHAT_TYPE` is `team`               |none                      |
|KBFSU_CHAT_TEAM_CHANNEL|str      |The team chat channel to send notifications to.                                                          |No                                                |general                   |
|KBFSU_CHAT_USER        |str      |The user to sharefiles with                                                                              |Yes, if `KBFSU_CHAT_TYPE` is `private` or `silent`|Same as `KEYBASE_USERNAME`|
|KBFSU_FILER_DIR        |str      |The subdirectory path to store files in.                                                                 |No                                                |none                      |
|KEYBASE_USERNAME       |str      |The username to log into Keybase with                                                                    |Yes                                               |none                      |
|KEYBASE_PAPERKEY       |str      |The paperkey to use to log the user into Keybase                                                         |Yes                                               |none                      |


### API Interaction

The API accepts `POST` requests to `/upload/<type>`, where `type` is either `note` or `file`. Both types accept `form-data` as the input. Both types also require the following form entries:

* `filename` - The name to save the file to. This filename will be sanitized and timestamped after the fact, but is still required.
* `sender` - The name of the person submitting the form.

You can also send `recipient` to identify the intended recipient of the file. This is an arbitrary string and does not have to be a particular Keybase username.

If `type` is `note`, the request also needs to include a `body` field that contains the text to be stored. If the `type` is `file`, the uploaded file must be sent with the `file` key.

This is all the reference needed to build your own front-end for this api.

## Development/Contribution

As stated before, Poetry is used to manage the project. If there are any improvements/changes to be made, feel free to submit a PR.

## Support

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/dakotakae)
