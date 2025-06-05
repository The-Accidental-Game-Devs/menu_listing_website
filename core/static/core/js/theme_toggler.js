// theme_toggler.js
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const html = document.documentElement;

// Load saved theme or default to light
let theme = localStorage.getItem('bs-theme') || 'light';
html.setAttribute('data-bs-theme', theme);
themeIcon.className = theme === 'dark' ? 'bi bi-sun' : 'bi bi-moon';

if (themeToggle) {
    themeToggle.addEventListener('click', function (event) {
        event.preventDefault();
        theme = html.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light';
        html.setAttribute('data-bs-theme', theme);
        localStorage.setItem('bs-theme', theme);
        themeIcon.className = theme === 'dark' ? 'bi bi-sun' : 'bi bi-moon';
    });
}
