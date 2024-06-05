function registrarUsuario() {
  const nombre = document.getElementById('nombre').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const confirmarPassword = document.getElementById('confirmar-password').value;

  if (!nombre || !email || !password || !confirmarPassword) {
    alert('Por favor, completa todos los campos.');
    return;
  }

  if (password !== confirmarPassword) {
    alert('Las contraseñas no coinciden.');
    return;
  }

  const xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://localhost/registrar_usuario.php', true);

  const formData = new FormData();
  formData.append('nombre', nombre);
  formData.append('email', email);
  formData.append('password', password);

  xhr.onload = function() {
    if (xhr.status === 200) {
      const respuesta = JSON.parse(xhr.responseText);
      if (respuesta.exito) {
        alert('¡Usuario registrado exitosamente!');
        limpiarFormulario();
        // Desactivar el botón después del primer envío
        document.getElementById('button-area').disabled = true;
      } else {
        alert('Error al registrar el usuario: ' + respuesta.mensaje);
      }
    } else {
      alert('Error al enviar los datos.');
    }
  };

  xhr.send(formData);
}

function limpiarFormulario() {
  document.getElementById('nombre').value = '';
  document.getElementById('email').value = '';
  document.getElementById('password').value = '';
  document.getElementById('confirmar-password').value = '';
}
