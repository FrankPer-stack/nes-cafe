// Funciones para el manejo de modales
console.log('Script de modales cargado');

function openModal(modalId) {
    console.log('Abriendo modal:', modalId);
    document.getElementById(modalId).classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeModal(modalId) {
    console.log('Cerrando modal:', modalId);
    document.getElementById(modalId).classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Cerrar modal al hacer clic fuera de él
window.onclick = function(event) {
    if (event.target.classList.contains('fixed')) {
        event.target.classList.add('hidden');
        document.body.style.overflow = 'auto';
    }
}

// tipos de cafe

// tipos de cafe
function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    dropdown.classList.toggle('hidden');
}

function toggleSubMenu(id) {
    const submenu = document.getElementById(id);
    submenu.classList.toggle('hidden');
}

// Cerrar el dropdown cuando se hace clic fuera de él
document.addEventListener('click', function(event) {
    if (!event.target.matches('button') && !event.target.matches('svg') && !event.target.matches('path')) {
        const dropdowns = document.querySelectorAll('[id$="Dropdown"], [id$="Submenu"]');
        dropdowns.forEach(dropdown => {
            if (!dropdown.classList.contains('hidden')) {
                dropdown.classList.add('hidden');
            }
        });
    }
});

// Manejar hover para el submenú
document.addEventListener('DOMContentLoaded', function() {
    const tiposCafeButton = document.querySelector('[onclick="toggleSubMenu(\'tiposCafeSubmenu\')"]');
    const tiposCafeSubmenu = document.getElementById('tiposCafeSubmenu');

    if (tiposCafeButton && tiposCafeSubmenu) {
        // Manejar hover
        tiposCafeButton.addEventListener('mouseenter', function() {
            tiposCafeSubmenu.classList.remove('hidden');
        });

        tiposCafeButton.addEventListener('mouseleave', function(e) {
            // Verificar si el mouse se movió al submenú
            const toElement = e.relatedTarget;
            if (!tiposCafeSubmenu.contains(toElement)) {
                tiposCafeSubmenu.classList.add('hidden');
            }
        });

        tiposCafeSubmenu.addEventListener('mouseleave', function(e) {
            // Verificar si el mouse se movió al botón
            const toElement = e.relatedTarget;
            if (!tiposCafeButton.contains(toElement)) {
                tiposCafeSubmenu.classList.add('hidden');
            }
        });

        // Prevenir que el click en el submenú cierre el menú principal
        tiposCafeSubmenu.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    }
});
