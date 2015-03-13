import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """\
    <html>
      <head></head>
      <body>
        <h2>Hello Russell and friends!</h2>
        <p>Welcome to the new and improved Bus App. It's already better than the last one.<br>
        </p>
      </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
