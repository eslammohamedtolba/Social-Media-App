document.addEventListener('DOMContentLoaded', function () {
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
