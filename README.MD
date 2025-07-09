# Proyecto: Afectación de la Movilidad por Apropiación del Espacio Público en La Estanzuela, Bogotá

## 1. Requisitos y Requerimientos del Proyecto

### Requisitos funcionales:
- Mostrar un mapa interactivo con Leaflet.
- Permitir la visualización de calles afectadas con datos del archivo GeoJSON.
- Capturar información adicional mediante formularios (estrato, estado vía, tipo vía, etc.).
- Al hacer clic sobre una calle, permitir ingresar o ver datos específicos de movilidad.
- Almacenar información en una base de datos SQLite.
- Consultar calles por dirección y mostrar sus características.

### Requisitos no funcionales:
- Aplicación desarrollada en Flask (Python).
- Interfaz responsiva usando HTML, Bootstrap y JavaScript.
- Código mantenible con separación de lógica y vista.
- Persistencia mediante SQLAlchemy.

---

## 2. Arquitectura de Iteraciones y Capas

### Arquitectura general en 4 capas:

- **Frontend:** HTML, Bootstrap, Leaflet.js para visualización de mapas y formularios interactivos.
- **Backend:** Flask (Python) para manejar rutas, lógica y procesamiento de formularios.
- **Base de Datos:** SQLite usando SQLAlchemy para persistencia de datos.
- **API / Comunicación:** Rutas Flask que permiten consulta y envío de datos entre frontend y backend.

### Iteraciones:

#### Iteración 1: Mapa básico + carga de datos estáticos
- Creación del mapa en Leaflet centrado en Bogotá.
- Carga inicial de datos desde GeoJSON (calles.geojson).
- Visualización básica de marcadores con iconos diferenciados.

#### Iteración 2: Integración de base de datos y formularios
- Configuración de SQLite y SQLAlchemy.
- Creación del modelo `Espacio`.
- Formulario para registrar características de una vía.
- Almacenamiento de datos desde formulario.

#### Iteración 3: Consulta por dirección
- Implementación de búsqueda de dirección en GeoJSON.
- Visualización de los atributos en un `popup`.

#### Iteración 4: Mejoras UI/UX
- Formularios desplegables para categorías como estrato, tipo de vía, estado, sentido.
- Opción de seleccionar múltiples rangos horarios.
- Estilizado con Bootstrap.

---

## 3. Avance de Iteraciones

| Iteración | Descripción                                                 |
|-----------|-------------------------------------------------------------|
| 1         | Inicialización de proyecto Flask y mapa Leaflet             |
| 2         | Base de datos integrada y modelo `Espacio` creado           |
| 3         | Consulta de dirección implementada                         |
| 4         | Interfaz mejorada, formularios dropdown y validaciones     |

---

## 4. Cuaderno de Bitácora de Desarrollo

| Actividad                                                    | Responsable |
|--------------------------------------------------------------|-------------|
| Estructura base Flask y rutas iniciales                      | Esteban     |
| Configuración SQLAlchemy y conexión con SQLite               | Esteban     |
| Diseño de modelo de datos y primer formulario                | Esteban     |
| Implementación de lectura GeoJSON y búsqueda de dirección    | Esteban     |
| Mejora UI, dropdowns y selección múltiple en horas pico      | Esteban     |

---

## 5. Artículos Académicos Relevantes

1. **Centro automotriz La Estanzuela: intervención urbano-arquitectónica integral**  
   Analiza la apropiación del espacio público por talleres mecánicos en La Estanzuela y su impacto en la movilidad.  
   [Repositorio Javeriana](https://repository.javeriana.edu.co/handle/10554/39373)

2. **Equipamientos de transporte: experiencias y reflexiones sobre los patio-talleres del SITP**  
   Relaciona el deterioro urbano con la apropiación mecánica del espacio.  
   [Repositorio Javeriana](https://repository.javeriana.edu.co/handle/10554/20879)

3. **Movilidad, espacio público y diseño participativo**  
   Estudia la ocupación de espacio público y su relación con restricciones de movilidad urbana.  
   [Redalyc](https://www.redalyc.org/journal/748/74860961001)

4. **Habitabilidad del espacio público en Bogotá**  
   Expone cómo la ocupación por actores no regulados deteriora las condiciones de tránsito y uso del espacio.  
   [Revistas Javeriana](https://revistas.javeriana.edu.co/index.php/cvyu/article/view/35925/27994)

5. **Atravesando la ciudad: movilidad y experiencia subjetiva del espacio**  
   Narra cómo se afecta la circulación cotidiana de los habitantes por la ocupación informal del espacio público.  
   [Redalyc](https://www.redalyc.org/journal/196/19659113002/html)

---

## 6. AUTOR

**Brayan Esteban Alarcón Galindo**  
**Código:** 20192025144
