from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/about/profile")
def about_profile():
    return render_template("about_profile.html")

@app.route("/about/education")
def about_education():
    return render_template("about_education.html")

@app.route("/about/hobbies")
def about_hobbies():
    return render_template("about_hobbies.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)