document.addEventListener('DOMContentLoaded', function () {
    const input = document.querySelector('input[type="file"][name="image"]');
    const preview = document.getElementById('image-preview');

    input?.addEventListener('change', function () {
        const [file] = input.files;
        if (file) {
            preview.src = URL.createObjectURL(file);
            preview.style.display = 'block';
        } else {
            preview.style.display = 'none';
            preview.src = '';
        }
    });
});