from flask import Flask, render_template, request, redirect
from  models import  *
import re

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


@app.route("/signup")
def login():
    error = request.args['error']
    return render_template("login.html", error=error)


@app.route('/signup/action', methods=['POST'])
def action():
    data = request.form.to_dict()
    emailRegx = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(emailRegx, data['email']):
        return redirect("/signup?error=Email is not valid")
    if data['password'] != data['confirm']:
        return redirect("/signup?error=Password should be match")
    if len(data['password']) < 6:
        return redirect("/signup?error=Password should be at least six character long")
    return render_template("index.html")


if __name__ == '__main__':
    app.run("192.168.8.187")
