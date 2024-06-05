document.addEventListener('DOMContentLoaded', function() {
  function iniciarSesion(event) {
    event.preventDefault();
    
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    fetch('http://localhost/autenticar_usuario.php', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: email, password: password })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Credenciales incorrectas');
      }
      return response.json();
    })
    .then(data => {
      if (data.exito) {
        window.location.href = "/panel/";
      } else {
        alert(data.mensaje);
      }
    })
    .catch(error => {
      alert(error.message);
    });
  }

  document.getElementById('login-form').addEventListener('submit', iniciarSesion);
});
