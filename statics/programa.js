

    var map = L.map('map').setView([4.6100, -74.0810], 15);
   
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    
    var marker = L.marker([4.6100, -74.081]).addTo(map);

    map.on('click', function (e) {
      var { lat, lng } = e.latlng;
      if (marker) map.removeLayer(marker);
      marker = L.marker([lat, lng]).addTo(map);

      document.getElementById('lat').value = lat;
      document.getElementById('lng').value = lng;
    });

 async function cargarPuntos() {
  try {
    const respuesta = await fetch("calles.geojson");
    const datos = await respuesta.json();
    const listaFeatures = datos.features;

    const infoDiv = document.getElementById("infoPuntos");
    infoDiv.innerHTML = "<h4>Datos cargados:</h4>"; // Título opcional

    for (let i = 0; i < 5 && i < listaFeatures.length; i++) {
      const f = listaFeatures[i];
      const coords = f.geometry.coordinates;
      const props = f.properties;

      // Mostrar marcador en mapa
      const marcador = L.marker(coords.reverse()).addTo(map); // GeoJSON usa [lng, lat]

      // Crear HTML para mostrar propiedades
      let detalles = "<div class='card mb-2 p-2'>";
      for (const clave in props) {
        detalles += `<strong>${clave}:</strong> ${props[clave]}<br>`;
      }
      detalles += "</div>";

      // Añadir al div
      infoDiv.innerHTML += detalles;

      // También puedes mostrarlo en popup del marcador si quieres
      marcador.bindPopup(detalles);
    }
  } catch (error) {
    console.error("Error cargando puntos:", error);
  }
}

cargarPuntos();
