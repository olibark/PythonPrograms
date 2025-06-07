// Select the button element by its ID
const button = document.getElementById('Button');
const button2 = document.getElementById('Button2');
// Add a click event listener to the button
button.addEventListener('click', () => {
    alert('Button was clicked!');
});
button2.addEventListener('click', () => {
    alert2('Button2 was clicked!');
});