from flask import Flask, request, send_file, render_template
from hypeddit import get_download_file
import requests
import json
import mimetypes
from io import BytesIO

app = Flask(__name__)

s = requests.session()

@app.route("/")
def main():
    return render_template("index.html")


@app.route("/download")
def hypeddit_grab():
    url = request.args.get("url")

    res = get_download_file(url)

    print(res)
    print(url)

    if not res:
        return "couldn't find a Hypeddit download with that URL"

    r = s.get(res["url"])

    #if ""

    # Guess extension
    if "Content-Type" not in r.headers:
        return f"idk what to do: {json.dumps(r.headers)}"

    guessed_extension = mimetypes.guess_extension(r.headers["Content-Type"])

    print(guessed_extension)


    # Use BytesIO instead of StringIO here.
    buffer = BytesIO()
    buffer.write(r.content)
    # Or you can encode it to bytes.
    # buffer.write('Just some letters.'.encode('utf-8'))
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name=res["file_name_suggestion"] + guessed_extension,
        mimetype=r.headers["Content-Type"]
    )

    #
    # if r.headers["Content-Type"] == "audio/mpeg":
    #     guessed_extension = ".mp3"
    # elif r.headers["Content-Type"] == "audio/wav":
    #
    #     pass
