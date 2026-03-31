from flask import Flask, render_template, request

app = Flask(__name__)

projects_data = [
    {
        "title": "Module 1 Web Design",
        "description": "A website created for an alternative band, Deadlands. This project demonstrates my ability to structure content, apply styling, and design an engaging user interface.",
        "tech": "HTML, CSS",
        "link": "https://mariellecabie22-a11y.github.io/Deadlands",
        "category": "webdesign" 
    },
    {
        "title": "Module 2 Javascript",
        "description": "BrewLab is a project developed as part of my second module, showcasing my skills in HTML, CSS, and JavaScript. It demonstrates my ability to combine structured design with interactive functionality, creating a dynamic and user-friendly web experience.",
        "tech": "HTML, CSS, JavaScript",
        "link": "https://mariellecabie22-a11y.github.io/BrewLab",
        "category": "JavaScript"
    }
]

@app.route("/")
def home():
    return render_template("home.html", name="Marielle Cabie")

@app.route("/projects")
def projects():
    return render_template("projects.html", projects=projects_data)

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print(name, email, message)
        return render_template("contact.html", success="Message sent!")

    return render_template("contact.html", success=None)

if __name__ == "__main__":
    app.run(debug=True)