import {getCookie} from "./utils.js";

document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('item-container');

    if (!container) {
        console.warn("No #item-container found on this page.");
        return;
    }

    container.addEventListener('click', function (event) {
        const button = event.target.closest('.delete-item-btn');
        if (!button) return;

        const itemId = button.dataset.id;
        const deleteContext = button.dataset.context;
        const confirmed = confirm("Are you sure you want to delete this item?");
        if (!confirmed) return;

        fetch(`/menu/item/${itemId}/delete/`, {
            method: 'POST', headers: {
                'X-CSRFToken': getCookie('csrftoken'), 'X-Requested-With': 'XMLHttpRequest'
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message);

                    if (deleteContext === 'detail') {
                        window.location.href = '/menu/';
                    }

                    button.closest('.item').remove();
                } else {
                    alert(data.message || "Failed to delete item.");
                }
            })
            .catch(error => {
                alert("Error occurred.");
                console.error(error);
            });
    });
});
