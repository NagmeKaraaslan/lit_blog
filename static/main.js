document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('newPost');
})

function creatNewPost(title, content) {
    /* console.log('Yeni Post:',{tite, content}); */
}

document.querySelectorAll('.post').forEach(post => {
    post.addEventListener('mouseenter', () => {
        document.querySelectorAll('.canBlurImage').forEach(img => {
            img.style.filter = 'blur(3px)';
        });
    });

    post.addEventListener('mouseleave', () => {
        document.querySelectorAll('.canBlurImage').forEach(img => {
            img.style.filter = 'none';
        });
    });
});