document.addEventListener('DOMContentLoaded', () => {
    const profileButtonBack = document.getElementById('uploadBottonBack');
    const popupBack = document.getElementById('profilepopupBack');
    const closeBack = document.getElementById('profilecloseBack');
    const profileButtonFront = document.getElementById('uploadBottonFront');
    const popupFront = document.getElementById('profilepopupFront');
    const closeFront = document.getElementById('profilecloseFront');

    profileButtonBack.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevents the click event from propagating to the document
        togglePopupBack();
    });
    profileButtonFront.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevents the click event from propagating to the document
        togglePopupFront();
    });
    closeBack.addEventListener('click', () => {
        togglePopupBack();
    });
    closeFront.addEventListener('click', () => {
        togglePopupFront();
    });
    document.addEventListener('click', (e) => {
        if (popupBack.style.display === 'block' && !popupBack.contains(e.target) && e.target !== profileButtonBack) {
            popupBack.style.display = 'none';
        }
        if (popupFront.style.display === 'block' && !popupFront.contains(e.target) && e.target !== profileButtonFront) {
            popupFront.style.display = 'none';
        }
    });
    function togglePopupBack() {
        popupBack.style.display = popupBack.style.display === 'block' ? 'none' : 'block';
    }
    function togglePopupFront() {
        popupFront.style.display = popupFront.style.display === 'block' ? 'none' : 'block';
    }
});
