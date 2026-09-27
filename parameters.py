import streamlit as st


# =========================================================
# PARAMETER DATA
# =========================================================

PARAMETERS = [

    # =====================================================
    # VEHICLE
    # =====================================================

    (
        "Vehicle",
        "Vehicle mass",
        "<i>m</i>",
        "kg",
        "Total mass of the vehicle or locomotive.",
    ),

    (
        "Vehicle",
        "Adhesive weight",
        "<i>W</i><sub>a</sub>",
        "N",
        "Weight carried by the powered or driving wheels.",
    ),

    (
        "Vehicle",
        "Number of powered axles",
        "<i>n</i><sub>a</sub>",
        "—",
        "Number of axles driven by the powertrain.",
    ),

    (
        "Vehicle",
        "Wheel diameter",
        "<i>D</i>",
        "m",
        "Diameter of the driving wheel.",
    ),

    (
        "Vehicle",
        "Wheel radius",
        "<i>r</i>",
        "m",
        "Radius of the driving wheel.",
    ),

    # =====================================================
    # PRIME MOVER
    # =====================================================

    (
        "Prime mover",
        "Prime mover power",
        "<i>P</i><sub>pm</sub>",
        "W / kW",
        "Power supplied by the prime mover.",
    ),

    (
        "Prime mover",
        "Prime mover speed",
        "<i>N</i><sub>pm</sub>",
        "rpm",
        "Rotational speed of the prime mover.",
    ),

    (
        "Prime mover",
        "Prime mover torque",
        "<i>T</i><sub>pm</sub>",
        "N·m",
        "Torque produced by the prime mover.",
    ),

    (
        "Prime mover",
        "Prime mover efficiency",
        "<i>η</i><sub>pm</sub>",
        "%",
        "Efficiency of the prime mover.",
    ),

    # =====================================================
    # POWERTRAIN
    # =====================================================

    (
        "Powertrain",
        "Gear ratio",
        "<i>G</i>",
        "—",
        "Ratio between input speed and output speed of the transmission.",
    ),

    (
        "Powertrain",
        "Powertrain efficiency",
        "<i>η</i><sub>pt</sub>",
        "%",
        "Overall efficiency of power transmission to the driving wheels.",
    ),

    (
        "Powertrain",
        "Wheel torque",
        "<i>T</i><sub>w</sub>",
        "N·m",
        "Torque available at the driving wheel.",
    ),

    (
        "Powertrain",
        "Number of powered wheels",
        "<i>n</i><sub>w</sub>",
        "—",
        "Number of wheels receiving torque from the powertrain.",
    ),

    # =====================================================
    # OPERATING CONDITIONS
    # =====================================================

    (
        "Operating condition",
        "Vehicle speed",
        "<i>v</i>",
        "m/s or km/h",
        "Linear speed of the vehicle.",
    ),

    (
        "Operating condition",
        "Acceleration",
        "<i>a</i>",
        "m/s<sup>2</sup>",
        "Rate of change of vehicle speed.",
    ),

    (
        "Operating condition",
        "Gradient",
        "<i>i</i>",
        "% or ‰",
        "Longitudinal inclination of the track.",
    ),

    (
        "Operating condition",
        "Gradient angle",
        "<i>θ</i>",
        "°",
        "Angle of inclination of the track.",
    ),

    # =====================================================
    # RESISTANCE
    # =====================================================

    (
        "Resistance",
        "Rolling resistance coefficient",
        "<i>C</i><sub>rr</sub>",
        "—",
        "Dimensionless coefficient representing rolling resistance.",
    ),

    (
        "Resistance",
        "Rolling resistance",
        "<i>F</i><sub>rr</sub>",
        "N",
        "Resistance caused by rolling losses.",
    ),

    (
        "Resistance",
        "Aerodynamic drag",
        "<i>F</i><sub>aero</sub>",
        "N",
        "Resistance caused by air acting on the vehicle.",
    ),

    (
        "Resistance",
        "Grade resistance",
        "<i>F</i><sub>g</sub>",
        "N",
        "Resistance caused by the component of vehicle weight acting along the gradient.",
    ),

    (
        "Resistance",
        "Curve resistance",
        "<i>F</i><sub>c</sub>",
        "N",
        "Additional resistance caused by track curvature.",
    ),

    # =====================================================
    # AERODYNAMICS
    # =====================================================

    (
        "Aerodynamics",
        "Coefficient of drag",
        "<i>C</i><sub>d</sub>",
        "—",
        "Dimensionless coefficient representing the aerodynamic characteristics of the vehicle.",
    ),

    (
        "Aerodynamics",
        "Frontal area",
        "<i>A</i>",
        "m<sup>2</sup>",
        "Projected frontal area exposed to the airflow.",
    ),

    (
        "Aerodynamics",
        "Air density",
        "<i>ρ</i>",
        "kg/m<sup>3</sup>",
        "Density of the surrounding air.",
    ),

    (
        "Aerodynamics",
        "Wind speed",
        "<i>v</i><sub>w</sub>",
        "m/s",
        "Wind speed relative to the vehicle.",
    ),

    # =====================================================
    # ADHESION
    # =====================================================

    (
        "Adhesion",
        "Adhesion coefficient",
        "<i>μ</i>",
        "—",
        "Coefficient representing the available wheel–rail adhesion.",
    ),
]


