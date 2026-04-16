from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)

# Project data stored as a list of dictionaries
# This allows the project cards and project details page
# to be generated dynamically in the HTML templates.
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
        "title": "Module 2 JavaScript",
        "description": "BrewLab is a project developed as part of my second module, showcasing my skills in HTML, CSS, and JavaScript. It demonstrates my ability to combine structured design with interactive functionality, creating a dynamic and user-friendly web experience.",
        "tech": "HTML, CSS, JavaScript",
        "link": "https://mariellecabie22-a11y.github.io/BrewLab",
        "category": "javascript",
        "explanation": "This project focused on adding interactivity and dynamic behaviour with JavaScript. I combined structure, styling, and scripting to create a more engaging user experience.",
        "learning": "I learned how JavaScript improves user interaction, and how to connect functionality with frontend design."
    }
]

# Temporary storage for project suggestions submitted by users.
# This data is not saved permanently and will reset when the app restarts.
suggestions_list = []


# Home route
# Renders the main landing page and passes the user's name to the template.
@app.route("/")
def home():
    return render_template("home.html", name="Marielle Cabie")


# Projects route
# Handles both:
# GET  -> displays the project cards and current suggestions
# POST -> receives a new suggestion from the suggestion form
@app.route("/projects", methods=["GET", "POST"])
def projects():
    if request.method == "POST":
        # Get the suggestion entered by the user in the form
        suggestion = request.form.get("suggestion")

        # Only add the suggestion if the input is not empty
        if suggestion:
            suggestions_list.append(suggestion)

    return render_template(
        "projects.html",
        projects=projects_data,
        suggestions=suggestions_list
    )


# Project details route
# Displays more detailed explanations of each project,
# including technologies used and learning outcomes.
@app.route("/project-details")
def project_details():
    return render_template("project_details.html", projects=projects_data)


# About route
# Renders the About page, which can include background information,
# skills, and career goals.
@app.route("/about")
def about():
    return render_template("about.html")


# Contact route
# Handles both:
# GET  -> displays the contact form
# POST -> processes form input and returns a success message
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Retrieve values entered by the user in the form
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Print submitted values to the terminal for testing/debugging
        print(name, email, message)

        # Send the success message and user's name back to the template
        return render_template("contact.html", success="Message sent!", name=name)

    return render_template("contact.html", success=None, name=None)


# Run the Flask development server
# debug=True allows automatic reloading and detailed error messages
if __name__ == "__main__":
    app.run(debug=True)