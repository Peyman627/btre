const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
    $('#message').fadeOut();
}, 3000);