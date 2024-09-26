document.getElementById('submitBtn').addEventListener('click', function(event) {
    const description = document.getElementById('description').value;
    const wordCount = description.trim().split(/\s+/).length;
    
    if (wordCount < 20) {
        event.preventDefault();

        const notification = document.getElementById('notification');
        notification.classList.add('show');

        setTimeout(function() {
            notification.classList.remove('show');
        }, 3000);
    }
});