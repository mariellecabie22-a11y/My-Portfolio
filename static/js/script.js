// Wait until the DOM is fully loaded before running scripts
document.addEventListener("DOMContentLoaded", function () {

    // Select all links on the page
    const links = document.querySelectorAll("a");

    // Add hover effect to links (changes opacity)
    links.forEach(link => {
        link.addEventListener("mouseenter", () => {
            link.style.opacity = "0.8";
        });

        link.addEventListener("mouseleave", () => {
            link.style.opacity = "1";
        });
    });

    // Select theme toggle button
    const toggleBtn = document.getElementById("theme-toggle");

    // Toggle light mode when button is clicked
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            document.body.classList.toggle("light-mode");
        });
    }

    // Select form (used in contact page)
    const form = document.querySelector("form");

    // Display confirmation message when form is submitted
    if (form) {
        form.addEventListener("submit", () => {
            alert("Message sent successfully!");
        });
    }
});


// Function to filter projects by category
function filterProjects(category) {

    // Select all project cards
    const cards = document.querySelectorAll(".card");

    // Loop through each card and show/hide based on category
    cards.forEach(card => {
        if (category === "all" || card.classList.contains(category)) {
            card.style.display = "block"; // Show matching cards
        } else {
            card.style.display = "none"; // Hide non-matching cards
        }
    });
}