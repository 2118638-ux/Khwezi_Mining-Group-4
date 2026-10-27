import streamlit as st
import pandas as pd

# ============================================================
# KHWEZI MINING
# Mining Health, Safety and Equipment Monitoring Application
# ============================================================

st.set_page_config(
    page_title="Khwezi Mining",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Interface styling: the photograph is loaded without altering its pixels.
from pathlib import Path
import base64

APP_FOLDER = Path(__file__).resolve().parent
COVER_FILE = APP_FOLDER / "khwezi_cover.jpg"


def apply_layout():
    image_css = ""
    if COVER_FILE.exists():
        image_data = base64.b64encode(COVER_FILE.read_bytes()).decode("ascii")
        image_css = f"""
        body:has(.khwezi-login-marker) .stApp {{
            background-image: linear-gradient(rgba(6,18,30,.16), rgba(6,18,30,.16)),
                              url('data:image/jpeg;base64,{image_data}');
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
        }}
        """

    st.markdown("""<style>
        :root {--khwezi-navy:#10283d; --khwezi-gold:#c99a42;}
        .stApp {background:#f3f6f9; color:#16283a;}
        [data-testid="stHeader"] {background:transparent;}
        [data-testid="stSidebar"] {background:#10283d;}
        [data-testid="stSidebar"] * {color:#f5f7fa;}
        [data-testid="stSidebar"] [role="radiogroup"] label {padding:7px 10px; border-radius:5px;}
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {background:#c99a42;}
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) * {color:#10283d;}
        [data-testid="stMetric"] {background:white; border:1px solid #e3e9ef;
            border-radius:7px; padding:17px 16px; min-height:112px;}
        [data-testid="stMetricLabel"] {color:#5a6a7a;}
        [data-testid="stMetricValue"] {color:#10283d;}
        div.stButton > button[kind="primary"], div.stFormSubmitButton > button[kind="primary"] {
            background:#c99a42; border-color:#c99a42; color:#10283d; font-weight:650;}
        div.stButton > button:hover {border-color:#b88630;}
        div[data-testid="stDataFrame"], div[data-testid="stTable"] {
            background:#fff; border-radius:6px;}
        .khwezi-brand {font-size:1.5rem; letter-spacing:.19em; font-weight:750; color:#10283d;}
        .khwezi-tagline {font-size:1rem; color:#10283d; margin-top:.3rem;}
        .khwezi-system {font-size:1.05rem; color:#10283d; margin-top:1.5rem; line-height:1.5;}
        .khwezi-logo {display:flex; align-items:flex-end; gap:5px; height:70px; justify-content:center;}
        .khwezi-logo span {display:block; width:15px; background:#10283d;}
        .khwezi-logo span:nth-child(1) {height:22px;}
        .khwezi-logo span:nth-child(2) {height:40px;}
        .khwezi-logo span:nth-child(3) {height:59px;}
        .khwezi-logo span:nth-child(4) {height:17px; background:#c99a42; align-self:center; margin-top:-15px;}
        .khwezi-login-marker {display:none;}
        body:has(.khwezi-login-marker) [data-testid="stSidebar"] {display:none;}
        body:has(.khwezi-login-marker) [data-testid="stAppViewContainer"] > .main
            .block-container {max-width:1300px; padding-top:11vh;}
        body:has(.khwezi-login-marker) .khwezi-brand,
        body:has(.khwezi-login-marker) .khwezi-tagline,
        body:has(.khwezi-login-marker) .khwezi-system {text-shadow:0 1px 12px #ffffffaa;}
        /* LOGIN PAGE ONLY: brand in sky above haul truck; solid white login card. */
        body:has(.khwezi-login-marker) [data-testid="stAppViewContainer"] .main .block-container {
            max-width: 1320px !important;
            padding-top: 1vh !important;
            padding-left: 4vw !important;
            padding-right: 4vw !important;
        }
        body:has(.khwezi-login-marker) [data-testid="stHorizontalBlock"] {
            align-items: flex-start !important;
        }
        body:has(.khwezi-login-marker) .khwezi-brand,
        body:has(.khwezi-login-marker) .khwezi-tagline,
        body:has(.khwezi-login-marker) .khwezi-system {
            color: #10283d !important;
            text-shadow: 0 1px 12px rgba(255,255,255,.85), 0 0 4px white;
        }
        body:has(.khwezi-login-marker) .khwezi-logo {margin-top:0;}
        body:has(.khwezi-login-marker) .khwezi-authorised {
            text-align: center !important;
            color: #657587 !important;
            font-size: .78rem;
            border-top: 1px solid #e8edf1;
            padding-top: 13px;
            margin: 0 !important;
        }
        @media (min-width: 850px) {
            body:has(.khwezi-login-marker) [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
                padding-top: 0 !important;
            }
            body:has(.khwezi-login-marker) [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:last-child {
                padding-top: 1vh !important;
            }
        }

        /* Login card: target the native Streamlit keyed container directly. */
        .st-key-khwezi_login_card,
        div[data-testid="stVerticalBlockBorderWrapper"].st-key-khwezi_login_card {
            background: #ffffff !important;
            background-color: #ffffff !important;
            border-radius: 10px !important;
            color: #10283d !important;
        }
        .st-key-khwezi_login_card {
            border: 1px solid #e2e6ec !important;
            padding: 22px 24px !important;
            box-shadow: 0 12px 35px rgba(0,0,0,.28) !important;
        }
        .st-key-khwezi_login_card [data-testid="stVerticalBlock"],
        .st-key-khwezi_login_card [data-testid="stElementContainer"] {
            background-color: transparent !important;
        }
        .st-key-khwezi_login_card h3,
        .st-key-khwezi_login_card p,
        .st-key-khwezi_login_card label,
        .st-key-khwezi_login_card summary { color: #10283d !important; }
        .st-key-khwezi_login_card [data-testid="stExpander"] summary {
            justify-content: center !important;
            text-align: center !important;
            text-decoration: underline;
        }
        .st-key-khwezi_login_card .khwezi-authorised {
            text-align: center !important;
            font-size: 12px !important;
            color: #697889 !important;
            border-top: 1px solid #e7ebef;
            padding-top: 10px;
        }
        /* Remove the large top gap on the login screen. */
        body:has(.khwezi-login-marker) .block-container {
            padding-top: 0.5rem !important;
            max-width: 1320px !important;
        }
        body:has(.khwezi-login-marker) .khwezi-logo { margin-top: 0 !important; }
        body:has(.khwezi-login-marker) [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:last-child {
            padding-top: 5rem !important;
        }

        /* Revised global accessible light forms and action buttons */
        .stApp [data-testid="stWidgetLabel"] *, .stApp label, .stApp label p,
        .stApp [data-testid="stMarkdownContainer"] label {color:#10283d !important; opacity:1 !important;}
        .stApp [data-testid="stTextInput"] input,
        .stApp [data-testid="stNumberInput"] input,
        .stApp [data-testid="stTextArea"] textarea,
        .stApp [data-baseweb="select"] > div {
            background:#ffffff !important; color:#10283d !important;
            border-color:#cbd5e1 !important;
        }
        .stApp [data-baseweb="select"] * {color:#10283d !important;}
        .stApp input::placeholder, .stApp textarea::placeholder {color:#738498 !important; opacity:1;}
        .stApp [data-testid="stTextInput"] input:focus,
        .stApp [data-testid="stTextArea"] textarea:focus {border-color:#c99a42 !important;}
        .stApp div.stButton > button, .stApp div.stDownloadButton > button,
        .stApp div.stFormSubmitButton > button {
            background:#c99a42 !important; border:1px solid #bd8d34 !important;
            color:#10283d !important; font-weight:700 !important; border-radius:8px !important;
        }
        .stApp div.stButton > button *, .stApp div.stDownloadButton > button *,
        .stApp div.stFormSubmitButton > button * {color:#10283d !important;}
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button {
            background:#c99a42 !important; color:#10283d !important;
            border-radius:8px !important; box-shadow:0 2px 8px #10283d33;
        }
        [data-testid="stSidebarCollapsedControl"] svg,
        [data-testid="stSidebarCollapseButton"] svg {stroke:#10283d !important; color:#10283d !important;}
        .khwezi-system {font-size:1.55rem !important; font-weight:800 !important;
            line-height:1.25 !important; text-shadow:0 2px 12px white, 0 0 9px white !important;}
        .khwezi-kpi {background:#fff; border:1px solid #e0e7ee; border-radius:12px;
            min-height:142px; padding:16px; margin-bottom:12px; box-shadow:0 3px 10px #10283d09;}
        .khwezi-kpi-icon {font-size:1.55rem; display:inline-flex; width:43px; height:43px;
            align-items:center; justify-content:center; border-radius:10px; background:#f2e7d1;}
        .khwezi-kpi-number {font-size:2rem; font-weight:750; color:#10283d; margin-top:7px;}
        .khwezi-kpi-label {font-size:.83rem; font-weight:550; color:#5d6c7b;}
        
        /* Strong visible sidebar toggle across Streamlit releases */
        [data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stExpandSidebarButton"],
        [data-testid="stSidebarNavCollapseButton"],
        [data-testid="stSidebarHeader"] button,
        [data-testid="stHeader"] button[kind="header"],
        [data-testid="stHeader"] button[data-testid="stBaseButton-headerNoPadding"],
        button[aria-label*="sidebar" i] {
            opacity: 1 !important;
            visibility: visible !important;
            color: #10283d !important;
        }
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stSidebarCollapsedControl"] button *,
        [data-testid="stSidebarHeader"] button,
        [data-testid="stSidebarHeader"] button *,
        [data-testid="stHeader"] button[kind="header"],
        [data-testid="stHeader"] button[kind="header"] * {
            color:#10283d !important;
            stroke:#10283d !important;
            opacity:1 !important;
        }
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stSidebarHeader"] button,
        [data-testid="stHeader"] button[kind="header"] {
            background:#f0c361 !important;
            border:2px solid #10283d !important;
            border-radius:8px !important;
            min-width:38px !important;
            min-height:38px !important;
            box-shadow:0 2px 6px #10283d44 !important;
        }
        [data-testid="stSidebarCollapsedControl"] svg,
        [data-testid="stSidebarHeader"] svg,
        [data-testid="stHeader"] button svg {
            stroke:#10283d !important;
            color:#10283d !important;
            opacity:1 !important;
        }
        /* Consistent full-width navigation with permanent labels and Lucide/Material icons */
        [data-testid="stSidebar"] div.stButton > button {
            display:flex !important;
            width:100% !important;
            justify-content:flex-start !important;
            text-align:left !important;
            gap:12px !important;
            min-height:43px !important;
            padding:9px 14px !important;
            color:#f5f7fa !important;
            background:transparent !important;
            border:1px solid transparent !important;
            border-radius:8px !important;
            font-weight:600 !important;
        }
        [data-testid="stSidebar"] div.stButton > button p,
        [data-testid="stSidebar"] div.stButton > button span {
            color:inherit !important;
            opacity:1 !important;
            visibility:visible !important;
        }
        [data-testid="stSidebar"] div.stButton > button[kind="primary"] {
            color:#10283d !important;
            background:#d6a74a !important;
        }
        [data-testid="stSidebar"] div.stButton > button:hover {
            background:#28445b !important;
            color:white !important;
        }
        [data-testid="stSidebar"] div.stButton > button[kind="primary"]:hover {
            background:#edc36d !important;
            color:#10283d !important;
        }
        /* Sidebar navigation labels: override global gold-button text rules. */
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"],
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"] *,
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"] p,
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"] span {
            color:#ffffff !important;
            opacity:1 !important;
            visibility:visible !important;
        }
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
            background:transparent !important;
            border-color:transparent !important;
        }
        [data-testid="stSidebar"] div.stButton > button[kind="primary"],
        [data-testid="stSidebar"] div.stButton > button[kind="primary"] * {
            color:#10283d !important;
        }
        /* Final visibility and navigation refinements */
        [data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarNavCollapseButton"],
        [data-testid="stExpandSidebarButton"],
        button[aria-label*="sidebar" i] {
            color:#10283d !important; opacity:1 !important;
        }
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button,
        [data-testid="stExpandSidebarButton"] button,
        button[aria-label="Open sidebar"], button[aria-label="Close sidebar"] {
            background:#d4a23d !important; color:#10283d !important;
            border:2px solid #10283d !important; opacity:1 !important;
            min-width:36px !important; min-height:36px !important;
            box-shadow:0 2px 7px #10283d33 !important;
        }
        [data-testid="stSidebarCollapsedControl"] svg,
        [data-testid="stSidebarCollapseButton"] svg,
        [data-testid="stExpandSidebarButton"] svg,
        button[aria-label*="sidebar" i] svg {
            color:#10283d !important; stroke:#10283d !important;
            fill:none !important; opacity:1 !important;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label,
        [data-testid="stSidebar"] [role="radiogroup"] label p,
        [data-testid="stSidebar"] [role="radiogroup"] label span,
        [data-testid="stSidebar"] [role="radiogroup"] label div {
            font-size:0.98rem !important; visibility:visible !important;
            opacity:1 !important; white-space:normal !important;
            color:#f5f7fa !important;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) p,
        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) span {
            color:#10283d !important;
        }
        .khwezi-kpi-icon svg {width:27px;height:27px;stroke:#10283d;stroke-width:2.2;
            fill:none;stroke-linecap:round;stroke-linejoin:round;}
        .khwezi-topline {padding:10px 16px; margin-bottom:20px; background:#10283d;
            border-radius:5px; color:white; font-weight:650; letter-spacing:.12em;}
        .khwezi-page-description {color:#657587; margin-top:-12px; margin-bottom:22px;}
        """ + image_css + "</style>", unsafe_allow_html=True)


apply_layout()

# ------------------------------------------------------------
# FILES
# ------------------------------------------------------------

USERS_FILE = APP_FOLDER / "users.csv"
PERMISSIONS_FILE = APP_FOLDER / "permissions.csv"
WORKERS_FILE = APP_FOLDER / "workers.csv"
INCIDENTS_FILE = APP_FOLDER / "incidents.csv"
EQUIPMENT_FILE = APP_FOLDER / "equipment (1).csv"

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------


def load_data():
    users = pd.read_csv(USERS_FILE)
    permissions = pd.read_csv(PERMISSIONS_FILE)
    workers = pd.read_csv(WORKERS_FILE)
    incidents = pd.read_csv(INCIDENTS_FILE)
    equipment = pd.read_csv(EQUIPMENT_FILE)
    return users, permissions, workers, incidents, equipment


if "users" not in st.session_state:
    (
        st.session_state.users,
        st.session_state.permissions,
        st.session_state.workers,
        st.session_state.incidents,
        st.session_state.equipment,
    ) = load_data()

users = st.session_state.users
permissions = st.session_state.permissions
workers = st.session_state.workers
incidents = st.session_state.incidents
equipment = st.session_state.equipment

# Fields listed in the brief that are not in the supplied CSVs.
for column in ["Safety observations", "Risk level"]:
    if column not in workers.columns:
        workers[column] = ""

for column in [
    "Time",
    "Location",
    "Injury_Status",
    "LTI_Status",
    "Corrective_Action",
]:
    if column not in incidents.columns:
        incidents[column] = ""

st.session_state.workers = workers
st.session_state.incidents = incidents

# ------------------------------------------------------------
# LOGIN STATE
# ------------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "user_role" not in st.session_state:
    st.session_state.user_role = ""

# ------------------------------------------------------------
# PERMISSIONS
# ------------------------------------------------------------


def has_access(permission_name):
    role_permissions = permissions[
        permissions["Role"] == st.session_state.user_role
    ]

    if role_permissions.empty:
        return False

    if permission_name not in role_permissions.columns:
        return False

    return role_permissions[permission_name].values[0] == "Yes"


# ------------------------------------------------------------
# RISK
# ------------------------------------------------------------


def risk_level(score):
    if score <= 4:
        return "Low"
    elif score <= 9:
        return "Medium"
    elif score <= 16:
        return "High"
    else:
        return "Critical"


# ------------------------------------------------------------
# EQUIPMENT CONDITION
# ------------------------------------------------------------


def check_equipment_status(temperature, vibration):
    # Temperature: <80 normal, 80-100 warning, >100 critical.
    if temperature > 100:
        temperature_status = "CRITICAL"
    elif temperature >= 80:
        temperature_status = "WARNING"
    else:
        temperature_status = "NORMAL"

    # Vibration: <5 normal, 5-8 warning, >8 critical.
    if vibration > 8:
        vibration_status = "CRITICAL"
    elif vibration >= 5:
        vibration_status = "WARNING"
    else:
        vibration_status = "NORMAL"

    if "CRITICAL" in [temperature_status, vibration_status]:
        reasons = []

        if temperature_status == "CRITICAL":
            reasons.append("temperature exceeds predefined threshold")

        if vibration_status == "CRITICAL":
            reasons.append("vibration exceeds predefined threshold")

        return (
            "CRITICAL",
            f"CRITICAL: Equipment {' and '.join(reasons)}. Inspection required."
        )

    if "WARNING" in [temperature_status, vibration_status]:
        reasons = []

        if temperature_status == "WARNING":
            reasons.append("temperature approaching predefined threshold")

        if vibration_status == "WARNING":
            reasons.append("vibration approaching predefined threshold")

        return (
            "WARNING",
            f"WARNING: Equipment {' and '.join(reasons)}."
        )

    return (
        "NORMAL",
        "NORMAL: Equipment operating within defined monitoring limits."
    )


def apply_equipment_conditions(equipment_data):
    results = equipment_data.apply(
        lambda row: check_equipment_status(
            row["Temperature"],
            row["Vibration"]
        ),
        axis=1
    )

    equipment_data["Status"] = results.apply(lambda x: x[0])
    equipment_data["Status_Message"] = results.apply(lambda x: x[1])
    return equipment_data


# ------------------------------------------------------------
# MAINTENANCE
# ------------------------------------------------------------


def check_equipment_maintenance(equipment_row):
    total_time = (
        equipment_row["operating_time"]
        + equipment_row["downtime"]
    )

    if total_time > 0:
        availability = (
            equipment_row["operating_time"]
            / total_time
            * 100
        )
    else:
        availability = 0

    flags = []

    if equipment_row["status"] == "Due":
        flags.append("Due for maintenance")

    if equipment_row["status"] == "Overdue":
        flags.append("Overdue equipment")

    if equipment_row["status"] == "Under Maintenance":
        flags.append("Equipment under maintenance")

    if equipment_row["downtime"] > 15:
        flags.append("Excessive downtime")

    if equipment_row["alerts"] > 2:
        flags.append("Repeated alerts")

    if availability < 85:
        flags.append("Low availability")

    return availability, flags


def apply_maintenance(equipment_data):
    availability_list = []
    flags_list = []

    for _, row in equipment_data.iterrows():
        equipment_row = {
            "operating_time": row["Operating_Time"],
            "downtime": row["Downtime"],
            "status": row["Maintenance_Status"],
            "alerts": row["Alert_Count"],
        }

        availability, flags = check_equipment_maintenance(equipment_row)
        availability_list.append(round(availability, 1))
        flags_list.append("; ".join(flags) if flags else "None")

    equipment_data["Calculated_Availability"] = availability_list
    equipment_data["Maintenance_Flags"] = flags_list
    return equipment_data


# ------------------------------------------------------------
# ALERT FUNCTIONS
# ------------------------------------------------------------


def temperature_alert(value):
    if value > 100:
        return "Critical"
    elif value >= 80:
        return "Warning"
    else:
        return "Normal"


def vibration_alert(value):
    if value > 8:
        return "Critical"
    elif value >= 5:
        return "Warning"
    else:
        return "Normal"


def incident_alert(value):
    if str(value).strip().lower() == "critical":
        return "CRITICAL INCIDENT"
    return "NO ALERT"


def ppe_alert(value):
    if str(value).strip().lower() == "no":
        return "LOW PPE COMPLIANCE"
    return "NO ALERT"


def fatigue_alert(value):
    if str(value).strip().lower() == "high":
        return "HIGH FATIGUE"
    return "NO ALERT"


# ------------------------------------------------------------
# BUILD ANALYSIS DATA AND ALERTS
# ------------------------------------------------------------


def build_project_data():
    current_workers = st.session_state.workers.copy()
    current_incidents = st.session_state.incidents.copy()
    current_equipment = st.session_state.equipment.copy()

    current_equipment = apply_equipment_conditions(current_equipment)
    current_equipment = apply_maintenance(current_equipment)

    current_equipment["Temperature_Alert"] = (
        current_equipment["Temperature"].apply(temperature_alert)
    )

    current_equipment["Vibration_Alert"] = (
        current_equipment["Vibration"].apply(vibration_alert)
    )

    current_incidents["Incident_Alert"] = (
        current_incidents["Severity"].apply(incident_alert)
    )

    current_workers["PPE_Alert"] = (
        current_workers["PPE compliance"].apply(ppe_alert)
    )

    current_workers["Fatigue_Alert"] = (
        current_workers["Fatigue level"].apply(fatigue_alert)
    )

    # Risk Score = Likelihood x Consequence.
    current_incidents["Risk_Score"] = (
        current_incidents["Likelihood"]
        * current_incidents["Consequence"]
    )

    current_incidents["Risk_Level"] = (
        current_incidents["Risk_Score"].apply(risk_level)
    )

    central_alerts = []

    # 1. High equipment temperature.
    for _, row in current_equipment.iterrows():
        if row["Temperature_Alert"] != "Normal":
            central_alerts.append({
                "Source": "Equipment",
                "ID": row["Equipment_ID"],
                "Alert_Type": "Temperature",
                "Level": row["Temperature_Alert"],
                "Recommended_Action": (
                    "Inspect equipment and follow appropriate "
                    "maintenance/safety procedures."
                ),
            })

    # 2. High equipment vibration.
    for _, row in current_equipment.iterrows():
        if row["Vibration_Alert"] != "Normal":
            central_alerts.append({
                "Source": "Equipment",
                "ID": row["Equipment_ID"],
                "Alert_Type": "Vibration",
                "Level": row["Vibration_Alert"],
                "Recommended_Action": (
                    "Inspect equipment and follow appropriate "
                    "maintenance/safety procedures."
                ),
            })

    # 3. Critical safety incidents.
    for _, row in current_incidents.iterrows():
        if row["Incident_Alert"] != "NO ALERT":
            central_alerts.append({
                "Source": "Incident",
                "ID": row["Incident_ID"],
                "Alert_Type": "Critical Safety Incident",
                "Level": "Critical",
                "Recommended_Action": (
                    "Review the incident and corrective action."
                ),
            })

    # 4. Low PPE compliance.
    for _, row in current_workers.iterrows():
        if row["PPE_Alert"] != "NO ALERT":
            central_alerts.append({
                "Source": "Worker",
                "ID": row["Worker ID"],
                "Alert_Type": "Low PPE Compliance",
                "Level": "Warning",
                "Recommended_Action": (
                    "Ensure the worker has and uses the required PPE."
                ),
            })

    # 5. High fatigue.
    for _, row in current_workers.iterrows():
        if row["Fatigue_Alert"] != "NO ALERT":
            central_alerts.append({
                "Source": "Worker",
                "ID": row["Worker ID"],
                "Alert_Type": "High Fatigue",
                "Level": "Warning",
                "Recommended_Action": (
                    "Review the worker's fatigue condition before work continues."
                ),
            })

    # 6. Overdue maintenance.
    for _, row in current_equipment.iterrows():
        if str(row["Maintenance_Status"]).strip().lower() == "overdue":
            central_alerts.append({
                "Source": "Equipment",
                "ID": row["Equipment_ID"],
                "Alert_Type": "Overdue Maintenance",
                "Level": "Warning",
                "Recommended_Action": "Schedule the required maintenance.",
            })

    # 7. High-risk safety observations.
    for _, row in current_workers.iterrows():
        worker_risk = str(row["Risk level"]).strip().lower()

        if worker_risk in ["high", "critical"]:
            central_alerts.append({
                "Source": "Worker",
                "ID": row["Worker ID"],
                "Alert_Type": "High-Risk Safety Observation",
                "Level": row["Risk level"],
                "Recommended_Action": (
                    "Review the safety observation and apply appropriate controls."
                ),
            })

    # 8. Excessive downtime.
    downtime_threshold = current_equipment["Downtime"].quantile(0.75)

    for _, row in current_equipment.iterrows():
        if row["Downtime"] > downtime_threshold:
            central_alerts.append({
                "Source": "Equipment",
                "ID": row["Equipment_ID"],
                "Alert_Type": "Excessive Downtime",
                "Level": "Warning",
                "Recommended_Action": (
                    "Investigate the cause of downtime and review maintenance needs."
                ),
            })

    alert_columns = [
        "Source",
        "ID",
        "Alert_Type",
        "Level",
        "Recommended_Action",
    ]

    alerts = pd.DataFrame(central_alerts, columns=alert_columns)

    # Dashboard KPIs.
    total_workers = len(current_workers)
    total_incidents = len(current_incidents)
    total_equipment = len(current_equipment)
    total_alerts = len(alerts)

    total_near_misses = current_workers["Near misses"].sum()

    ppe_compliance_rate = (
        current_workers["PPE compliance"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("yes")
        .mean()
        * 100
    )

    # The original project used high/critical incident risk records
    # for this dashboard KPI. We keep that calculation because the
    # supplied worker CSV does not have existing Risk level values.
    high_risk_observations = (
        current_incidents["Risk_Score"] >= 10
    ).sum()

    under_maintenance = (
        current_equipment["Maintenance_Status"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("under maintenance")
        .sum()
    )

    available_equipment = total_equipment - under_maintenance

    overdue_maintenance = (
        current_equipment["Maintenance_Status"]
        .astype(str)
        .str.strip()
        .str.lower()
        .eq("overdue")
        .sum()
    )

    average_availability = current_equipment["Availability"].mean()

    equipment_alerts = (
        alerts["Source"]
        .astype(str)
        .str.lower()
        .eq("equipment")
        .sum()
    )

    critical_equipment_alerts = (
        (
            alerts["Source"].str.lower() == "equipment"
        )
        &
        (
            alerts["Level"].str.lower() == "critical"
        )
    ).sum()

    return {
        "workers": current_workers,
        "incidents": current_incidents,
        "equipment": current_equipment,
        "alerts": alerts,
        "total_workers": total_workers,
        "total_incidents": total_incidents,
        "total_equipment": total_equipment,
        "total_alerts": total_alerts,
        "total_near_misses": total_near_misses,
        "ppe_compliance_rate": ppe_compliance_rate,
        "high_risk_observations": high_risk_observations,
        "under_maintenance": under_maintenance,
        "available_equipment": available_equipment,
        "overdue_maintenance": overdue_maintenance,
        "average_availability": average_availability,
        "equipment_alerts": equipment_alerts,
        "critical_equipment_alerts": critical_equipment_alerts,
    }


# ------------------------------------------------------------
# LOGIN PAGE
# ------------------------------------------------------------


def login_page():
    st.markdown('<span class="khwezi-login-marker"></span>', unsafe_allow_html=True)
    left, right = st.columns([1.0, 1.05], gap="large", vertical_alignment="top")
    with left:
        st.markdown("""
        <div style="text-align:center; padding:0 0 12px;">
          <div class="khwezi-logo"><span></span><span></span><span></span><span></span></div>
          <div class="khwezi-brand">KHWEZI MINING</div>
          <div class="khwezi-tagline">Safety First. Efficiency Always.</div>
          <div style="width:80px;height:3px;background:#c99a42;margin:19px auto;"></div>
          <div class="khwezi-system">Health, Safety &amp; Equipment<br>Monitoring System</div>
        </div>""", unsafe_allow_html=True)

    with right:
        with st.container(border=True, key="khwezi_login_card"):
            st.markdown('<span class="khwezi-login-card"></span>', unsafe_allow_html=True)
            st.markdown("<h3 style='text-align:center;color:#10283d;margin-bottom:0'>Welcome to Khwezi Mining</h3>", unsafe_allow_html=True)
            st.markdown("<p style='text-align:center;color:#6a7b8a'>Please sign in to continue</p>", unsafe_allow_html=True)
            username = st.text_input("Username", placeholder="Username")
            password = st.text_input("Password", type="password", placeholder="Password")
            if st.button("Login", type="primary", use_container_width=True):
                if username == "" or password == "":
                    st.warning("Please enter both username and password.")
                elif username in users["Username"].values:
                    current_user = users[users["Username"] == username]
                    if password in current_user["Password"].values:
                        st.session_state.logged_in = True
                        st.session_state.username = username
                        st.session_state.user_role = current_user["Role"].values[0]
                        st.rerun()
                    else:
                        st.error("Incorrect password. Please try again.")
                else:
                    st.error("Username not found. Please try again.")

            with st.expander("Forgot password?"):
                reset_username = st.text_input("Username", key="reset_username")
                reset_worker_id = st.text_input("Worker ID", key="reset_worker_id")
                reset_role = st.text_input("Role", key="reset_role")
                new_password = st.text_input("New password", type="password", key="reset_password")
                confirm_password = st.text_input("Confirm password", type="password", key="reset_confirm_password")
                if st.button("Change password"):
                    if reset_username not in users["Username"].values:
                        st.error("Username not found.")
                    else:
                        current_user = users[users["Username"] == reset_username]
                        if reset_worker_id not in current_user["Worker ID"].values:
                            st.error("Incorrect Worker ID.")
                        elif reset_role not in current_user["Role"].values:
                            st.error("Incorrect role.")
                        elif new_password == "" or new_password != confirm_password:
                            st.error("Passwords do not match or are empty.")
                        else:
                            users.loc[users["Username"] == reset_username, "Password"] = new_password
                            users.to_csv(USERS_FILE, index=False)
                            st.session_state.users = users
                            st.success("Password changed successfully.")
            st.markdown('<p class="khwezi-authorised">Authorised personnel only</p>', unsafe_allow_html=True)


# ------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------


def dashboard_page(data):
    import html
    import plotly.express as px
    import plotly.graph_objects as go

    st.title("Dashboard")
    st.markdown('<div class="khwezi-page-description">Mining Health, Safety and Equipment Monitoring</div>', unsafe_allow_html=True)

    def kpi(label, value, icon):
        st.markdown(
            f'<div class="khwezi-kpi"><div class="khwezi-kpi-icon">{icon}</div>'
            f'<div class="khwezi-kpi-number">{html.escape(str(value))}</div>'
            f'<div class="khwezi-kpi-label">{html.escape(label)}</div></div>',
            unsafe_allow_html=True,
        )

    # Consistent outline icons (inline SVG, no internet or extra dependency needed).
    icon_paths = {
        "workers": '<path d="M3 21v-2a4 4 0 0 1 4-4h10a4 4 0 0 1 4 4v2"/><circle cx="12" cy="7" r="4"/>',
        "incident": '<path d="M10 3h4l2 5v5H8V8zM6 13h12v7H6zM3 20h18M4 7l-2-2m18 2 2-2M12 1v1"/>',
        "warning": '<path d="m12 3 10 18H2L12 3z"/><path d="M12 9v5m0 3h.01"/>',
        "shield": '<path d="M12 22s8-4 8-11V5l-8-3-8 3v6c0 7 8 11 8 11z"/><path d="m9 12 2 2 4-4"/>',
        "helmet": '<path d="M4 16v-3a8 8 0 0 1 16 0v3M2 16h20v3H2zM12 5v11"/>',
        "truck": '<path d="M2 6h12v12H2zM14 10h4l4 4v4h-8z"/><circle cx="7" cy="19" r="2"/><circle cx="18" cy="19" r="2"/>',
        "check": '<rect x="3" y="3" width="18" height="18" rx="4"/><path d="m7 12 3 3 7-7"/>',
        "wrench": '<path d="M14 6a5 5 0 0 0-6 6L3 17a3 3 0 0 0 4 4l5-5a5 5 0 0 0 6-6l-4 3-3-3z"/>',
        "bell": '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9M10 21h4"/>',
        "chart": '<path d="M3 20h18M5 16v-5h3v5M11 16V5h3v11M17 16V9h3v7"/>',
        "critical": '<path d="M12 2 2 20h20L12 2zM12 8v6m0 3h.01"/>',
        "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 2v6m10-6v6M3 10h18M8 15h8"/>',
    }
    def svg(name):
        return '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">' + icon_paths[name] + '</svg>'

    cards = [
        ("Total Workers", data["total_workers"], svg("workers")),
        ("Safety Incidents", data["total_incidents"], svg("incident")),
        ("Near Misses", data["total_near_misses"], svg("warning")),
        ("High-Risk Observations", data["high_risk_observations"], svg("shield")),
        ("PPE Compliance", f'{data["ppe_compliance_rate"]:.1f}%', svg("helmet")),
        ("Total Equipment", data["total_equipment"], svg("truck")),
        ("Equipment Available", data["available_equipment"], svg("check")),
        ("Under Maintenance", data["under_maintenance"], svg("wrench")),
        ("Equipment Alerts", data["equipment_alerts"], svg("bell")),
        ("Average Availability", f'{data["average_availability"]:.1f}%', svg("chart")),
        ("Critical Equipment Alerts", data["critical_equipment_alerts"], svg("critical")),
        ("Overdue Maintenance", data["overdue_maintenance"], svg("calendar")),
    ]
    for offset in (0, 5, 10):
        group = cards[offset:offset + 5]
        cols = st.columns(len(group))
        for col, (label, value, icon) in zip(cols, group):
            with col:
                kpi(label, value, icon)

    palette = ["#c99a42", "#10283d", "#e36b5b", "#65a9bb", "#7b9e71", "#9b84b7"]

    def donut(frame, column, title):
        if column not in frame.columns or frame[column].dropna().empty:
            st.info(f"No {title.lower()} data available.")
            return
        counts = frame[column].fillna("Not specified").astype(str).value_counts().reset_index()
        counts.columns = ["Category", "Count"]
        fig = px.pie(counts, names="Category", values="Count", hole=.60,
                     color_discrete_sequence=palette)
        fig.update_traces(textposition="outside", textinfo="percent+label")
        fig.update_layout(height=340, margin=dict(l=12,r=12,t=12,b=12),
                          paper_bgcolor="white", font_color="#10283d",
                          legend=dict(orientation="h", y=-.15, font=dict(color="#10283d", size=12)),
                          font=dict(color="#10283d", size=13))
        fig.update_traces(textfont=dict(color="#10283d", size=12))
        st.plotly_chart(fig, use_container_width=True)

    def horizontal(frame, column, title):
        if column not in frame.columns or frame[column].dropna().empty:
            st.info(f"No {title.lower()} data available.")
            return
        counts = frame[column].fillna("Not specified").astype(str).value_counts().reset_index()
        counts.columns = ["Category", "Count"]
        fig = px.bar(counts, x="Count", y="Category", orientation="h",
                     color="Category", color_discrete_sequence=palette, text="Count")
        fig.update_layout(height=330, margin=dict(l=8,r=8,t=12,b=12),
                          paper_bgcolor="white", plot_bgcolor="white", showlegend=False,
                          font_color="#10283d", font=dict(color="#10283d", size=13), yaxis_title=None,
                          xaxis=dict(tickfont=dict(color="#10283d"), title_font=dict(color="#10283d")),
                          yaxis=dict(tickfont=dict(color="#10283d")))
        fig.update_traces(textposition="outside")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Safety and Risk Analysis")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("**Incidents by Severity**")
        donut(data["incidents"], "Severity", "Incident severity")
    with c2:
        st.markdown("**Risk Levels**")
        horizontal(data["incidents"], "Risk_Level", "Risk levels")

    st.subheader("Equipment and Maintenance Analysis")
    c3,c4 = st.columns(2)
    with c3:
        st.markdown("**Equipment Condition**")
        donut(data["equipment"], "Status", "Equipment condition")
    with c4:
        st.markdown("**Maintenance Status**")
        horizontal(data["equipment"], "Maintenance_Status", "Maintenance status")

    st.subheader("Operational Performance")
    c5,c6 = st.columns(2)
    with c5:
        st.markdown("**PPE Compliance**")
        st.progress(min(1.0, max(0.0, float(data["ppe_compliance_rate"]) / 100)))
        st.caption(f'{data["ppe_compliance_rate"]:.1f}% of recorded workers compliant')
    with c6:
        st.markdown("**Average Equipment Availability**")
        st.progress(min(1.0, max(0.0, float(data["average_availability"]) / 100)))
        st.caption(f'{data["average_availability"]:.1f}% average recorded availability')

    incidents = data["incidents"]
    date_col = next((col for col in ("Date", "Incident_Date", "Incident Date", "Date_Reported") if col in incidents.columns), None)
    if date_col:
        dates = pd.to_datetime(incidents[date_col], errors="coerce")
        if dates.notna().any():
            st.subheader("Incident Trend Over Time")
            trend = dates.dropna().dt.to_period("M").value_counts().sort_index()
            trend.index = trend.index.astype(str)
            st.line_chart(trend.rename("Incidents"), color="#c99a42")

    st.divider()
    st.subheader("Active Alerts")
    if data["alerts"].empty:
        st.success("No active alerts.")
    else:
        st.dataframe(data["alerts"], use_container_width=True)


# ------------------------------------------------------------
# WORKER SAFETY
# ------------------------------------------------------------


def worker_safety_page(data):
    st.title("Worker Safety Data")

    display_columns = [
        "Worker ID",
        "Department",
        "Job role",
        "Shift",
        "PPE compliance",
        "Safety training",
        "Fatigue level",
        "Safety observations",
        "Near misses",
        "Previous incidents",
        "Risk level",
    ]

    display_columns = [
        column for column in display_columns
        if column in data["workers"].columns
    ]

    st.subheader("Worker Database")
    st.dataframe(
        data["workers"][display_columns],
        use_container_width=True
    )

    st.divider()
    st.subheader("Add Worker Safety Record")

    worker_id = st.text_input("Worker ID")
    department = st.text_input("Department")
    job_role = st.text_input("Job role")
    shift = st.selectbox("Shift", ["Day", "Night"])
    ppe = st.selectbox("PPE compliance", ["Yes", "No"])
    training = st.selectbox(
        "Safety training",
        ["Complete", "Incomplete"]
    )
    fatigue = st.selectbox(
        "Fatigue level",
        ["Low", "Medium", "High"]
    )
    observation = st.text_area("Safety observation")
    near_misses = st.number_input(
        "Number of near misses",
        min_value=0,
        step=1
    )
    previous_incidents = st.number_input(
        "Number of previous incidents",
        min_value=0,
        step=1
    )
    worker_risk = st.selectbox(
        "Risk level",
        ["Low", "Medium", "High", "Critical"]
    )

    if st.button("Save Worker"):
        if worker_id == "" or department == "" or job_role == "":
            st.warning("Please complete Worker ID, Department and Job role.")

        elif worker_id in data["workers"]["Worker ID"].values:
            st.error("Worker ID already exists.")

        else:
            new_worker = pd.DataFrame(
                [[
                    worker_id,
                    department,
                    job_role,
                    shift,
                    ppe,
                    training,
                    fatigue,
                    observation,
                    near_misses,
                    previous_incidents,
                    worker_risk,
                ]],
                columns=[
                    "Worker ID",
                    "Department",
                    "Job role",
                    "Shift",
                    "PPE compliance",
                    "Safety training",
                    "Fatigue level",
                    "Safety observations",
                    "Near misses",
                    "Previous incidents",
                    "Risk level",
                ]
            )

            workers_updated = pd.concat(
                [data["workers"], new_worker],
                ignore_index=True,
                sort=False
            )

            workers_updated.to_csv(WORKERS_FILE, index=False)
            st.session_state.workers = workers_updated

            st.success("Worker information saved successfully.")

            if ppe == "No":
                st.warning("Warning: PPE non-compliance")

            if training == "Incomplete":
                st.warning("Warning: Safety training incomplete")

            if fatigue == "High":
                st.warning("Warning: High fatigue level")

            if worker_risk in ["High", "Critical"]:
                st.warning("Warning: High-risk safety observation")

            if ppe == "No" and training == "Incomplete" and fatigue == "High":
                st.error("ALERT: Multiple safety risks detected")

            st.dataframe(
                workers_updated,
                use_container_width=True
            )


# ------------------------------------------------------------
# SAFETY INCIDENTS
# ------------------------------------------------------------


def incident_page(data):
    st.title("Safety Incidents")

    action = st.selectbox(
        "Choose an action",
        [
            "Add New Incident",
            "View All Incidents",
            "Search Incident",
            "Count Incidents",
            "Filter Incidents",
            "Incident Trends",
        ]
    )

    current_incidents = data["incidents"]

    if action == "Add New Incident":
        incident_id = st.text_input("Incident ID")
        worker_id = st.text_input("Worker ID")
        department = st.selectbox(
            "Department",
            ["Mining", "Processing", "Maintenance", "Engineering"]
        )
        date = st.date_input("Date")
        time = st.time_input("Time")
        shift = st.selectbox("Shift", ["Day", "Night"])
        location = st.text_input("Location")
        incident_type = st.selectbox(
            "Incident type",
            ["Slip/Fall", "Equipment", "PPE", "Injury", "Other"]
        )
        description = st.text_area("Incident description")
        injury_status = st.selectbox(
            "Injury status",
            ["No Injury", "Injury"]
        )
        lti_status = st.selectbox(
            "Lost-time injury status",
            ["No", "Yes"]
        )
        cause = st.text_input("Cause")
        corrective_action = st.text_area("Corrective action")
        likelihood = st.number_input(
            "Likelihood (1-5)",
            min_value=1,
            max_value=5,
            value=1,
            step=1
        )
        consequence = st.number_input(
            "Consequence (1-5)",
            min_value=1,
            max_value=5,
            value=1,
            step=1
        )
        status = st.selectbox(
            "Incident status",
            ["Open", "Closed", "Under Investigation"]
        )

        if st.button("Add Incident"):
            if incident_id == "" or worker_id == "":
                st.warning("Please enter the Incident ID and Worker ID.")

            elif incident_id in current_incidents["Incident_ID"].values:
                st.error("Incident ID already exists.")

            else:
                risk_score = likelihood * consequence
                severity = risk_level(risk_score)

                new_row = {
                    "Incident_ID": incident_id,
                    "Worker_ID": worker_id,
                    "Department": department,
                    "Date": str(date),
                    "Time": str(time),
                    "Shift": shift,
                    "Location": location,
                    "Incident_Type": incident_type,
                    "Description": description,
                    "Injury_Status": injury_status,
                    "LTI_Status": lti_status,
                    "Cause": cause,
                    "Corrective_Action": corrective_action,
                    "Severity": severity,
                    "Incident_Status": status,
                    "Likelihood": likelihood,
                    "Consequence": consequence,
                }

                updated = pd.concat(
                    [current_incidents, pd.DataFrame([new_row])],
                    ignore_index=True,
                    sort=False
                )

                updated.to_csv(INCIDENTS_FILE, index=False)
                st.session_state.incidents = updated

                st.success("Incident successfully added!")
                st.write("Risk Score:", risk_score)
                st.write("Severity:", severity)

                if severity in ["High", "Critical"]:
                    st.warning(
                        f"Warning: {severity} risk incident identified."
                    )

                st.dataframe(
                    updated.tail(),
                    use_container_width=True
                )

    elif action == "View All Incidents":
        st.dataframe(
            current_incidents,
            use_container_width=True
        )

    elif action == "Search Incident":
        incident_id = st.text_input("Enter Incident ID to search")

        if st.button("Search Incident"):
            result = current_incidents[
                current_incidents["Incident_ID"] == incident_id
            ]

            if result.empty:
                st.warning("Incident not found.")
            else:
                st.success("Incident found.")
                st.dataframe(result, use_container_width=True)

    elif action == "Count Incidents":
        st.metric("Total number of incidents", len(current_incidents))

    elif action == "Filter Incidents":
        filter_type = st.selectbox(
            "Filter by",
            [
                "Department",
                "Incident Type",
                "Severity",
                "Incident Status",
            ]
        )

        if filter_type == "Department":
            value = st.selectbox(
                "Department",
                ["Mining", "Processing", "Maintenance", "Engineering"]
            )
            result = current_incidents[
                current_incidents["Department"].str.lower() == value.lower()
            ]

        elif filter_type == "Incident Type":
            values = current_incidents["Incident_Type"].dropna().unique().tolist()
            value = st.selectbox(
                "Incident type",
                values if values else ["No data"]
            )
            result = current_incidents[
                current_incidents["Incident_Type"] == value
            ]

        elif filter_type == "Severity":
            value = st.selectbox(
                "Severity",
                ["Low", "Medium", "High", "Critical"]
            )
            result = current_incidents[
                current_incidents["Severity"].str.lower() == value.lower()
            ]

        else:
            value = st.selectbox(
                "Incident status",
                ["Open", "Closed", "Under Investigation"]
            )
            result = current_incidents[
                current_incidents["Incident_Status"].str.lower() == value.lower()
            ]

        st.dataframe(result, use_container_width=True)

    else:
        st.subheader("Incident Trends")

        dates = pd.to_datetime(
            current_incidents["Date"],
            errors="coerce"
        )

        trend = current_incidents.copy()
        trend["Date"] = dates
        trend = trend.dropna(subset=["Date"])

        if trend.empty:
            st.write("No usable dates are available for a trend chart.")
        else:
            trend = trend.groupby("Date").size()
            st.line_chart(trend)


# ------------------------------------------------------------
# EQUIPMENT
# ------------------------------------------------------------


def equipment_page(data):
    st.title("🚜 Equipment Data")

    st.info(
        "Temperature and vibration thresholds are educational prototype "
        "thresholds from the project brief, not actual manufacturer or mine limits."
    )

    st.subheader("Equipment Database")
    st.dataframe(
        data["equipment"],
        use_container_width=True
    )

    st.divider()
    st.subheader("Equipment Requiring Attention")

    attention = data["equipment"][
        data["equipment"]["Status"] != "NORMAL"
    ]

    if attention.empty:
        st.success("No equipment requires attention.")
    else:
        st.dataframe(
            attention[
                [
                    "Equipment_ID",
                    "Equipment_Type",
                    "Temperature",
                    "Vibration",
                    "Status",
                    "Status_Message",
                ]
            ],
            use_container_width=True
        )

    st.divider()
    st.subheader("Equipment Condition")
    _khwezi_section_chart(data["equipment"]["Status"], "donut", "Equipment Condition")

    st.subheader("Equipment Type")
    _khwezi_section_chart(data["equipment"]["Equipment_Type"], "horizontal", "Equipment Type")

    st.divider()
    st.subheader("Equipment Analysis")

    question = st.selectbox(
        "Select a question",
        [
            "Which equipment has the highest downtime?",
            "Which equipment has the lowest availability?",
            "Which equipment has the highest vibration?",
            "Which equipment has the highest operating temperature?",
            "Which equipment has generated the most alerts?",
            "Which equipment is overdue for maintenance?",
            "Which equipment requires immediate inspection?",
        ]
    )

    equipment_data = data["equipment"]

    if question == "Which equipment has the highest downtime?":
        result = equipment_data.nlargest(10, "Downtime")[
            ["Equipment_ID", "Equipment_Type", "Downtime"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has the lowest availability?":
        result = equipment_data.nsmallest(10, "Availability")[
            ["Equipment_ID", "Equipment_Type", "Availability"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has the highest vibration?":
        result = equipment_data.nlargest(10, "Vibration")[
            ["Equipment_ID", "Equipment_Type", "Vibration"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has the highest operating temperature?":
        result = equipment_data.nlargest(10, "Temperature")[
            ["Equipment_ID", "Equipment_Type", "Temperature"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has generated the most alerts?":
        result = equipment_data.nlargest(10, "Alert_Count")[
            ["Equipment_ID", "Equipment_Type", "Alert_Count"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment is overdue for maintenance?":
        result = equipment_data[
            equipment_data["Maintenance_Status"]
            .astype(str)
            .str.lower()
            == "overdue"
        ]
        st.dataframe(result, use_container_width=True)

    else:
        result = equipment_data[
            equipment_data["Status"] == "CRITICAL"
        ]
        st.dataframe(result, use_container_width=True)


# ------------------------------------------------------------
# MAINTENANCE
# ------------------------------------------------------------


def _khwezi_section_chart(values, kind="donut", title=""):
    """Visual-only chart for existing category counts; never changes source data."""
    import plotly.express as px
    counts = values.dropna().astype(str).value_counts().rename_axis("Category").reset_index(name="Count")
    if counts.empty:
        st.info("No data available for this chart.")
        return
    colors = ["#c99a42", "#10283d", "#e36b5b", "#65a9bb", "#7b9e71", "#9b84b7", "#df8a46", "#537eaa"]
    risk_colors = {"critical":"#d94841", "high":"#ed8733",
                   "medium":"#d3a13e", "low":"#4d9b69"}
    category_colors = ({str(c): risk_colors[str(c).strip().lower()] for c in counts["Category"]}
                       if title == "Risk Level Counts" else None)
    if kind == "donut":
        fig = px.pie(counts, names="Category", values="Count", hole=0.60,
                     color="Category", color_discrete_sequence=colors)
        fig.update_traces(textposition="outside", textinfo="label+percent",
                          textfont=dict(color="#10283d", size=13))
        fig.update_layout(height=380, showlegend=True,
                          legend=dict(orientation="h", y=-0.12, font=dict(color="#10283d", size=12)))
    else:
        counts = counts.sort_values("Count", ascending=True)
        fig = px.bar(counts, x="Count", y="Category", orientation="h",
                     color="Category", color_discrete_sequence=colors,
                     color_discrete_map=category_colors, text="Count")
        fig.update_traces(textposition="outside", cliponaxis=False)
        fig.update_layout(height=max(330, 55 * len(counts) + 100), showlegend=False,
                          xaxis=dict(title="Count", gridcolor="#e4eaf0", color="#10283d",
                                     rangemode="tozero"),
                          yaxis=dict(title=None, color="#10283d"))
    fig.update_layout(template="plotly_white", paper_bgcolor="white", plot_bgcolor="white",
                      font=dict(color="#10283d", size=13),
                      margin=dict(l=105, r=45, t=22, b=65))
    fig.update_xaxes(tickfont=dict(color="#10283d", size=12),
                     title_font=dict(color="#10283d", size=13),
                     linecolor="#a7b6c5", tickcolor="#a7b6c5")
    fig.update_yaxes(tickfont=dict(color="#10283d", size=12),
                     title_font=dict(color="#10283d", size=13),
                     linecolor="#a7b6c5", tickcolor="#a7b6c5")
    st.plotly_chart(fig, use_container_width=True)


def maintenance_page(data):
    st.title("🔧 Maintenance")

    status = data["equipment"]["Maintenance_Status"]

    due = status.astype(str).str.lower().eq("due").sum()
    overdue = status.astype(str).str.lower().eq("overdue").sum()
    under = status.astype(str).str.lower().eq("under maintenance").sum()
    low_availability = (
        data["equipment"]["Calculated_Availability"] < 85
    ).sum()

    row = st.columns(4)
    row[0].metric("Due", due)
    row[1].metric("Overdue", overdue)
    row[2].metric("Under Maintenance", under)
    row[3].metric("Low Availability", low_availability)

    st.divider()

    st.subheader("Maintenance Status")
    _khwezi_section_chart(status, "donut", "Maintenance Status")

    st.subheader("Maintenance Monitoring Table")
    st.dataframe(
        data["equipment"][
            [
                "Equipment_ID",
                "Maintenance_Status",
                "Downtime",
                "Alert_Count",
                "Calculated_Availability",
                "Maintenance_Flags",
            ]
        ],
        use_container_width=True
    )

    st.subheader("Equipment With Maintenance Concerns")
    concerns = data["equipment"][
        data["equipment"]["Maintenance_Flags"] != "None"
    ]

    if concerns.empty:
        st.success("No maintenance concerns identified.")
    else:
        st.dataframe(
            concerns,
            use_container_width=True
        )


# ------------------------------------------------------------
# RISK ASSESSMENT
# ------------------------------------------------------------


def risk_assessment_page(data):
    st.title("⚠️ Risk Assessment")
    st.write("Risk Score = Likelihood × Consequence")
    st.write("1-4 Low | 5-9 Medium | 10-16 High | 17-25 Critical")

    st.dataframe(
        data["incidents"][
            [
                "Incident_ID",
                "Department",
                "Date",
                "Incident_Type",
                "Likelihood",
                "Consequence",
                "Risk_Score",
                "Risk_Level",
            ]
        ],
        use_container_width=True
    )

    selected = st.selectbox(
        "Filter risk level",
        ["All", "Low", "Medium", "High", "Critical"]
    )

    if selected == "All":
        result = data["incidents"]
    else:
        result = data["incidents"][
            data["incidents"]["Risk_Level"].str.lower() == selected.lower()
        ]

    st.dataframe(
        result[
            [
                "Incident_ID",
                "Department",
                "Risk_Score",
                "Risk_Level",
                "Incident_Status",
            ]
        ],
        use_container_width=True
    )

    if selected in ["High", "Critical"] and not result.empty:
        st.warning(
            f"Warning: {selected} risk has been identified. Review the incidents and apply appropriate controls."
        )

    st.subheader("Risk Level Counts")
    _khwezi_section_chart(data["incidents"]["Risk_Level"], "horizontal", "Risk Level Counts")


# ------------------------------------------------------------
# INTERACTIVE DATA ANALYSIS
# ------------------------------------------------------------


def analysis_page(data):
    st.title("🔎 Interactive Data Analysis")
    st.write(
        "Use the questions below to answer meaningful mining engineering "
        "questions from the project datasets."
    )

    question = st.selectbox(
        "Select an analysis question",
        [
            "How many safety incidents occurred during the selected period?",
            "Which department has the highest number of incidents?",
            "Which shift records the most incidents?",
            "What percentage of workers comply with PPE requirements?",
            "How many near misses have been recorded?",
            "Which incident types occur most frequently?",
            "How many incidents are classified as high or critical?",
            "Which departments have the highest safety risk?",
            "Is there a difference in incidents between day and night shifts?",
            "Which equipment has the highest downtime?",
            "Which equipment has the lowest availability?",
            "Which equipment has the highest vibration?",
            "Which equipment has the highest operating temperature?",
            "Which equipment has generated the most alerts?",
            "Which equipment requires maintenance?",
            "Which equipment is overdue for maintenance?",
            "What is the average equipment availability?",
            "Which equipment type has the highest downtime?",
            "Are safety incidents associated with particular shifts?",
            "Which departments have both high safety risk and high equipment downtime?",
            "Which equipment contributes to the greatest number of alerts?",
            "What are the most common causes of safety incidents?",
            "Which safety indicators require management intervention?",
            "Which safety conditions require immediate attention?",
            "What percentage of monitored equipment is operating normally?",
            "How many critical alerts are currently active?",
            "Which areas of the operation require the greatest attention?",
            "What recommendations can be generated from the monitoring results?",
        ]
    )

    incident_data = data["incidents"].copy()
    equipment_data = data["equipment"].copy()
    worker_data = data["workers"].copy()

    if question == "How many safety incidents occurred during the selected period?":
        dates = pd.to_datetime(incident_data["Date"], errors="coerce")
        valid_dates = dates.dropna()

        if valid_dates.empty:
            st.write("No usable incident dates are available.")
        else:
            start_date = st.date_input(
                "Start date",
                value=valid_dates.min().date()
            )
            end_date = st.date_input(
                "End date",
                value=valid_dates.max().date()
            )

            selected = incident_data[
                (dates.dt.date >= start_date)
                &
                (dates.dt.date <= end_date)
            ]

            st.metric(
                "Incidents in selected period",
                len(selected)
            )

    elif question == "Which department has the highest number of incidents?":
        counts = incident_data["Department"].value_counts()
        st.bar_chart(counts)
        st.write("Department with the most incidents:", counts.idxmax())

    elif question == "Which shift records the most incidents?":
        counts = incident_data["Shift"].value_counts()
        st.bar_chart(counts)
        st.write("Shift with the most incidents:", counts.idxmax())

    elif question == "What percentage of workers comply with PPE requirements?":
        rate = (
            worker_data["PPE compliance"]
            .astype(str)
            .str.strip()
            .str.lower()
            .eq("yes")
            .mean()
            * 100
        )
        st.metric("PPE Compliance", f"{rate:.1f}%")

    elif question == "How many near misses have been recorded?":
        st.metric(
            "Total Near Misses",
            worker_data["Near misses"].sum()
        )

    elif question == "Which incident types occur most frequently?":
        counts = incident_data["Incident_Type"].value_counts()
        st.bar_chart(counts)
        st.write("Most frequent incident type:", counts.idxmax())

    elif question == "How many incidents are classified as high or critical?":
        count = incident_data["Risk_Level"].isin(
            ["High", "Critical"]
        ).sum()
        st.metric("High or Critical Incidents", count)

    elif question == "Which departments have the highest safety risk?":
        result = (
            incident_data.groupby("Department")["Risk_Score"]
            .mean()
            .sort_values(ascending=False)
        )
        st.bar_chart(result)
        st.write("Highest average department risk:", result.idxmax())

    elif question == "Is there a difference in incidents between day and night shifts?":
        counts = incident_data["Shift"].value_counts()
        st.bar_chart(counts)

        day = int(counts.get("Day", 0))
        night = int(counts.get("Night", 0))

        st.write(f"Day shift incidents: {day}")
        st.write(f"Night shift incidents: {night}")

    elif question == "Which equipment has the highest downtime?":
        result = equipment_data.nlargest(10, "Downtime")[
            ["Equipment_ID", "Equipment_Type", "Downtime"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has the lowest availability?":
        result = equipment_data.nsmallest(10, "Availability")[
            ["Equipment_ID", "Equipment_Type", "Availability"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has the highest vibration?":
        result = equipment_data.nlargest(10, "Vibration")[
            ["Equipment_ID", "Equipment_Type", "Vibration"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has the highest operating temperature?":
        result = equipment_data.nlargest(10, "Temperature")[
            ["Equipment_ID", "Equipment_Type", "Temperature"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment has generated the most alerts?":
        result = equipment_data.nlargest(10, "Alert_Count")[
            ["Equipment_ID", "Equipment_Type", "Alert_Count"]
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment requires maintenance?":
        result = equipment_data[
            equipment_data["Maintenance_Status"]
            .astype(str)
            .str.lower()
            != "up to date"
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "Which equipment is overdue for maintenance?":
        result = equipment_data[
            equipment_data["Maintenance_Status"]
            .astype(str)
            .str.lower()
            == "overdue"
        ]
        st.dataframe(result, use_container_width=True)

    elif question == "What is the average equipment availability?":
        average = equipment_data["Availability"].mean()
        st.metric("Average Availability", f"{average:.2f}%")

    elif question == "Which equipment type has the highest downtime?":
        result = (
            equipment_data.groupby("Equipment_Type")["Downtime"]
            .sum()
            .sort_values(ascending=False)
        )
        st.bar_chart(result)
        st.write("Equipment type with highest total downtime:", result.idxmax())

    elif question == "Are safety incidents associated with particular shifts?":
        result = incident_data.groupby(
            "Shift"
        ).size().sort_values(ascending=False)
        st.bar_chart(result)
        st.write("Shift with the most incidents:", result.idxmax())

    elif question == "Which departments have both high safety risk and high equipment downtime?":
        risk_by_department = incident_data.groupby(
            "Department"
        )["Risk_Score"].mean()

        downtime_by_type = equipment_data.groupby(
            "Equipment_Type"
        )["Downtime"].sum()

        st.write("Average incident risk by department")
        st.bar_chart(risk_by_department)

        st.write("Equipment downtime by equipment type")
        st.bar_chart(downtime_by_type)

        st.info(
            "Compare the two results when identifying areas where safety risk "
            "and equipment downtime require joint management attention."
        )

    elif question == "Which equipment contributes to the greatest number of alerts?":
        result = equipment_data.nlargest(10, "Alert_Count")[
            ["Equipment_ID", "Equipment_Type", "Alert_Count"]
        ]
        st.dataframe(result, use_container_width=True)
        st.bar_chart(
            result.set_index("Equipment_ID")["Alert_Count"]
        )

    elif question == "What are the most common causes of safety incidents?":
        counts = (
            incident_data["Cause"]
            .fillna("Unknown")
            .value_counts()
        )
        st.bar_chart(counts.head(10))
        st.write("Most common cause:", counts.idxmax())

    elif question == "Which safety indicators require management intervention?":
        indicators = {
            "High/Critical risk incidents": int(
                incident_data["Risk_Level"].isin(["High", "Critical"]).sum()
            ),
            "Workers with high fatigue": int(
                worker_data["Fatigue level"].astype(str).str.lower().eq("high").sum()
            ),
            "Workers with low PPE compliance": int(
                worker_data["PPE compliance"].astype(str).str.lower().eq("no").sum()
            ),
            "Overdue equipment": int(
                equipment_data["Maintenance_Status"].astype(str).str.lower().eq("overdue").sum()
            ),
            "Critical equipment": int(
                equipment_data["Status"].eq("CRITICAL").sum()
            ),
        }
        st.bar_chart(pd.Series(indicators))
        st.dataframe(
            pd.DataFrame(
                list(indicators.items()),
                columns=["Indicator", "Count"]
            ),
            use_container_width=True
        )

    elif question == "Which safety conditions require immediate attention?":
        immediate = data["alerts"][
            data["alerts"]["Level"].astype(str).str.lower().isin(
                ["critical", "high"]
            )
        ]

        if immediate.empty:
            st.success("No high or critical safety conditions are currently recorded.")
        else:
            st.dataframe(
                immediate,
                use_container_width=True
            )

    elif question == "What percentage of monitored equipment is operating normally?":
        rate = (
            equipment_data["Status"].eq("NORMAL").mean()
            * 100
        )
        st.metric("Equipment Operating Normally", f"{rate:.1f}%")

    elif question == "How many critical alerts are currently active?":
        count = (
            data["alerts"]["Level"]
            .astype(str)
            .str.lower()
            .eq("critical")
            .sum()
        )
        st.metric("Critical Active Alerts", count)

    elif question == "Which areas of the operation require the greatest attention?":
        st.write("Current critical or high-risk workers")
        worker_risk = worker_data[
            worker_data["Risk level"].astype(str).str.lower().isin(
                ["high", "critical"]
            )
        ]
        st.dataframe(worker_risk, use_container_width=True)

        st.write("Current critical equipment")
        critical_equipment = equipment_data[
            equipment_data["Status"] == "CRITICAL"
        ]
        st.dataframe(critical_equipment, use_container_width=True)

        st.write("Overdue maintenance")
        overdue = equipment_data[
            equipment_data["Maintenance_Status"].astype(str).str.lower()
            == "overdue"
        ]
        st.dataframe(overdue, use_container_width=True)

    else:
        st.write("### Recommendations")

        recommendations = []

        if data["critical_equipment_alerts"] > 0:
            recommendations.append(
                "Prioritise inspection of equipment with critical temperature or vibration alerts."
            )

        if data["overdue_maintenance"] > 0:
            recommendations.append(
                "Prioritise overdue equipment maintenance."
            )

        if data["ppe_compliance_rate"] < 100:
            recommendations.append(
                "Address worker PPE non-compliance through supervision and corrective action."
            )

        if data["total_alerts"] == 0:
            recommendations.append(
                "Continue routine monitoring because no active alerts are currently recorded."
            )

        if not recommendations:
            recommendations.append(
                "Continue monitoring safety, risk and equipment indicators regularly."
            )

        for recommendation in recommendations:
            st.write("-", recommendation)


# ------------------------------------------------------------
# ALERTS
# ------------------------------------------------------------


def alerts_page(data):
    st.title("🔔 Alerts and Notifications")

    st.metric("Active Alerts", data["total_alerts"])

    if data["alerts"].empty:
        st.success("No active alerts.")
    else:
        st.dataframe(
            data["alerts"],
            use_container_width=True
        )

        st.subheader("Alerts by Level")
        _khwezi_section_chart(data["alerts"]["Level"], "donut", "Alerts by Level")


# ------------------------------------------------------------
# REPORTS
# ------------------------------------------------------------


def reports_page(data):
    st.title("📑 Reports")
    st.write("Download current project data and alert information.")

    st.download_button(
        "Download Workers CSV",
        data["workers"].to_csv(index=False),
        "workers_report.csv",
        "text/csv"
    )

    st.download_button(
        "Download Incidents CSV",
        data["incidents"].to_csv(index=False),
        "incidents_report.csv",
        "text/csv"
    )

    st.download_button(
        "Download Equipment CSV",
        data["equipment"].to_csv(index=False),
        "equipment_report.csv",
        "text/csv"
    )

    st.download_button(
        "Download Alerts CSV",
        data["alerts"].to_csv(index=False),
        "alerts_report.csv",
        "text/csv"
    )


# ------------------------------------------------------------
# MANAGE USERS
# ------------------------------------------------------------


def manage_users_page():
    st.title("👤 Manage Users")

    choice = st.selectbox(
        "Choose an action",
        ["View Users", "Add User", "Remove User"]
    )

    current_users = st.session_state.users

    if choice == "View Users":
        st.dataframe(
            current_users,
            use_container_width=True
        )

    elif choice == "Add User":
        worker_id = st.text_input("Worker ID")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.selectbox(
            "Role",
            [
                "Administrator",
                "Safety Officer",
                "Mining Engineer",
                "Maintenance Engineer",
                "Manager",
            ]
        )

        if st.button("Add User"):
            if worker_id == "" or username == "" or password == "":
                st.warning("Please complete all fields.")
            elif worker_id in current_users["Worker ID"].values:
                st.error("Worker ID already exists.")
            elif username in current_users["Username"].values:
                st.error("Username already exists.")
            else:
                new_user = pd.DataFrame(
                    [[worker_id, username, password, role]],
                    columns=[
                        "Worker ID",
                        "Username",
                        "Password",
                        "Role",
                    ]
                )

                updated_users = pd.concat(
                    [current_users, new_user],
                    ignore_index=True
                )

                updated_users.to_csv(
                    USERS_FILE,
                    index=False
                )

                st.session_state.users = updated_users
                st.success("User added successfully.")
                st.dataframe(
                    updated_users,
                    use_container_width=True
                )

    else:
        username = st.text_input("Username to remove")

        if st.button("Remove User"):
            if username in current_users["Username"].values:
                updated_users = current_users[
                    current_users["Username"] != username
                ]

                updated_users.to_csv(
                    USERS_FILE,
                    index=False
                )

                st.session_state.users = updated_users
                st.success("User removed successfully.")
                st.dataframe(
                    updated_users,
                    use_container_width=True
                )
            else:
                st.error("Username not found.")


# ------------------------------------------------------------
# MAIN APPLICATION
# ------------------------------------------------------------


def main():
    if not st.session_state.logged_in:
        login_page()
        return

    data = build_project_data()

    st.markdown("<div class=\"khwezi-topline\">▥ &nbsp; KHWEZI MINING &nbsp; <span style=\"float:right;letter-spacing:0;font-weight:400\">Safety First. Efficiency Always.</span></div>", unsafe_allow_html=True)
    st.sidebar.title("▥ KHWEZI MINING")
    st.sidebar.write("Username:", st.session_state.username)
    st.sidebar.write("Role:", st.session_state.user_role)
    st.sidebar.divider()

    pages = []

    # The permission names below match the supplied permissions.csv
    # and the access table in the project brief.
    if has_access("View Dashboard"):
        pages += [
            "📊 Dashboard",
            "🔎 Interactive Analysis",
            "🔔 Alerts",
        ]

    if has_access("Worker safety data"):
        pages.append("👷 Worker Data")

    if has_access("Safety incidents"):
        pages.append("🚨 Safety Incidents")

    if has_access("Equipment data"):
        pages.append("🚜 Equipment Data")

    if has_access("Maintenance data"):
        pages.append("🔧 Maintenance")

    if has_access("Risk Assessment"):
        pages.append("⚠️ Risk Assessment")

    if has_access("Generate reports"):
        pages.append("📑 Reports")

    if has_access("Manage user"):
        pages.append("👤 Manage Users")

    # Explicit, permanently labelled navigation buttons (not emoji-only radio controls).
    nav_icons = {
        "📊 Dashboard": ":material/dashboard:",
        "🔎 Interactive Analysis": ":material/analytics:",
        "🔔 Alerts": ":material/notifications_active:",
        "👷 Worker Data": ":material/engineering:",
        "🚨 Safety Incidents": ":material/emergency:",
        "🚜 Equipment Data": ":material/precision_manufacturing:",
        "🔧 Maintenance": ":material/build:",
        "⚠️ Risk Assessment": ":material/health_and_safety:",
        "📑 Reports": ":material/description:",
        "👤 Manage Users": ":material/manage_accounts:",
    }
    if st.session_state.get("khwezi_nav_page") not in pages:
        st.session_state["khwezi_nav_page"] = pages[0] if pages else None
    for nav_page in pages:
        display_name = nav_page.split(" ", 1)[-1]
        selected = st.session_state["khwezi_nav_page"] == nav_page
        if st.sidebar.button(display_name, icon=nav_icons.get(nav_page),
                             key="nav_" + display_name.replace(" ", "_"),
                             type="primary" if selected else "secondary",
                             use_container_width=True):
            st.session_state["khwezi_nav_page"] = nav_page
            st.rerun()
    page = st.session_state["khwezi_nav_page"]

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.user_role = ""
        st.rerun()

    if page == "📊 Dashboard":
        dashboard_page(data)

    elif page == "🔎 Interactive Analysis":
        analysis_page(data)

    elif page == "🔔 Alerts":
        alerts_page(data)

    elif page == "👷 Worker Data":
        worker_safety_page(data)

    elif page == "🚨 Safety Incidents":
        incident_page(data)

    elif page == "🚜 Equipment Data":
        equipment_page(data)

    elif page == "🔧 Maintenance":
        maintenance_page(data)

    elif page == "⚠️ Risk Assessment":
        risk_assessment_page(data)

    elif page == "📑 Reports":
        reports_page(data)

    elif page == "👤 Manage Users":
        manage_users_page()


if __name__ == "__main__":
    main()
