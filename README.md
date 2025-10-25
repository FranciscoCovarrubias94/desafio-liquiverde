# desafio-liquiverde

## Backend
1. Crear entorno virtual:
```
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python -m app.db 
python -m app.load_sample_data #para cargar datos de ejemplo
uvicorn app.main:app --reload --port 8000
```

## **Configuración de APIs y variables de entorno**

## Algoritmos implementados
1. Scoring de productos (compute_product_score): Calcula un puntaje de sostenibilidad para cada producto combinando tres dimensiones: económico (econ), ambiental (env) y social (soc). Económico favorece precios bajos, ambiental premia menor huella de carbono y social considera atributos como empaques reciclables. Cada dimensión se normaliza entre 0 y 100 y se pondera según los pesos dados, generando un puntaje overall que refleja la sostenibilidad integral del producto.
2. Optimización de lista (knapsack_by_budget): Implementa un algoritmo tipo mochila multi-objetivo para seleccionar productos dentro de un presupuesto limitado. Cada producto recibe un “ratio” que combina utilidad y bajo impacto ambiental (weighted_value) dividido por su precio. Luego se ordenan los productos por este ratio y se agregan a la lista hasta agotar el presupuesto o el límite de ítems, maximizando la sostenibilidad por unidad monetaria gastada.

## Uso de IA
Se utilizó ChatGPT para:
- Asesoramiento en la estructura de backend y frontend.
- Ejemplos de scripts para cargar datos.
- Explicación y optimización de algoritmos de scoring y mochila.

## Extra
No se logro dejar precios finales con datos utiles para mostrar el algoritmo de optimización, aunque se logro apreciar que si 
funcionaba con datos de prueba utilizados anteriormente, como se puede comprobar si se cargan los datos de prueba de la
carpeta dataset