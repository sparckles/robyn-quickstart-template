from robyn import Robyn, jsonify
from robyn.templating import JinjaTemplate


app = Robyn(__file__)


@app.get('/')
def hello(request):
    JINJA_TEMPLATE = JinjaTemplate("templates")
    template = JINJA_TEMPLATE.render_template("index.html", title="Hello")
    return template



if __name__ == "__main__":
    app.add_directory(
        route="/static",
        directory_path="static",
    )
    app.start(port=8080)