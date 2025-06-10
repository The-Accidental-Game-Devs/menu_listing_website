import {getCookie} from './utils.js';

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.delete-item-btn').forEach(button => {
        button.addEventListener('click', function () {
            console.log(button.dataset.id);
            const ItemId = this.dataset.id;
            const deleteContext = this.dataset.context;
            const confirmed = confirm("Are you sure you want to delete this item?");
            if (!confirmed) return;

            fetch(`/menu/item/${ItemId}/delete/`, {
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

                        this.closest('.item').remove();
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
});
