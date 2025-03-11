document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('message').value,
        number: document.getElementById('number').value
    };
    
    fetch('http://127.0.0.1:5000/send_email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMessage').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});