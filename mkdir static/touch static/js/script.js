document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        fetch('/generate_meme', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const img = document.createElement('img');
            img.src = url;
            img.style.maxWidth = '100%';
            img.style.marginTop = '20px';
            document.body.appendChild(img);
        })
        .catch(error => console.error('Error:', error));
    });
});
