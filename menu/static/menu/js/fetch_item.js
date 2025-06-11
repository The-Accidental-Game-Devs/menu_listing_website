document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
    });

    // Load categories
    fetchItems()

    // Attach select event to all category selections
    document.getElementById('category').addEventListener('change', function () {
        const search = document.getElementById('search').value;
        const category = this.value;
        fetchItems(search, category);
    });


    // Attach click event to all search buttons
    document.querySelectorAll('.item-search-btn').forEach(button => {
        button.addEventListener('click', function () {
            const search = document.getElementById('search').value;
            const category = document.getElementById('category').value;
            fetchItems(search, category);
        });
    });


    function fetchItems(search = '', category = '') {
        fetch(`/menu/?category=${category}&search=${search}`, {
            headers: {'X-Requested-With': 'XMLHttpRequest'}
        })
            .then(response => response.json())
            .then(data => {
                document.getElementById('item-container').innerHTML = data.html;
            });
    }
});
