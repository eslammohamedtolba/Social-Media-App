document.addEventListener('DOMContentLoaded', () => {
    const profileButton = document.getElementById('profileButton');
    const popup = document.getElementById('popup');
    const close = document.getElementById('close');

    profileButton.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevents the click event from propagating to the document
        togglePopup();
    });

    close.addEventListener('click', () => {
        togglePopup();
    });

    document.addEventListener('click', (e) => {
        if (popup.style.display === 'block' && !popup.contains(e.target) && e.target !== profileButton) {
            popup.style.display = 'none';
        }
    });

    function togglePopup() {
        popup.style.display = popup.style.display === 'block' ? 'none' : 'block';
    }
});
