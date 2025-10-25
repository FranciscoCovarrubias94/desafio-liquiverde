# desafio-liquiverde

## Backend
1. Crear entorno virtual:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python -m app.db 
python -m app.load_sample_data #para cargar datos de ejemplo
uvicorn app.main:app --reload --port 8000


## **Configuración de APIs y variables de entorno**

## Algoritmos implementados
1. **Scoring de Sostenibilidad**: combina factores económicos, ambientales y sociales para asignar un puntaje global a cada producto.
2. **Optimización de lista (Mochila Multi-objetivo)**: selecciona productos optimizando score global dentro de un presupuesto.

## Uso de IA
Se utilizó ChatGPT para:
- Asesoramiento en la estructura de backend y frontend.
- Ejemplos de scripts para cargar datos.
- Explicación y optimización de algoritmos de scoring y mochila.

##Extra
No se logro dejar precios finales con datos utiles para mostrar el algoritmo de optimización, aunque se logro apreciar que si 
funcionaba con datos de prueba utilizados anteriormente