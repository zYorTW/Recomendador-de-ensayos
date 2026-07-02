# Punto de entrada principal.
# Re-exporta todo lo necesario para que los tests existentes sigan
# funcionando sin cambios (import from recomendador_nuevo).

import sys
from pathlib import Path

# Agrega la subcarpeta modulos/ al path para que Python encuentre los módulos
_modulos_dir = Path(__file__).resolve().parent / "modulos"
if str(_modulos_dir) not in sys.path:
    sys.path.insert(0, str(_modulos_dir))

from recomendador_config import (  # noqa: F401
    BASE_DIR, ARCHIVO_HISTORICO, ARCHIVO_MODELO, ARCHIVO_MODELOS,
    HOJA_HISTORICO, HOJA_MODELO, RANDOM_SEED, UMBRAL, PKL_VERSION,
    MAX_COMBINACIONES_EXACTAS, MAX_COMBINACIONES_EVALUAR,
    REGLAS_PROYECTO, PROYECTOS_MODELO_PROPIO,
    TARGET_AQ, TARGET_AR, COLUMNA_PROYECTO, COLUMNA_UNIDAD,
    COLUMNAS_CATEGORICAS, COLUMNAS_NUMERICAS,
    COLUMNAS_NUMERICAS_SECUNDARIAS, COLUMNAS_CATEGORICAS_SECUNDARIAS,
    VARIABLES_CONTROLABLES, COLUMNAS_HISTORICA_REAL,
    logger,
)
from recomendador_utils import (  # noqa: F401
    normalizar_texto, limpiar_nulos_dataframe,
    limpiar_categorica, limpiar_numerica,
    renombrar_columnas_objetivo, estandarizar_tiempo_mutacion,
    moda_segura, mediana_segura, nearest_existing_value,
    filtrar_opciones_validas_categoricas, filtrar_opciones_validas_numericas,
    etiqueta_cumplimiento, score_objetivo,
    obtener_regla_proyecto, obtener_tipo_modelo,
    aplicar_reglas_proyecto, describir_filtros,
    nombre_archivo_salida,
)
from recomendador_engine import RecomendadorEngine  # noqa: F401
from recomendador_gui import RecomendadorApp        # noqa: F401

if __name__ == "__main__":
    app = RecomendadorApp()
    app.mainloop()