# =========================================================
# DISPLAY PARAMETER TABLE
# =========================================================

def show_parameter_table():

    rows = ""

    for category, parameter, symbol, unit, description in PARAMETERS:

        rows += f"""
        <tr>

            <td class="category">
                {category}
            </td>

            <td>
                {parameter}
            </td>

            <td class="symbol">
                {symbol}
            </td>

            <td class="unit">
                {unit}
            </td>

            <td>
                {description}
            </td>

        </tr>
        """

    # =====================================================
    # TABLE HTML + CSS
    # =====================================================

    html = f"""
    <style>

    /* =================================================
       PARAMETER TABLE
       ================================================= */

    .parameter-table {{

        width: 100%;

        border-collapse: collapse;

        margin-top: 15px;
        margin-bottom: 20px;

        font-family:
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            Roboto,
            Arial,
            sans-serif;

        font-size: 14px;

        color:
            var(--text-color);

        background-color:
            var(--background-color);
    }}


    /* =================================================
       TABLE HEADER
       ================================================= */

    .parameter-table th {{

        padding: 12px 14px;

        text-align: left;

        font-weight: 700;

        color:
            var(--text-color);

        background-color:
            var(--secondary-background-color);

        border-bottom:
            2px solid
            var(--border-color);
    }}


    /* =================================================
       TABLE CELLS
       ================================================= */

    .parameter-table td {{

        padding: 10px 14px;

        color:
            var(--text-color);

        background-color:
            var(--background-color);

        border-bottom:
            1px solid
            var(--border-color);

        vertical-align: middle;
    }}


    /* =================================================
       HOVER EFFECT
       ================================================= */

    .parameter-table tr:hover td {{

        background-color:
            var(--secondary-background-color);
    }}


    /* =================================================
       CATEGORY
       ================================================= */

    .category {{

        font-weight: 600;
    }}


    /* =================================================
       SYMBOL
       ================================================= */

    .symbol {{

        font-family:
            "Times New Roman",
            Georgia,
            serif;

        font-size: 18px;

        white-space: nowrap;
    }}


    /* =================================================
       UNIT
       ================================================= */

    .unit {{

        white-space: nowrap;
    }}

    </style>


    <table class="parameter-table">

        <thead>

            <tr>

                <th>
                    Category
                </th>

                <th>
                    Parameter
                </th>

                <th>
                    Symbol
                </th>

                <th>
                    Unit
                </th>

                <th>
                    Description
                </th>

            </tr>

        </thead>


        <tbody>

            {rows}

        </tbody>

    </table>
    """

    st.html(html)