document.addEventListener('DOMContentLoaded', function () {
    // Create pop up for the post
    const PostButtonBack = document.getElementById('postBotton');
    const Postpopup = document.getElementById('postpopup');
    const PostClose = document.getElementById('postclose');
    PostButtonBack.addEventListener('click', (e) => {
        e.stopPropagation(); // Prevents the click event from propagating to the document
        PostTogglePopup();
    });
    PostClose.addEventListener('click', () => {
        PostTogglePopup();
    });
    document.addEventListener('click', (e) => {
        if (Postpopup.style.display === 'block' && !Postpopup.contains(e.target) && e.target !== PostButtonBack) {
            Postpopup.style.display = 'none';
        }
    });
    function PostTogglePopup() {
        Postpopup.style.display = Postpopup.style.display === 'block' ? 'none' : 'block';
    }

    const likeButtons = document.querySelectorAll('.like-button');
    likeButtons.forEach(button => {
        button.addEventListener('click', async () => {
            const postId = button.getAttribute('data-post-id');
            let likes = parseInt(button.getAttribute('data-likes'));
            if (button.classList.contains('liked')) {
                likes -= 1;
                button.classList.remove('liked');
            } else {
                likes += 1;
                button.classList.add('liked');
            }
            button.setAttribute('data-likes', likes);
            button.querySelector('.like-count').textContent = likes;
        });
    });
});
