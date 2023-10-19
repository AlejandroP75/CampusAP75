document.addEventListener('DOMContentLoaded', () => {
    let launchList = document.getElementById('launch-list');
    let sortSelect = document.getElementById('sort');
    let sortButton = document.getElementById('sort-button');

    let apiUrl = 'https://api.spacexdata.com/v4/launches';

    function fetchDataAndDisplay(sortBy) {
        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                data.sort((a, b) => {
                    if (sortBy === 'name') {
                        return a.name.localeCompare(b.name);
                    } else if (sortBy === 'date_utc') {
                        return new Date(a.date_utc) - new Date(b.date_utc);
                    } else if (sortBy === 'success') {
                        return a.success - b.success;
                    }
                });
                launchList.innerHTML = '';
                data.forEach(launch => {
                    let li = document.createElement('li');
                    li.innerHTML = `<strong>Misión:</strong> ${launch.name}<br>
                                    <strong>Fecha de Lanzamiento:</strong> ${new Date(launch.date_utc).toDateString()}<br>
                                    <strong>Éxito:</strong> ${launch.success ? 'Sí' : 'No'}`;
                    launchList.appendChild(li);
                });
            })
            .catch(error => console.error('Error al cargar la API de SpaceX:', error));
    }
    sortButton.addEventListener('click', () => {
        let sortBy = sortSelect.value;
        fetchDataAndDisplay(sortBy);
    });
    fetchDataAndDisplay('name');
});
