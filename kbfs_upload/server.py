from flask import Flask, request, Response, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> Response:
    """
    Basic health check to allow
    a ping to return a 200
    """
    return jsonify({"status": "OK"})


@app.route("/upload/<string:_type>", methods=["POST"])
def upload_file(_type: str) -> Response:
    from kbfs_upload.utils import (
        send_chat_notification,
        write_file_to_kbfs,
        timestamp_file,
        get_file_sha56,
    )

    if _type == "note":
        filename = secure_filename(request.form["filename"])
        file_contents = request.form["body"].encode()
    elif _type == "file":
        filename = secure_filename(request.files["file"].filename)
        file_contents = request.files["file"].stream.read()
    filename = timestamp_file(filename)
    _sha256 = get_file_sha56(file_contents)
    write_file_to_kbfs(filename, file_contents)
    send_chat_notification(
        filename, request.form["sender"], request.form.get("recipient"), _type, _sha256
    )
    return jsonify({"status": "complete"})
