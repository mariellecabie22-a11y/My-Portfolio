document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll("a");

    links.forEach(link => {
        link.addEventListener("mouseenter", () => {
            link.style.opacity = "0.8";
        });

        link.addEventListener("mouseleave", () => {
            link.style.opacity = "1";
        });
    });

    const toggleBtn = document.getElementById("theme-toggle");
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            document.body.classList.toggle("light-mode");
        });
    }

    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", () => {
            alert("Message sent successfully!");
        });
    }
});

function filterProjects(category) {
    const cards = document.querySelectorAll(".card");

    cards.forEach(card => {
        if (category === "all" || card.classList.contains(category)) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}