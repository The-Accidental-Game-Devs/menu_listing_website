import {getCookie} from "./utils";

document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('category-container');

    if (!container) {
        console.warn("No #category-container found on this page.");
        return;
    }

    container.addEventListener('click', function (event) {
        const button = event.target.closest('.delete-category-btn');
        if (!button) return;

        const categoryId = button.dataset.id;
        const confirmed = confirm("Are you sure you want to delete this category?");
        if (!confirmed) return;

        fetch(`/menu/category/${categoryId}/delete/`, {
            method: 'POST', headers: {
                'X-CSRFToken': getCookie('csrftoken'), 'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);
                    button.closest('.category').remove();
                } else {
                    alert(data.message || "Failed to delete category.");
                }
            })
            .catch(error => {
                alert("Error occurred.");
                console.error(error);
            });
    });
});
