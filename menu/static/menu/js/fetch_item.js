document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
    });
    // Load items
    fetchItems(document.getElementById('search').value, document.getElementById('category').value, false // don't pushState because URL is already correct
    );

    // Handle back/forward browser navigation
    window.addEventListener('popstate', function () {
        const params = new URLSearchParams(window.location.search);
        const search = params.get('search') || '';
        const category = params.get('category') || '';
        document.getElementById('search').value = search;
        document.getElementById('category').value = category;
        fetchItems(search, category, false); // don't push the state again
    });


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


    function fetchItems(search = '', category = '', push = true) {
        const newUrl = `/menu/?category=${encodeURIComponent(category)}&search=${encodeURIComponent(search)}`;

        if (push) {
            history.pushState(null, '', newUrl);
        }

        fetch(newUrl, {
            headers: {'X-Requested-With': 'XMLHttpRequest'}
        })
            .then(response => {
                // Check if response is JSON
                const contentType = response.headers.get("content-type");
                if (contentType && contentType.includes("application/json")) {
                    return response.json();
                } else {
                    // Fallback: full page reload
                    window.location.href = newUrl;
                }
            })
            .then(data => {
                if (data && data.html) {
                    document.getElementById('item-container').innerHTML = data.html;
                }
            });
    }

});
