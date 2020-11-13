from flask import Flask, render_template, request
from  models import  *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", url=request.base_url)


@app.route("/classes/<department>")
def classes(department):
    k = klasses()
    cls = k.getKlassByDepartment(department)
    return render_template("klasses.html", cls=cls)

@app.route("/classes/kourses/<klass>")
def kourses(klass):
    c = courses()
    kes = c.getByClassId(klass)
    print(kes)
    return render_template("courses.html", kes=kes)


if __name__ == '__main__':
    app.run("192.168.8.187")
