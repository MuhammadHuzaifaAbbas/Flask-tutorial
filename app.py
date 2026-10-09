from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Huzaifa Abbas"
@app.route("/users")
def users():
    return "welcome users"
@app.route("/user/<name>")
def user(name):
    return f"welcome {name}"
@app.route("/about")
@app.route("/student/<name>/<course>")
def student(name,course):
    return f" {name} is learning {course}"
def about():
    return "welcome to about page"
@app.route("/contact")
def contact():
    return"welcome to contact page"
if __name__=="__main__":
    app.run(debug=True)