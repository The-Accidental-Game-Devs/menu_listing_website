document.addEventListener("DOMContentLoaded", function () {
    document.querySelector('form').addEventListener('submit', function (e) {
        e.preventDefault();
    });
    // Load categories
    fetchCategories(
        document.getElementById('search').value,
        false
    )

    // Handle back/forward browser navigation
    window.addEventListener('popstate', function () {
        const params = new URLSearchParams(window.location.search);
        const search = params.get('search') || '';
        fetchCategories(search, false); // don't push the state again
    });


    // Attach click event to all search buttons
    document.querySelectorAll('.item-search-btn').forEach(button => {
        button.addEventListener('click', function () {
            const search = document.getElementById('search').value;
            fetchCategories(search);
        });
    });

    function fetchCategories(search = '', push = true) {
        // Update the URL without reloading the page
        const newUrl = `/menu/category/?search=${encodeURIComponent(search)}`;

        if (push) {
            history.pushState(null, '', newUrl);
        }

        fetch(newUrl, {
            headers: {'X-Requested-With': 'XMLHttpRequest'}
        })
            .then(response => {
                const contentType = response.headers.get('content-type');
                if (contentType && contentType.includes('application/json')) {
                    return response.json();
                } else {
                    // Fallback: full page reload
                    window.location.href = newUrl;
                }
            })
            .then(data => {
                if (data && data.html) {
                    document.getElementById('category-container').innerHTML = data.html;
                }
            })
    }
});
