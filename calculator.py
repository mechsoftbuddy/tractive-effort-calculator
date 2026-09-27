import math
import streamlit as st


def show_calculator():

    # =========================================================
    # PAGE STYLING
    # =========================================================

    st.markdown(
        """
<style>

/* =========================================================
   GLOBAL CALCULATOR SPACING
   ========================================================= */

.block-container {
    padding-top: 1rem;
}


/* =========================================================
   CALCULATOR HEADER
   ========================================================= */

.calc-header {
    padding: 0.1rem 0 0.8rem 0;
    border-bottom: 1px solid var(--border-color);
    margin-bottom: 0.9rem;
}

.calc-kicker {
    font-size: 0.68rem;
    font-weight: 750;
    letter-spacing: 0.13em;
    opacity: 0.58;
    margin-bottom: 0.15rem;
}

.calc-header h2 {
    margin: 0;
    font-size: 1.75rem;
    font-style: italic;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 5px;
}

.calc-header p {
    margin: 0.35rem 0 0 0;
    opacity: 0.68;
    font-size: 0.88rem;
}


/* =========================================================
   SECTION HEADINGS
   ========================================================= */

.calc-section-heading {
    display: inline-block;
    margin: 0.75rem 0 0.65rem 0;
    padding-bottom: 0.18rem;

    font-size: 1.12rem;
    font-weight: 750;
    font-style: italic;

    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 5px;

    border-bottom: 1px solid var(--border-color);
}


/* =========================================================
   VEHICLE TYPE
   ========================================================= */

.vehicle-type-area {
    margin-top: 0.35rem;
    margin-bottom: 0.25rem;
}

.vehicle-type-label {
    font-size: 0.95rem;
    font-weight: 700;
    font-style: italic;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 4px;
    margin-bottom: 0.15rem;
}


/* =========================================================
   INPUT LABELS
   ========================================================= */

div[data-testid="stWidgetLabel"] p {
    font-size: 0.80rem;
}


/* =========================================================
   RESULT CARDS
   ========================================================= */

.result-card {
    border-radius: 16px;
    padding: 1.15rem 1.15rem;
    min-height: 140px;
    color: white;

    position: relative;
    overflow: hidden;

    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.10);
}

.result-card::after {
    content: "";
    position: absolute;

    width: 95px;
    height: 95px;

    right: -32px;
    top: -32px;

    border-radius: 50%;

    background: rgba(255, 255, 255, 0.10);
}

.result-card.rolling {
    background:
        linear-gradient(
            135deg,
            #2563EB 0%,
            #1D4ED8 55%,
            #1E3A8A 100%
        );
}

.result-card.aero {
    background:
        linear-gradient(
            135deg,
            #7C3AED 0%,
            #6D28D9 55%,
            #4C1D95 100%
        );
}

.result-card.gradient {
    background:
        linear-gradient(
            135deg,
            #F59E0B 0%,
            #D97706 55%,
            #92400E 100%
        );
}

.result-card.acceleration {
    background:
        linear-gradient(
            135deg,
            #EF4444 0%,
            #DC2626 55%,
            #991B1B 100%
        );
}

.result-label {
    position: relative;
    z-index: 2;

    font-size: 0.70rem;
    font-weight: 750;

    text-transform: uppercase;
    letter-spacing: 0.07em;

    opacity: 0.88;
}

.result-value {
    position: relative;
    z-index: 2;

    font-size: 1.65rem;
    font-weight: 800;

    margin-top: 0.50rem;

    line-height: 1.05;
}

.result-formula {
    position: relative;
    z-index: 2;

    font-size: 0.76rem;

    margin-top: 0.55rem;

    opacity: 0.78;
}


/* =========================================================
   REQUIRED / AVAILABLE FORCE CARDS
   ========================================================= */

.force-card {
    border-radius: 17px;

    padding: 1.3rem 1.4rem;

    min-height: 175px;

    color: white;

    position: relative;
    overflow: hidden;

    box-shadow: 0 9px 25px rgba(0, 0, 0, 0.12);
}

.force-card::after {
    content: "";
    position: absolute;

    width: 155px;
    height: 155px;

    right: -50px;
    top: -78px;

    border-radius: 50%;

    background: rgba(255, 255, 255, 0.09);
}

.force-card.required {
    background:
        linear-gradient(
            135deg,
            #0F172A 0%,
            #1E3A8A 50%,
            #2563EB 100%
        );
}

.force-card.available {
    background:
        linear-gradient(
            135deg,
            #064E3B 0%,
            #047857 50%,
            #10B981 100%
        );
}

.force-card-label {
    position: relative;
    z-index: 2;

    font-size: 0.74rem;
    font-weight: 750;

    text-transform: uppercase;
    letter-spacing: 0.08em;

    opacity: 0.82;
}

.force-card-value {
    position: relative;
    z-index: 2;

    font-size: 2.25rem;
    font-weight: 850;

    margin-top: 0.4rem;

    line-height: 1.05;
}

.force-card-formula {
    position: relative;
    z-index: 2;

    margin-top: 0.55rem;

    font-size: 0.82rem;

    opacity: 0.72;
}

.force-card-note {
    position: relative;
    z-index: 2;

    margin-top: 0.65rem;

    font-size: 0.75rem;

    opacity: 0.68;
}


/* =========================================================
   USABLE FORCE
   ========================================================= */

.margin-card {
    margin-top: 0.75rem;

    border-radius: 13px;

    padding: 0.75rem 1rem;

    border: 1px solid var(--border-color);

    background: var(--secondary-background-color);

    display: flex;

    justify-content: space-between;
    align-items: center;
}

.margin-label {
    font-size: 0.80rem;
    opacity: 0.70;
}

.margin-value {
    font-size: 0.95rem;
    font-weight: 750;
}


/* =========================================================
   POWERTRAIN SUMMARY
   ========================================================= */

.powertrain-card {
    border: 1px solid var(--border-color);

    border-radius: 13px;

    padding: 0.85rem 1rem;

    background: var(--secondary-background-color);
}

.powertrain-title {
    font-weight: 750;

    font-style: italic;

    margin-bottom: 0.45rem;
}

.powertrain-row {
    display: flex;

    justify-content: space-between;

    padding: 0.34rem 0;

    border-bottom: 1px solid var(--border-color);

    gap: 1rem;
}

.powertrain-row:last-child {
    border-bottom: none;
}

.powertrain-label {
    opacity: 0.68;

    font-size: 0.80rem;
}

.powertrain-value {
    font-weight: 700;

    font-size: 0.84rem;

    text-align: right;
}


/* =========================================================
   STATUS
   ========================================================= */

.status-good {
    border-radius: 14px;

    padding: 1rem 1.15rem;

    background: rgba(34, 197, 94, 0.10);

    border: 1px solid rgba(34, 197, 94, 0.30);
}

.status-good-title {
    color: #16A34A;

    font-weight: 800;

    font-size: 1rem;
}

.status-good-text {
    margin-top: 0.25rem;

    opacity: 0.72;

    font-size: 0.84rem;
}

.status-bad {
    border-radius: 14px;

    padding: 1rem 1.15rem;

    background: rgba(239, 68, 68, 0.10);

    border: 1px solid rgba(239, 68, 68, 0.30);
}

.status-bad-title {
    color: #DC2626;

    font-weight: 800;

    font-size: 1rem;
}

.status-bad-text {
    margin-top: 0.25rem;

    opacity: 0.72;

    font-size: 0.84rem;
}


/* =========================================================
   DIVIDER
   ========================================================= */

.section-divider {
    height: 1px;

    background: var(--border-color);

    margin: 1.15rem 0;
}

</style>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # HEADER
    # =========================================================

    st.markdown(
        """
<div class="calc-header">
<div class="calc-kicker">ENGINEERING CALCULATOR</div>
<h2>Tractive effort calculator</h2>
<p>
Calculate the force required to move the vehicle uphill
and determine the available tractive force from the powertrain.
</p>
</div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # VEHICLE TYPE
    # =========================================================

    st.markdown(
        """
<div class="vehicle-type-area">
<div class="vehicle-type-label">Vehicle type</div>
</div>
        """,
        unsafe_allow_html=True,
    )

    vehicle_type = st.radio(
        "Vehicle type",
        [
            "Electric vehicle (EV)",
            "Internal combustion engine (ICE)",
        ],
        horizontal=True,
        label_visibility="collapsed",
    )

    is_ev = vehicle_type == "Electric vehicle (EV)"

    # =========================================================
    # VEHICLE & OPERATING CONDITIONS
    # =========================================================

    st.markdown(
        '<div class="calc-section-heading">Vehicle &amp; operating conditions</div>',
        unsafe_allow_html=True,
    )

    input_col1, input_col2, input_col3, input_col4 = st.columns(4)

    # =========================================================
    # VEHICLE
    # =========================================================

    with input_col1:

        st.markdown("**Vehicle**")

        mass = st.number_input(
            "Mass (kg)",
            min_value=0.0,
            value=1500.0,
            step=50.0,
        )

        wheel_radius = st.number_input(
            "Wheel radius (m)",
            min_value=0.01,
            value=0.31,
            step=0.01,
            format="%.2f",
        )

        speed = st.number_input(
            "Speed",
            min_value=0.0,
            value=60.0,
            step=5.0,
        )

        speed_unit = st.selectbox(
            "Speed unit",
            ["km/h", "m/s"],
        )

        acceleration = st.number_input(
            "Acceleration (m/s²)",
            min_value=0.0,
            value=1.0,
            step=0.1,
        )

    # =========================================================
    # GRADIENT & ROLLING RESISTANCE
    # =========================================================

    with input_col2:

        st.markdown("**Gradient & rolling resistance**")

        gradient = st.number_input(
            "Gradient",
            min_value=0.0,
            value=5.0,
            step=0.5,
        )

        gradient_unit = st.selectbox(
            "Gradient unit",
            ["%", "degree"],
        )

        rolling_coefficient = st.number_input(
            "Rolling resistance coefficient",
            min_value=0.0,
            value=0.012,
            step=0.001,
            format="%.3f",
        )

        gravity = st.number_input(
            "Gravity (m/s²)",
            min_value=0.0,
            value=9.81,
            step=0.01,
        )

    # =========================================================
    # AERODYNAMICS
    # =========================================================

    with input_col3:

        st.markdown("**Aerodynamics**")

        drag_coefficient = st.number_input(
            "Drag coefficient, Cd",
            min_value=0.0,
            value=0.30,
            step=0.01,
            format="%.2f",
        )

        frontal_area = st.number_input(
            "Frontal area (m²)",
            min_value=0.0,
            value=2.2,
            step=0.1,
            format="%.2f",
        )

        air_density = st.number_input(
            "Air density (kg/m³)",
            min_value=0.0,
            value=1.225,
            step=0.01,
            format="%.3f",
        )

    # =========================================================
    # POWERTRAIN
    # =========================================================

    with input_col4:

        if is_ev:

            st.markdown("**EV powertrain**")

            motor_torque = st.number_input(
                "Motor maximum torque (Nm)",
                min_value=0.0,
                value=300.0,
                step=10.0,
            )

            motor_power = st.number_input(
                "Motor maximum power (kW)",
                min_value=0.0,
                value=80.0,
                step=5.0,
            )

            transmission_ratio = st.number_input(
                "Transmission ratio",
                min_value=0.01,
                value=1.00,
                step=0.05,
                format="%.2f",
            )

            final_drive_ratio = st.number_input(
                "Final drive ratio",
                min_value=0.01,
                value=9.00,
                step=0.10,
                format="%.2f",
            )

            powertrain_efficiency = st.number_input(
                "Powertrain efficiency (%)",
                min_value=0.0,
                max_value=100.0,
                value=90.0,
                step=1.0,
            )

        else:

            st.markdown("**ICE powertrain**")

            engine_torque = st.number_input(
                "Engine torque at operating point (Nm)",
                min_value=0.0,
                value=250.0,
                step=10.0,
            )

            engine_power = st.number_input(
                "Engine maximum power (kW)",
                min_value=0.0,
                value=80.0,
                step=5.0,
            )

            transmission_ratio = st.number_input(
                "Selected gear ratio",
                min_value=0.01,
                value=1.00,
                step=0.05,
                format="%.2f",
            )

            final_drive_ratio = st.number_input(
                "Final drive ratio",
                min_value=0.01,
                value=4.00,
                step=0.10,
                format="%.2f",
            )

            powertrain_efficiency = st.number_input(
                "Drivetrain efficiency (%)",
                min_value=0.0,
                max_value=100.0,
                value=90.0,
                step=1.0,
            )

    # =========================================================
    # ADHESION
    # =========================================================

    st.markdown(
        '<div class="calc-section-heading">Adhesion</div>',
        unsafe_allow_html=True,
    )

    adhesion_col1, adhesion_col2, adhesion_col3 = st.columns(3)

    with adhesion_col1:

        driving_weight_fraction = st.number_input(
            "Driving-wheel weight fraction",
            min_value=0.0,
            max_value=1.0,
            value=0.60,
            step=0.05,
            format="%.2f",
        )

    with adhesion_col2:

        adhesion_coefficient = st.number_input(
            "Adhesion coefficient, μ",
            min_value=0.0,
            value=0.70,
            step=0.05,
            format="%.2f",
        )

    with adhesion_col3:

        st.markdown(
            """
<div style="padding-top:1.65rem; opacity:0.65; font-size:0.80rem;">
Adhesive weight = driving-wheel fraction × vehicle weight
</div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # UNIT CONVERSIONS
    # =========================================================

    if speed_unit == "km/h":
        speed_ms = speed / 3.6
    else:
        speed_ms = speed

    if gradient_unit == "%":
        gradient_radians = math.atan(
            gradient / 100.0
        )
    else:
        gradient_radians = math.radians(
            gradient
        )

    powertrain_efficiency_decimal = (
        powertrain_efficiency / 100.0
    )

    # =========================================================
    # VEHICLE FORCES
    # =========================================================

    adhesive_weight = (
        driving_weight_fraction
        * mass
        * gravity
    )

    rolling_resistance = (
        rolling_coefficient
        * mass
        * gravity
        * math.cos(gradient_radians)
    )

    aerodynamic_drag = (
        0.5
        * air_density
        * drag_coefficient
        * frontal_area
        * speed_ms**2
    )

    gradient_resistance = (
        mass
        * gravity
        * math.sin(gradient_radians)
    )

    acceleration_force = (
        mass
        * acceleration
    )

    # =========================================================
    # REQUIRED TRACTIVE FORCE
    # =========================================================

    required_tractive_force = (
        rolling_resistance
        + aerodynamic_drag
        + gradient_resistance
        + acceleration_force
    )

    # =========================================================
    # WHEEL SPEED
    # =========================================================

    wheel_angular_speed = (
        speed_ms / wheel_radius
    )

    total_reduction_ratio = (
        transmission_ratio
        * final_drive_ratio
    )

    shaft_angular_speed = (
        wheel_angular_speed
        * total_reduction_ratio
    )

    shaft_speed_rpm = (
        shaft_angular_speed
        * 60.0
        / (2.0 * math.pi)
    )

    # =========================================================
    # POWERTRAIN PARAMETERS
    # =========================================================

    if is_ev:

        shaft_torque_limit = motor_torque
        shaft_power_kw = motor_power
        shaft_name = "Motor"
        torque_name = "Motor torque"

    else:

        shaft_torque_limit = engine_torque
        shaft_power_kw = engine_power
        shaft_name = "Engine"
        torque_name = "Engine torque"

    # =========================================================
    # TORQUE-LIMITED WHEEL TORQUE
    # =========================================================

    torque_limited_wheel_torque = (
        shaft_torque_limit
        * total_reduction_ratio
        * powertrain_efficiency_decimal
    )

    torque_limited_force = (
        torque_limited_wheel_torque
        / wheel_radius
    )

    # =========================================================
    # POWER-LIMITED FORCE
    # =========================================================

    shaft_power_watts = (
        shaft_power_kw * 1000.0
    )

    if speed_ms > 0:

        power_limited_force = (
            shaft_power_watts
            * powertrain_efficiency_decimal
            / speed_ms
        )

    else:

        power_limited_force = float("inf")

    # =========================================================
    # AVAILABLE TRACTIVE FORCE
    # =========================================================

    available_tractive_force = min(
        torque_limited_force,
        power_limited_force,
    )

    # =========================================================
    # ADHESION
    # =========================================================

    maximum_adhesive_force = (
        adhesion_coefficient
        * adhesive_weight
    )

    usable_tractive_force = min(
        available_tractive_force,
        maximum_adhesive_force,
    )

    # =========================================================
    # CHECKS
    # =========================================================

    powertrain_sufficient = (
        required_tractive_force
        <= available_tractive_force
    )

    adhesion_sufficient = (
        required_tractive_force
        <= maximum_adhesive_force
    )

    no_wheel_slip = (
        powertrain_sufficient
        and adhesion_sufficient
    )

    # =========================================================
    # RESULTS
    # =========================================================

    st.markdown(
        '<div class="section-divider"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="calc-section-heading">Calculation results</div>',
        unsafe_allow_html=True,
    )

    # =========================================================
    # FORCE RESULT CARDS
    # =========================================================

    result_col1, result_col2, result_col3, result_col4 = st.columns(4)

    with result_col1:

        st.markdown(
            f"""
<div class="result-card rolling">
<div class="result-label">
Rolling resistance
</div>

<div class="result-value">
{rolling_resistance:,.1f} N
</div>

<div class="result-formula">
F<sub>rr</sub> = C<sub>rr</sub>mg cos θ
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    with result_col2:

        st.markdown(
            f"""
<div class="result-card aero">
<div class="result-label">
Aerodynamic drag
</div>

<div class="result-value">
{aerodynamic_drag:,.1f} N
</div>

<div class="result-formula">
F<sub>aero</sub> = ½ρC<sub>d</sub>Av²
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    with result_col3:

        st.markdown(
            f"""
<div class="result-card gradient">
<div class="result-label">
Gradient resistance
</div>

<div class="result-value">
{gradient_resistance:,.1f} N
</div>

<div class="result-formula">
F<sub>g</sub> = mg sin θ
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    with result_col4:

        st.markdown(
            f"""
<div class="result-card acceleration">
<div class="result-label">
Acceleration force
</div>

<div class="result-value">
{acceleration_force:,.1f} N
</div>

<div class="result-formula">
F<sub>acc</sub> = ma
</div>
</div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # TRACTIVE FORCE
    # =========================================================

    st.markdown(
        '<div class="calc-section-heading">Tractive force</div>',
        unsafe_allow_html=True,
    )

    force_col1, force_col2 = st.columns(2)

    with force_col1:

        st.markdown(
            f"""
<div class="force-card required">

<div class="force-card-label">
Required tractive force
</div>

<div class="force-card-value">
{required_tractive_force:,.2f} N
</div>

<div class="force-card-formula">
F<sub>required</sub> =
F<sub>rr</sub> +
F<sub>aero</sub> +
F<sub>g</sub> +
F<sub>acc</sub>
</div>

<div class="force-card-note">
Force required to overcome resistance and accelerate the vehicle.
</div>

</div>
            """,
            unsafe_allow_html=True,
        )

    with force_col2:

        st.markdown(
            f"""
<div class="force-card available">

<div class="force-card-label">
Available tractive force
</div>

<div class="force-card-value">
{available_tractive_force:,.2f} N
</div>

<div class="force-card-formula">
F<sub>available</sub> =
min(F<sub>torque</sub>, F<sub>power</sub>)
</div>

<div class="force-card-note">
Available force from the selected powertrain at the current speed.
</div>

</div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # USABLE FORCE
    # =========================================================

    st.markdown(
        f"""
<div class="margin-card">

<div class="margin-label">
Usable tractive force after adhesion limit
</div>

<div class="margin-value">
{usable_tractive_force:,.2f} N
</div>

</div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # POWERTRAIN CALCULATION
    # =========================================================

    st.markdown(
        '<div class="calc-section-heading">Powertrain calculation</div>',
        unsafe_allow_html=True,
    )

    power_col1, power_col2 = st.columns(2)

    with power_col1:

        powertrain_name = (
            "Electric powertrain"
            if is_ev
            else "ICE powertrain"
        )

        st.markdown(
            f"""
<div class="powertrain-card">

<div class="powertrain-title">
{powertrain_name}
</div>

<div class="powertrain-row">
<span class="powertrain-label">
{torque_name}
</span>

<span class="powertrain-value">
{shaft_torque_limit:,.2f} Nm
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
{shaft_name} power
</span>

<span class="powertrain-value">
{shaft_power_kw:,.2f} kW
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
Transmission ratio
</span>

<span class="powertrain-value">
{transmission_ratio:.2f}
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
Final drive ratio
</span>

<span class="powertrain-value">
{final_drive_ratio:.2f}
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
Powertrain efficiency
</span>

<span class="powertrain-value">
{powertrain_efficiency:.1f} %
</span>
</div>

</div>
            """,
            unsafe_allow_html=True,
        )

    with power_col2:

        if torque_limited_force <= power_limited_force:

            limiting_source = "Torque limit"

        else:

            limiting_source = "Power limit"

        st.markdown(
            f"""
<div class="powertrain-card">

<div class="powertrain-title">
Available force calculation
</div>

<div class="powertrain-row">
<span class="powertrain-label">
{shaft_name} speed
</span>

<span class="powertrain-value">
{shaft_speed_rpm:,.0f} rpm
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
Torque-limited force
</span>

<span class="powertrain-value">
{torque_limited_force:,.2f} N
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
Power-limited force
</span>

<span class="powertrain-value">
{power_limited_force:,.2f} N
</span>
</div>

<div class="powertrain-row">
<span class="powertrain-label">
Limiting factor
</span>

<span class="powertrain-value">
{limiting_source}
</span>
</div>

</div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # WHEEL-SLIP CHECK
    # =========================================================

    st.markdown(
        '<div class="calc-section-heading">Wheel-slip check</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        rf"**Usable tractive force:** "
        rf"$F_{{usable}} = \min(F_{{available}}, F_{{adh}})"
        rf" = {usable_tractive_force:,.2f}\ \mathrm{{N}}$"
    )

    if no_wheel_slip:

        st.markdown(
            """
<div class="status-good">

<div class="status-good-title">
✓ Vehicle can provide the required tractive force without wheel slip
</div>

<div class="status-good-text">
The required tractive force is below both the available powertrain
force and the maximum adhesive force.
</div>

</div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            """
<div class="status-bad">

<div class="status-bad-title">
⚠ Required tractive force cannot be provided
</div>

<div class="status-bad-text">
The required tractive force exceeds either the available powertrain
force or the available adhesion limit.
</div>

</div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # CALCULATION DETAILS
    # =========================================================

    with st.expander("Show calculation details"):

        powertrain_equation_label = (
            "motor"
            if is_ev
            else "engine"
        )

        st.markdown(
            rf"""
**Gradient angle**

$\theta =
\tan^{{-1}}\left(\frac{{{gradient:.2f}}}{{100}}\right)
= {gradient_radians:.5f}\ \mathrm{{rad}}$

**Vehicle speed**

$v = {speed_ms:.3f}\ \mathrm{{m/s}}$

**Wheel angular speed**

$\omega_w =
\frac{{v}}{{r_w}}
= {wheel_angular_speed:.3f}\ \mathrm{{rad/s}}$

**{shaft_name} speed**

$n_{{{powertrain_equation_label}}}
= {shaft_speed_rpm:,.0f}\ \mathrm{{rpm}}$

**Rolling resistance**

$F_{{rr}} =
C_{{rr}}mg\cos\theta
= {rolling_resistance:,.2f}\ \mathrm{{N}}$

**Aerodynamic drag**

$F_{{aero}} =
\frac{{1}}{{2}}\rho C_d A v^2
= {aerodynamic_drag:,.2f}\ \mathrm{{N}}$

**Gradient resistance**

$F_g =
mg\sin\theta
= {gradient_resistance:,.2f}\ \mathrm{{N}}$

**Acceleration force**

$F_{{acc}} =
ma
= {acceleration_force:,.2f}\ \mathrm{{N}}$

**Required tractive force**

$F_{{required}} =
F_{{rr}} + F_{{aero}} + F_g + F_{{acc}}
= {required_tractive_force:,.2f}\ \mathrm{{N}}$

**Wheel torque**

$T_w =
T_{{{powertrain_equation_label}}}
\times i_g
\times i_{{FDR}}
\times \eta
= {torque_limited_wheel_torque:,.2f}\ \mathrm{{Nm}}$

**Torque-limited tractive force**

$F_{{torque}} =
\frac{{T_w}}{{r_w}}
= {torque_limited_force:,.2f}\ \mathrm{{N}}$

**Power-limited tractive force**

$F_{{power}} =
\frac{{P\eta}}{{v}}
= {power_limited_force:,.2f}\ \mathrm{{N}}$

**Available tractive force**

$F_{{available}} =
\min(F_{{torque}},F_{{power}})
= {available_tractive_force:,.2f}\ \mathrm{{N}}$

**Maximum adhesive force**

$F_{{adh}} =
\mu W_a
= \mu(0.60mg)
= {maximum_adhesive_force:,.2f}\ \mathrm{{N}}$

**Usable tractive force**

$F_{{usable}} =
\min(F_{{available}},F_{{adh}})
= {usable_tractive_force:,.2f}\ \mathrm{{N}}$
"""
        )