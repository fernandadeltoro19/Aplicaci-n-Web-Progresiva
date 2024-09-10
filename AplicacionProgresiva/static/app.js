document.addEventListener('DOMContentLoaded', async () => {
    // Obtener datos al cargar la página
    const response = await fetch('/api/data');
    const result = await response.json();
    document.getElementById('data').innerText = result.data;

    // Manejar el envío del formulario
    const form = document.getElementById('dataForm');
    form.addEventListener('submit', async (event) => {
        event.preventDefault();  // Prevenir recarga de la página
        
        // Obtener los valores introducidos
        const name = document.getElementById('name').value;
        const career = document.getElementById('career').value;
        
        // Enviar los datos al servidor usando Fetch API
        const response = await fetch('/api/data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: name, career: career }),
        });
        
        const result = await response.json();
        
        // Actualizar la pantalla con los datos nuevos
        document.getElementById('data').innerText = result.data;
        
        // Limpiar el formulario
        form.reset();
    });
});
