import {getCookie} from './utils.js';

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.delete-category-btn').forEach(button => {
        button.addEventListener('click', function () {
            console.log(button.dataset.id);
            const categoryId = this.dataset.id;
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
                        this.closest('.category').remove();
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
});
