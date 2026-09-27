import streamlit as st
from pathlib import Path
from parameters import show_parameter_table
import math
from calculator import show_calculator


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Tractive Effort",
    page_icon="🚆",
    layout="wide",
)


# =========================================================
# GLOBAL STYLING
# =========================================================

st.markdown(
    """
<style>

/* =========================================================
   COMPACT GLOBAL SPACING
   ========================================================= */

.stMarkdown {
    margin-bottom: 0.2rem !important;
}

.stMarkdown p {
    margin-top: 0.2rem !important;
    margin-bottom: 0.2rem !important;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3 {
    margin-top: 0.4rem !important;
    margin-bottom: 0.3rem !important;
}


/* =========================================================
   LATEX SPACING
   ========================================================= */

[data-testid="stLatex"] {
    margin-top: -0.15rem !important;
    margin-bottom: -0.15rem !important;
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

[data-testid="stSidebar"] {
    width: 235px !important;
    min-width: 235px !important;
    max-width: 235px !important;

    border-right: 1px solid var(--border-color);
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.4rem;
    padding-left: 0.9rem;
    padding-right: 0.75rem;
}


/* =========================================================
   SIDEBAR TITLE
   ========================================================= */

.sidebar-kicker {
    font-size: 0.62rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;

    opacity: 0.50;

    margin-bottom: 0.15rem;
}

.sidebar-title {
    font-size: 1.05rem;
    font-weight: 750;
    font-style: italic;

    margin-bottom: 1rem;

    padding-bottom: 0.5rem;

    border-bottom: 1px solid var(--border-color);
}


/* =========================================================
   SIDEBAR NAVIGATION
   ========================================================= */

.sidebar-section-label {
    font-size: 0.62rem;
    font-weight: 800;

    text-transform: uppercase;
    letter-spacing: 0.09em;

    opacity: 0.42;

    margin-top: 0.8rem;
    margin-bottom: 0.35rem;
}

.sidebar-link {
    display: block;

    color: var(--text-color) !important;
    text-decoration: none !important;

    font-size: 0.76rem;
    line-height: 1.25;

    padding: 0.42rem 0.45rem;

    margin: 0.08rem 0;

    border-radius: 6px;

    transition:
        background-color 0.15s ease,
        padding-left 0.15s ease;
}

.sidebar-link:hover {
    background: var(--secondary-background-color);

    padding-left: 0.7rem;
}


/* =========================================================
   ARTICLE ANCHORS
   ========================================================= */

.article-anchor {
    position: relative;
    top: -1rem;
}

.calculator-anchor {
    position: relative;
    top: -1rem;
}


/* =========================================================
   EXAMPLE CALCULATION AREA
   ========================================================= */

.calculation-step {
    margin-top: 0.45rem;
    margin-bottom: 0.05rem;

    font-weight: 700;
}

.calculation-note {
    margin-top: 0.2rem;
    margin-bottom: 0.1rem;

    opacity: 0.85;
}


/* =========================================================
   CALCULATION RESULT
   ========================================================= */

.calculation-conclusion {
    margin-top: 0.6rem;
    padding: 0.75rem 1rem;

    border-radius: 10px;

    background: var(--secondary-background-color);

    border-left: 4px solid #2563EB;
}

</style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        """
<div class="sidebar-kicker">
ENGINEERING ARTICLE
</div>

<div class="sidebar-title">
Tractive effort
</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="sidebar-section-label">
Article navigation
</div>

<a class="sidebar-link" href="#definition-of-tractive-effort">
1. Definition of tractive effort
</a>

<a class="sidebar-link" href="#demonstration-of-tractive-effort">
2. Demonstration of tractive effort and resistance forces
</a>

<a class="sidebar-link" href="#parameters-involved">
3. Parameters involved in tractive force calculation
</a>

<a class="sidebar-link" href="#resistive-forces">
4. Resistive forces acting on a vehicle & their formulations
</a>

<a class="sidebar-link" href="#required-tractive-force">
5. Required tractive force for vehicle movement
</a>

<a class="sidebar-link" href="#available-tractive-force">
6. Available tractive force for vehicle movement
</a>

<a class="sidebar-link" href="#example-calculation">
7. Example of tractive effort calculation for a vehicle
</a>

<a class="sidebar-link" href="#tractive-force-calculator">
8. Tractive effort calculator
</a>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# PAGE TITLE
# =========================================================

st.markdown(
    """
<h1 style="
    font-weight: bold;
    white-space: nowrap;
    margin-bottom: 0.5rem;
">
    Tractive effort & how it is calculated
</h1>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 1. DEFINITION OF TRACTIVE EFFORT
# =========================================================

st.markdown(
    """
<div id="definition-of-tractive-effort"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
">
    Definition of tractive effort:
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
**Tractive effort is the force produced by the driving wheels of a vehicle at the point of contact with the road or rail to move the vehicle forward.** It is generated by the engine or motor and transmitted through the transmission system to the driving wheels. This force is used to overcome various resistances such as rolling resistance, air resistance, and gradient resistance. The amount of tractive effort depends mainly on the **power of the engine, vehicle speed, and wheel radius**. In simple terms, tractive effort represents the **pulling force available at the wheels to propel the vehicle forward**.
"""
)


# =========================================================
# 2. DEMONSTRATION OF TRACTIVE EFFORT
# =========================================================

st.markdown(
    """
<div id="demonstration-of-tractive-effort"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
">
    Demonstration of tractive effort and resistance forces
</p>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# ANIMATION
# =========================================================

animation_file = (
    Path(__file__).parent
    / "animations"
    / "uphill_forces.html"
)

st.iframe(
    animation_file,
    width="stretch",
    height=650,
)


# =========================================================
# EXPLANATION
# =========================================================

st.markdown(
    """
The vehicle has to overcome several resistance forces while
moving uphill. These include **rolling resistance**,
**aerodynamic drag**, and **grade resistance**.

The available **tractive effort** must be sufficient to
overcome these opposing forces and provide the required
acceleration or hauling capability.
"""
)


# =========================================================
# 3. PARAMETERS INVOLVED IN TRACTIVE FORCE CALCULATION
# =========================================================

st.markdown(
    """
<div id="parameters-involved"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
">
    Parameters involved in tractive force calculation
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
The tractive force required by a vehicle depends on its
<b>mass, speed, acceleration, prime mover, powertrain,
wheel geometry, track condition, gradient, aerodynamic
characteristics, and various resistance forces.</b>
    """,
    unsafe_allow_html=True,
)

show_parameter_table()


# =========================================================
# 4. RESISTIVE FORCES
# =========================================================

st.markdown(
    """
<div id="resistive-forces"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 0.8rem;
    margin-bottom: 0.5rem;
">
    Resistive forces acting on a vehicle & their formulations:
</p>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# ROLLING RESISTANCE
# =========================================================

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 16px;
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
">
    Rolling resistance:
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
**Rolling resistance is the resistive force that opposes the motion of a vehicle due to deformation and friction between the wheels and the road or rail during rolling.**
"""
)

st.markdown(
    """
In simple terms, it is the **force that resists the forward movement of the vehicle as its wheels roll over the surface**.
"""
)

col_image, col_formula = st.columns(
    [1.16, 0.84],
    gap="large",
)


with col_image:

    rolling_resistance_image = (
        Path(__file__).parent
        / "images"
        / "rolling_resistance.png"
    )

    st.image(
        rolling_resistance_image,
        width="stretch",
    )


with col_formula:

    st.markdown("**Rolling resistance force**")

    st.latex(
        r"""
F_{rr}=C_{rr}N
"""
    )

    st.markdown(
        "On an inclined surface, the normal force is:"
    )

    st.latex(
        r"""
N=mg\cos\theta
"""
    )

    st.markdown(
        "Therefore, the rolling resistance force becomes:"
    )

    st.latex(
        r"""
\boxed{
F_{rr}=C_{rr}mg\cos\theta
}
"""
    )

    st.markdown(
        """
where:

- **N** = normal reaction force
"""
    )


# =========================================================
# AERODYNAMIC DRAG
# =========================================================

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 16px;
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
">
    Aerodynamic Drag Resistance Force:
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
**Aerodynamic drag force** is the resistive force that opposes the motion of a vehicle as it moves through the air. It is mainly caused by the pressure difference between the front and rear of the vehicle and friction between the vehicle surface and the surrounding air. The magnitude of aerodynamic drag depends mainly on the **air density, vehicle speed, frontal area, and drag coefficient**.
"""
)

st.latex(
    r"""
\boxed{
F_{aero}=\frac{1}{2}\rho C_d A v^2
}
"""
)


# =========================================================
# GRADIENT RESISTANCE
# =========================================================

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 16px;
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
">
    Gradient resistance:
</p>
    """,
    unsafe_allow_html=True,
)

col_image, col_formula = st.columns(
    [1, 1],
    gap="large",
)


with col_image:

    gradient_resistance_image = (
        Path(__file__).parent
        / "images"
        / "gradient_resistance.png"
    )

    st.image(
        gradient_resistance_image,
        width="stretch",
    )


with col_formula:

    st.markdown(
        """
**Gradient resisting force** is the component of the vehicle’s weight that acts opposite to its direction of motion when the vehicle travels on an inclined road or track. It occurs because of the slope and must be overcome by the tractive effort when the vehicle moves uphill.
"""
    )

    st.markdown(
        """
In simple terms, it is the **force that resists the forward movement of the vehicle as its wheels roll over the surface**.
"""
    )

    st.markdown("**Gradient resistance force**")

    st.latex(
        r"""
\boxed{
F_g=mg\sin\theta
}
"""
    )


# =========================================================
# 5. REQUIRED TRACTIVE FORCE
# =========================================================

st.markdown(
    """
<div id="required-tractive-force"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
">
    Required tractive force for vehicle movemment:
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
**Required tractive force** is the minimum force that must be developed at the driving wheels to move a vehicle under a given operating condition. It must be sufficient to overcome all the resistive forces acting on the vehicle and, when required, provide the force needed for acceleration.
"""
)

st.latex(
    r"""
\boxed{
F_T=F_{rr}+F_{aero}+F_g
}
"""
)

st.markdown(
    "Or, in terms of vehicle mass, speed, and gradient angle:"
)

st.latex(
    r"""
\boxed{
F_T
=
C_{rr}mg\cos\theta
+
\frac{1}{2}\rho C_d A v^2
+
mg\sin\theta
}
"""
)

st.markdown(
    "**Now, for the vehicle to accelarate, the required tractive force becomes:**"
)

st.latex(
    r"""
\boxed{
F_T
=
C_{rr}mg\cos\theta
+
\frac{1}{2}\rho C_d A v^2
+
mg\sin\theta
+
ma
}
"""
)


# =========================================================
# 6. AVAILABLE TRACTIVE FORCE
# =========================================================

st.markdown(
    """
<div id="available-tractive-force"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
">
    Available tractive force for vehicle movement:
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
**Available tractive force** is the maximum driving force that can be delivered by the vehicle's powertrain to the driving wheels under a given operating condition. It is determined mainly by the **motor or engine torque**, **transmission or gear ratio**, **drivetrain efficiency**, and **wheel radius**, and can be expressed as
"""
)

st.latex(
    r"""
\boxed{
F_{AT-Powertrain}=\frac{T_W}{r}
}
"""
)

st.markdown(
    """
The available tractive force is also limited by the **adhesion between the driving wheels and the road or rail**, since excessive force can cause wheel slip.
"""
)

st.latex(
    r"""
\boxed{
F_{AT-Adhesion}=\mu W_a
}
"""
)

st.markdown(
    "Hence, the **Actual available Tractive Force** is:"
)

st.latex(
    r"""
\boxed{
F_{AT}
=
\min
\left(
F_{AT-Powertrain},
F_{AT-Adhesion}
\right)
}
"""
)


# =========================================================
# 7. EXAMPLE OF TRACTIVE EFFORT CALCULATION
# =========================================================

st.markdown(
    """
<div id="example-calculation"
     class="article-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
">
    Example of tractive effort calculation for a vehicle:
</p>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
A **4-wheel electric vehicle** has a total mass of **1,500 kg** and is travelling uphill on a **5% gradient** at a speed of **60 km/h**. The vehicle is accelerating at **1 m/s²**. The coefficient of rolling resistance is **0.012**, the aerodynamic drag coefficient is **0.30**, and the frontal area is **2.2 m²**. The air density is **1.225 kg/m³**. The electric motor delivers **80 kW** of mechanical power to the wheels with a drivetrain efficiency of **90%**. Assume that **60% of the vehicle weight is supported by the driving wheels** and the coefficient of adhesion between the tyres and road is **0.7**.
"""
)

st.markdown(
    """
**Calculate:**

1. Rolling resistance force
2. Aerodynamic drag force
3. Gradient resisting force
4. Force required for acceleration
5. **Required tractive force**
6. **Available tractive force from the motor**
7. **Maximum adhesive force**
8. Determine whether the vehicle can provide the required
   tractive force **without wheel slip**.
"""
)


# =========================================================
# GIVEN PARAMETERS
# =========================================================

st.markdown("**Given:**")

param_col1, param_col2, param_col3, param_col4 = st.columns(4)


with param_col1:

    st.markdown(
        """
**m = 1500 kg**  
**v = 60 km/h**  
**a = 1 m/s²**
"""
    )


with param_col2:

    st.markdown(
        """
**i = 5 %**  
**C<sub>rr</sub> = 0.012**  
**C<sub>d</sub> = 0.30**
""",
        unsafe_allow_html=True,
    )


with param_col3:

    st.markdown(
        """
**A = 2.2 m²**  
**ρ = 1.225 kg/m³**  
**P = 80 kW**
"""
    )


with param_col4:

    st.markdown(
        """
**η<sub>pt</sub> = 90 %**  
**W<sub>a</sub> = 0.60mg**  
**μ = 0.70**  
**g = 9.81 m/s²**
""",
        unsafe_allow_html=True,
    )


# =========================================================
# EXAMPLE CALCULATION VALUES
# =========================================================

i = 5

theta = math.atan(i / 100)

velocity_kmh = 60

velocity_ms = (
    velocity_kmh
    * 1000
    / 3600
)


# =========================================================
# GRADIENT ANGLE
# =========================================================

st.markdown(
    f"**Gradient angle, θ = {theta:.5f} rad**"
)


# =========================================================
# VELOCITY
# =========================================================

st.markdown(
    f"**Velocity in m/s, v = {velocity_ms:.2f} m/s**"
)


# =========================================================
# 1. ROLLING RESISTANCE
# =========================================================

st.markdown(
    '<div class="calculation-step">1. Rolling resistance force:</div>',
    unsafe_allow_html=True,
)

st.latex(
    rf"""
F_{{rr}}
=
C_{{rr}}mg\cos\theta
=
0.012
\times 1500
\times 9.81
\times \cos(0.0499584)
=
176.5\ \mathrm{{N}}
"""
)


# =========================================================
# 2. AERODYNAMIC DRAG
# =========================================================

st.markdown(
    '<div class="calculation-step">2. Aerodynamic drag force:</div>',
    unsafe_allow_html=True,
)

st.latex(
    rf"""
F_{{aero}}
=
\frac{{1}}{{2}}\rho C_d A v^2
=
\frac{{1}}{{2}}
\times 1.225
\times 0.30
\times 2.2
\times (16.67)^2
=
112.3\ \mathrm{{N}}
"""
)


# =========================================================
# 3. GRADIENT RESISTANCE
# =========================================================

st.markdown(
    '<div class="calculation-step">3. Gradient resisting force:</div>',
    unsafe_allow_html=True,
)

st.latex(
    rf"""
F_g
=
mg\sin\theta
=
1500
\times 9.81
\times \sin(0.0499584)
=
735.1\ \mathrm{{N}}
"""
)


# =========================================================
# 4. ACCELERATION FORCE
# =========================================================

st.markdown(
    '<div class="calculation-step">4. Force required for acceleration:</div>',
    unsafe_allow_html=True,
)

st.latex(
    rf"""
F_a
=
ma
=
1500
\times 1
=
1500\ \mathrm{{N}}
"""
)


# =========================================================
# 5. REQUIRED TRACTIVE FORCE
# =========================================================

st.markdown(
    '<div class="calculation-step">5. Required tractive force:</div>',
    unsafe_allow_html=True,
)

st.latex(
    r"""
F_T
=
F_{rr}
+
F_{aero}
+
F_g
+
F_a
"""
)

st.latex(
    r"""
F_T
=
176.5
+
112.3
+
735.1
+
1500
=
2523.9\ \mathrm{N}
"""
)


# =========================================================
# 6. AVAILABLE TRACTIVE FORCE
# =========================================================

st.markdown(
    '<div class="calculation-step">6. Available tractive force from the motor:</div>',
    unsafe_allow_html=True,
)

st.latex(
    r"""
F_{AT-Powertrain}
=
\frac{P\eta_{pt}}{v}
"""
)

st.latex(
    r"""
F_{AT-Powertrain}
=
\frac{80000\times0.9}{16.67}
=
4320\ \mathrm{N}
"""
)


# =========================================================
# 7. MAXIMUM ADHESIVE FORCE
# =========================================================

st.markdown(
    '<div class="calculation-step">7. Maximum adhesive force:</div>',
    unsafe_allow_html=True,
)

st.latex(
    r"""
F_{AT-Adhesion}
=
\mu W_a
"""
)

st.latex(
    r"""
F_{AT-Adhesion}
=
0.7
\times0.60
\times1500
\times9.81
=
6171.3\ \mathrm{N}
"""
)


# =========================================================
# 8. ACTUAL AVAILABLE TRACTIVE FORCE
# =========================================================

st.markdown(
    '<div class="calculation-step">8. Actual available tractive force:</div>',
    unsafe_allow_html=True,
)

st.latex(
    r"""
F_{AT}
=
\min
\left(
F_{AT-Powertrain},
F_{AT-Adhesion}
\right)
"""
)

st.latex(
    r"""
F_{AT}
=
\min(4320,\ 6171.3)
=
4320\ \mathrm{N}
"""
)


# =========================================================
# CONCLUSION
# =========================================================

st.markdown(
    """
<div class="calculation-conclusion">

<b>Conclusion:</b>

The available tractive force is greater than the required
tractive force. Therefore, the vehicle can provide the required
tractive force without wheel slip.

</div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# 8. TRACTIVE EFFORT CALCULATOR
# =========================================================

st.markdown(
    """
<div id="tractive-force-calculator"
     class="calculator-anchor">
</div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<p style="
    font-weight: bold;
    font-style: italic;
    text-decoration: underline;
    font-size: 20px;
    margin-top: 2rem;
    margin-bottom: 0.8rem;
">
    Tractive effort calculator
</p>
    """,
    unsafe_allow_html=True,
)

show_calculator()