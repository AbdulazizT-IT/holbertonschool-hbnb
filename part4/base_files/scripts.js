/*
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');

    if (loginForm) {
      loginForm.addEventListener('submit', async (event) => {
        event.preventDefault(); // Page reload is prohibited.

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        await loginUser(email, password);
      });
    }
  });

  async function loginUser (email, password) {
    try {
      const response = await fetch('http://localhost:5000/api/v1/login', { // 👈 غيّر هذا إذا عندك رابط ثاني
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });

      if (response.ok) {
        const data = await response.json();

        // save the token in cookies
        document.cookie = `token=${data.access_token}; path=/;`;

        // We direct the user to the home page.
        window.location.href = 'index.html';
      } else {
      // show the message error
        const errorMessage = document.getElementById('error-message');
        errorMessage.textContent = 'Login failed. Please check your credentials.';
      }
    } catch (error) {
      console.error('Error during login:', error);
      const errorMessage = document.getElementById('error-message');
      errorMessage.textContent = 'An error occurred. Please try again later.';
    }
  }
});
