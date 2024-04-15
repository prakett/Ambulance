document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code here
    function addData(event) {
        event.preventDefault(); // Prevent form submission from reloading the page
        var email = document.getElementById('email').value;
        var password = document.getElementById('pass').value;

        // Store data in local storage
        localStorage.setItem('userEmail', email);
        localStorage.setItem('userPass', password);

        // Optionally, you can clear the form fields after storing the data
        document.getElementById('email').value = '';
        document.getElementById('pass').value = '';

        // Optional: Provide feedback to the user
        alert('Registration successful! Your data has been stored locally.');
    }

    // Attach the addData function to the form's submit event
    document.getElementById('registrationForm').addEventListener('submit', addData);
});
