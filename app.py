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
    return render_template("courses.html", kes=kes)


@app.route("/res/<course>")
def res(course):
    r = resources()
    resource = r.getByCourseId(course)
    return render_template("resources.html", resource=resource)


if __name__ == '__main__':
    app.run("192.168.8.187")
