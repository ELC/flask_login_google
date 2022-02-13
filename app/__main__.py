from . import app

from waitress import serve

if app.config["DEBUG"]:
    app.run()
else:
    serve(app, host="0.0.0.0", port=5000)
