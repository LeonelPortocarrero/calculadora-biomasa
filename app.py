
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Biomasa",
    page_icon="🌱",
    layout="centered"
)

# Encabezado
st.title("Calculadora de Biomasa y Biogás")
st.write("Proyecto de Programación - Ingeniería de la Energía")

st.info(
    "Estima la producción de biogás y el potencial energético "
    "a partir de residuos orgánicos animales."
)

# Ingreso de datos
st.header("1. Ingreso de biomasa")

cuyes = st.number_input(
    "Estiércol de cuyes (kg/día)",
    min_value=0.0,
    value=0.0,
    step=0.5
)

cerdos = st.number_input(
    "Estiércol de cerdos (kg/día)",
    min_value=0.0,
    value=0.0,
    step=0.5
)

vacas = st.number_input(
    "Estiércol de vacas (kg/día)",
    min_value=0.0,
    value=0.0,
    step=0.5
)

# Rendimientos de referencia ajustables
st.header("2. Parámetros de cálculo")

st.caption(
    "Los siguientes rendimientos son valores ilustrativos "
    "para fines académicos, no resultados experimentales."
)

with st.expander("Modificar rendimientos de biogás"):
    r_cuy = st.number_input(
        "Cuyes (m³/kg)",
        min_value=0.0,
        value=0.030,
        format="%.3f"
    )

    r_cerdo = st.number_input(
        "Cerdos (m³/kg)",
        min_value=0.0,
        value=0.050,
        format="%.3f"
    )

    r_vaca = st.number_input(
        "Vacas (m³/kg)",
        min_value=0.0,
        value=0.020,
        format="%.3f"
    )

poder_calorifico = st.number_input(
    "Poder calorífico estimado (kWh/m³)",
    min_value=0.0,
    value=6.0,
    step=0.1
)

# Función de cálculo
def calcular_biogas(cuyes, cerdos, vacas):
    biomasa = cuyes + cerdos + vacas

    biogas_cuyes = cuyes * r_cuy
    biogas_cerdos = cerdos * r_cerdo
    biogas_vacas = vacas * r_vaca

    biogas_total = (
        biogas_cuyes +
        biogas_cerdos +
        biogas_vacas
    )

    litros = biogas_total * 1000
    energia = biogas_total * poder_calorifico

    return biomasa, biogas_total, litros, energia

# Botón para calcular
st.header("3. Resultados")

if st.button("Calcular producción", type="primary"):

    biomasa, biogas, litros, energia = calcular_biogas(
        cuyes, cerdos, vacas
    )

    if biomasa == 0:
        st.warning("Ingrese una cantidad de biomasa.")
    else:
        st.success("Cálculo realizado correctamente")

        st.metric(
            "Biomasa total",
            f"{biomasa:.2f} kg/día"
        )

        st.metric(
            "Producción de biogás",
            f"{litros:.2f} litros/día"
        )

        st.metric(
            "Biogás en metros cúbicos",
            f"{biogas:.3f} m³/día"
        )

        st.metric(
            "Potencial energético térmico",
            f"{energia:.2f} kWh/día"
        )

        st.caption(
            "Resultados teóricos. La producción real depende "
            "del tipo de estiércol, materia orgánica, "
            "temperatura y condiciones del biodigestor."
        )

# Información educativa
st.header("4. ¿Qué es la biomasa?")

st.write(
    "La biomasa es materia orgánica que puede aprovecharse "
    "para producir energía. Mediante digestión anaerobia, "
    "los residuos animales pueden generar biogás."
)

st.header("5. Aplicación energética")

st.write(
    "El biogás puede utilizarse como combustible para "
    "cocinar, producir calor o generar electricidad "
    "mediante sistemas adecuados."
)

st.divider()
st.caption("Proyecto académico - Calculadora de Biomasa")
