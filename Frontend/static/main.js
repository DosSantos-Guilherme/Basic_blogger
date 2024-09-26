document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    fetch('/api/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, role })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    });
});

document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('profileUsername').value;

    fetch(`/api/profile/${username}`)
    .then(response => response.json())
    .then(data => {
        const profileResult = document.getElementById('profileResult');
        if (data.message) {
            profileResult.textContent = data.message;
        } else {
            profileResult.innerHTML = `
                <p><strong>Username:</strong> ${data.username}</p>
                <p><strong>Role:</strong> ${data.role}</p>
            `;
        }
    });
});
