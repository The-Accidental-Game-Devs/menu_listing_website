document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
    });
    // Load items
    fetchCategories()

    // Attach click event to all search buttons
    document.querySelectorAll('.item-search-btn').forEach(button => {
        button.addEventListener('click', function () {
            const search = document.getElementById('search').value;
            fetchCategories(search);
        });
    });

    function fetchCategories(search = '') {
        fetch(`/menu/category/?&search=${search}`, {
            headers: {'X-Requested-With': 'XMLHttpRequest'}
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('category-container').innerHTML = data.html;
            });
    }
});
