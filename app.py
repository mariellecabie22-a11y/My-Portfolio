from flask import Flask, render_template, request

app = Flask(__name__)

projects_data = [
    {
        "title": "Module 1 Web Design",
        "description": "A website created for an alternative band, Deadlands. This project demonstrates my ability to structure content, apply styling, and design an engaging user interface.",
        "tech": "HTML, CSS",
        "link": "https://mariellecabie22-a11y.github.io/Deadlands",
        "category": "webdesign",
        "explanation": "This project focused on creating a visually engaging and responsive website. I developed the layout, styling, and structure using HTML and CSS, while improving my understanding of user interface design and content presentation.",
        "learning": "I learned how to structure a multi-section website, apply consistent styling, and design with the user experience in mind."
    },
    {
        "title": "Module 2 Javascript",
        "description": "BrewLab is a project developed as part of my second module, showcasing my skills in HTML, CSS, and JavaScript. It demonstrates my ability to combine structured design with interactive functionality, creating a dynamic and user-friendly web experience.",
        "tech": "HTML, CSS, JavaScript",
        "link": "https://mariellecabie22-a11y.github.io/BrewLab",
        "category": "javascript",
        "explanation": "This project focused on adding interactivity and dynamic behaviour with JavaScript. I combined structure, styling, and scripting to create a more engaging user experience.",
        "learning": "I learned how JavaScript improves user interaction, and how to connect functionality with frontend design."
    }
]

suggestions_list = []

@app.route("/")
def home():
    return render_template("home.html", name="Marielle Cabie")

@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "POST":
        suggestion = request.form.get("suggestion")
        if suggestion:
            suggestions_list.append(suggestion)

    return render_template(
        "projects.html",
        projects=projects_data,
        suggestions=suggestions_list
    )

@app.route("/project-details")
def project_details():
    return render_template("project_details.html", projects=projects_data)

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
        return render_template("contact.html", success="Message sent!", name=name)

    return render_template("contact.html", success=None, name=None)

if __name__ == "__main__":
    app.run(debug=True)