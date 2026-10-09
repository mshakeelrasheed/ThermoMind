import html
import json
from pathlib import Path
import pandas as pd
import streamlit as st
import pydeck as pdk
import folium
from streamlit_folium import st_folium
from fpdf import FPDF
from datetime import datetime
from samples import SAN_ANTONIO_POINT, SAN_ANTONIO_POLYGON
from risk_engine import ThermoMindRiskEngine
from agent import OpenSourceThermoMindAgent

st.set_page_config(
    page_title="ThermoMind | Heat intelligence",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

CACHE_DIR = Path(__file__).resolve().parent / "thermomind" / "cache"
DATASETS = {
    "TCM heatmap": "san_antonio_tcm.json",
    "Exceedance": "san_antonio_exceedance.json",
    "Persistence": "san_antonio_persistence.json",
    "Environment": "san_antonio_env_params.json",
    "Satellite": "san_antonio_satellite.json",
}

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
    :root { --ink:#16212b; --muted:#66737d; --paper:#f5f7f4; --line:#dbe2df; --mint:#b9e7c5; --coral:#f48b75; --blue:#155b78; }
    html, body, [class*="css"] { font-family:'DM Sans', sans-serif; color:var(--ink) !important; }
    h1, h2, h3, h4, p, label, [data-testid="stMetricLabel"], [data-testid="stMetricValue"], [data-testid="stMetricDelta"] { color:var(--ink) !important; }
    [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li { color:var(--ink); }
    [data-testid="stMetricLabel"], [data-testid="stMetricDelta"] { color:var(--muted) !important; }
    [data-testid="stMetricValue"] { color:var(--ink) !important; }
    [data-testid="stAppViewContainer"] { background:var(--paper); }
    [data-testid="stHeader"] { background:transparent; }
    [data-testid="stSidebar"] { background:#16212b; }
    [data-testid="stSidebar"] * { color:#eef5f1 !important; }
    [data-testid="stSidebar"] .block-container { padding-top: 0.3rem !important; }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] .stCaption, [data-testid="stSidebar"] label { line-height:1.4 !important; }
    .block-container { padding-top: 0.8rem !important; }
    .sidebar-title { margin-top: 0.1rem; margin-bottom: 0.15rem; }
    .sidebar-title h2 { font-size: 2.05rem !important; line-height: 1.02 !important; letter-spacing: -0.04em !important; margin: 0 !important; }
    .eyebrow { font-family:'Space Mono', monospace; font-size:11px; letter-spacing:1.5px; text-transform:uppercase; color:var(--blue); font-weight:700; }
    .hero { padding:6px 0 18px; border-bottom:1px solid var(--line); margin-bottom:24px; }
    .hero h1 { color:var(--ink) !important; font-size:42px; letter-spacing:0; margin:8px 0 10px; }
    .hero p { color:var(--muted); font-size:16px; margin:0; }
    .panel { background:white; border:1px solid var(--line); border-radius:10px; padding:20px; height:100%; }
    .panel, .panel h3, .panel p, .panel li, .panel strong { color:var(--ink) !important; }
    .panel h3 { margin:3px 0 12px; font-size:19px; }
    .panel p, .panel li { color:var(--muted) !important; }
    .status { display:inline-block; padding:5px 10px; border-radius:99px; font-size:12px; font-weight:700; background:#fff0d6; color:#734b00 !important; }
    .status.ready { background:#d9f3df; color:#14372f !important; }
    .status.error { background:#ffe0da; color:#7d2b1b !important; }
    .kicker { color:var(--muted); font-size:12px; text-transform:uppercase; letter-spacing:.8px; }
    .big-number { font-size:30px; font-weight:700; margin-top:3px; }
    .chat-card { background:white; border:1px solid var(--line); border-radius:10px; padding:18px 20px 8px; }
    .chat-card h2, .chat-card h3, .chat-card p { color:var(--ink) !important; }
    .thermomind-shell { background:white; border:1px solid var(--line); border-radius:18px; padding:28px 24px 24px; margin-bottom:12px; height:100%; }
    .thermomind-shell .eyebrow { margin-bottom:8px; font-family:'Space Mono', monospace; font-size:11px; letter-spacing:1.4px; text-transform:uppercase; color:#4c5b66; }
    .thermomind-shell h2 { margin:0 0 12px; font-size:2.2rem; line-height:1.08; font-weight:700; }
    .thermomind-shell p { margin:0; color:var(--muted) !important; }
    .suggestion-list { margin:12px 0 0; padding-left:1.2rem; color:var(--ink); }
    .suggestion-list li { margin:0.35rem 0; line-height:1.45; color:#202a33 !important; }
    
    [data-testid="column"], [data-testid="stHorizontalBlock"] { 
        border: none !important; 
        background: transparent !important; 
        outline: none !important;
        align-items: flex-end !important;
    }
    
    .stTextInput {
        background-color: #16212b !important;
        border: 1.5px solid #82E0AA !important;
        border-radius: 10px !important;
        margin-top: 0px !important;
    }

    .stTextInput > label {
        display: none !important;
        height: 0px !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    div[data-baseweb="base-input"], div[data-baseweb="input"], div[data-baseweb="input"] > div {
        background-color: #16212b !important;
        background: #16212b !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    .stTextInput input {
        background-color: transparent !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        opacity: 1 !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0.65rem 1rem !important;
        font-size: 1rem !important;
        caret-color: #ffffff !important;
    }
    
    .stTextInput input::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }

    div.stFormSubmitButton {
        margin-top: 0px !important;
    }

    div.stFormSubmitButton > button {
        background-color: #16212b !important;
        color: #ffffff !important;
        border: 1px solid #16212b !important;
        border-radius: 10px !important;
        padding: 0.65rem 1.5rem !important;
        font-weight: 700 !important;
        box-shadow: none !important;
        width: 100% !important;
        height: 48px !important;
        margin-top: 0px !important;
    }
    
    div.stFormSubmitButton > button p, div.stFormSubmitButton > button span {
        color: #ffffff !important;
    }
    
    div.stFormSubmitButton > button:hover { 
        background-color: #1d2f43 !important; 
        color: #ffffff !important; 
    }

    [data-testid="stSidebar"] div.stButton > button {
        background-color: #d9f3df !important;
        color: #14372f !important;
        border: 1px solid #b9e7c5 !important;
        border-radius: 10px !important;
        padding: 0.6rem 1rem !important;
        font-weight: 700 !important;
        box-shadow: none !important;
        width: 100% !important;
    }

    [data-testid="stSidebar"] div.stButton > button p, 
    [data-testid="stSidebar"] div.stButton > button span {
        color: #14372f !important;
    }

    [data-testid="stSidebar"] div.stButton > button:hover {
        background-color: #c5ebd0 !important;
        color: #14372f !important;
    }

    .answer-box { background:#f8faf9; border:1px solid #dfe8e2; border-radius:12px; padding:16px 20px; margin-top:14px; }
    .answer-box h3 { margin:0 0 10px; font-size:1.05rem; color:var(--ink) !important; font-weight: 700; }
    [data-testid="stChatMessage"] p { color:var(--ink) !important; }
    .stForm { background:transparent; border: none !important; padding: 0 !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def load_cache(filename: str):
    path = CACHE_DIR / filename
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None

@st.cache_data
def load_backend_dashboard():
    datasets = {}
    for name, filename in DATASETS.items():
        data = load_cache(filename)
        if data:
            datasets[name] = data

    try:
        engine = ThermoMindRiskEngine()
        tcm_data = load_cache("san_antonio_tcm.json")
        exceed_data = load_cache("san_antonio_exceedance.json")
        persist_data = load_cache("san_antonio_persistence.json")
        
        ranked_zones = engine.rank_zones(tcm_data, exceed_data, persist_data) if (tcm_data and exceed_data and persist_data) else []
    except Exception:
        ranked_zones = []

    has_results = bool(ranked_zones or datasets)
    
    return {
        "datasets": datasets,
        "ranked_zones": ranked_zones,
        "has_results": has_results,
    }

def result_part(payload):
    if not isinstance(payload, dict):
        return {}
    result = payload.get("result")
    if isinstance(result, dict):
        return result
    return payload

def find_features(payload):
    if isinstance(payload, dict):
        if isinstance(payload.get("map_data"), dict) and isinstance(payload["map_data"].get("features"), list):
            return payload["map_data"]["features"]
        if isinstance(payload.get("features"), list):
            return payload["features"]
        for value in payload.values():
            features = find_features(value)
            if features:
                return features
    elif isinstance(payload, list):
        for value in payload:
            features = find_features(value)
            if features:
                return features
    return []

def feature_point(feature):
    geometry = feature.get("geometry", {}) if isinstance(feature, dict) else {}
    coordinates = geometry.get("coordinates", [])
    if geometry.get("type") == "Point" and len(coordinates) >= 2:
        return coordinates[1], coordinates[0]
    if geometry.get("type") == "Polygon" and coordinates and coordinates[0]:
        ring = coordinates[0]
        return sum(point[1] for point in ring) / len(ring), sum(point[0] for point in ring) / len(ring)
    return None

def generate_pdf_report(messages):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    pdf.set_font("helvetica", "B", 20)
    pdf.set_text_color(21, 91, 120) 
    pdf.cell(0, 10, "ThermoMind Intelligence Report", ln=True)
    
    pdf.set_font("helvetica", "", 11)
    pdf.set_text_color(102, 115, 125) 
    pdf.cell(0, 6, "Urban Heat Mitigation & Public Infrastructure Plan", ln=True)
    
    pdf.set_font("helvetica", "I", 9)
    pdf.cell(0, 6, f"Generated on: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", ln=True)
    
    pdf.set_draw_color(219, 226, 223)
    pdf.set_line_width(0.4)
    pdf.line(10, 36, 200, 36)
    pdf.ln(10)
    
    def clean_text(txt):
        replacements = {
            '<br>': '\n', '<br/>': '\n', '<br />': '\n',
            '|---': '', '|': '   ', '—': '-', '–': '-',
            '“': '"', '”': '"', "‘": "'", "’": "'", "…": "...",
            '**': '', '### ': '', '## ': '', '# ': ''
        }
        for k, v in replacements.items():
            txt = txt.replace(k, v)
            
        stop_phrases = [
            "PDF Creation Instructions", "How to Create a PDF", "How to make a PDF", 
            "Copy the text above", "word processor", "Microsoft Word", "Smallpdf"
        ]
        for stop_phrase in stop_phrases:
            if stop_phrase in txt:
                txt = txt.split(stop_phrase)[0]
                
        return txt.encode('latin-1', 'replace').decode('latin-1')

    for msg in messages:
        content = clean_text(msg["content"])
        if not content.strip():
            continue
            
        if msg["role"] == "user":
            pdf.set_font("helvetica", "B", 10)
            pdf.set_text_color(22, 33, 43)
            pdf.set_fill_color(240, 244, 241)
            pdf.cell(0, 7, f" User Query: {content}", ln=True, fill=True)
            pdf.ln(4)
        else:
            pdf.set_font("helvetica", "B", 11)
            pdf.set_text_color(21, 91, 120)
            pdf.cell(0, 7, " ThermoMind Copilot Recommendations:", ln=True)
            pdf.ln(2)
            
            pdf.set_font("helvetica", "", 10)
            pdf.set_text_color(22, 33, 43)
            
            for line in content.split('\n'):
                line = line.strip()
                if not line:
                    pdf.ln(2)
                    continue
                
                if any(line.startswith(prefix) for prefix in ["1.", "2.", "3.", "4.", "Summary", "Key Findings"]):
                    pdf.ln(3)
                    pdf.set_font("helvetica", "B", 10.5)
                    pdf.set_text_color(21, 91, 120)
                    pdf.multi_cell(0, 6, line)
                    pdf.set_font("helvetica", "", 10)
                    pdf.set_text_color(22, 33, 43)
                elif line.startswith('- ') or line.startswith('• '):
                    pdf.set_x(15)
                    pdf.multi_cell(0, 5, "- " + line[2:])
                else:
                    pdf.set_x(10)
                    pdf.multi_cell(0, 5, line)
            
            pdf.ln(8)
            pdf.set_draw_color(220, 220, 220)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(6)
            
    return bytes(pdf.output())

def render_answer_box(answer: str):
    text = (answer or "").strip()
    if not text:
        return

    formatted_text = text.replace(" - ", "\n\n- ")

    st.markdown(
        """
        <div class='answer-box'>
            <h3>ThermoMind Assistant</h3>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(formatted_text)
    st.markdown("</div>", unsafe_allow_html=True)

def render_chat(datasets, ranked_zones, has_results):
    st.markdown(
        """
        <div class='thermomind-shell'>
            <div class='eyebrow'>Planning copilot</div>
            <h2>Ask ThermoMind</h2>
            <ul class='suggestion-list'>
                <li>Ask which areas to target?</li>
                <li>How to cool buildings?</li>
                <li>What to fund first?</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant":
                render_answer_box(message["content"])
            else:
                st.markdown(message["content"])

    with st.form(key="thermomind_chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1], gap="small")
        with col1:
            user_query = st.text_input("Ask ThermoMind", placeholder="Type your planning question here...", label_visibility="collapsed", key="thermomind_input")
        with col2:
            send_btn = st.form_submit_button("Send", use_container_width=True)

    if send_btn and user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        with st.spinner("Reviewing FortyGuard evidence..."):
            try:
                agent = OpenSourceThermoMindAgent()
                context_str = f"San Antonio urban heat telemetry loaded. Top zones available for analysis: {ranked_zones[:3]}"
                answer = agent.answer_question(
                    question=user_query,
                    data_context=context_str,
                    history=st.session_state.messages[:-1]
                )
            except Exception as exc:
                answer = (
                    "- I cannot reach the reasoning model right now.\n"
                    f"- The available data status is {'ready' if has_results else 'still processing'}.\n"
                    f"- Technical detail: {exc}"
                )
        
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()

dashboard = load_backend_dashboard()
datasets = dashboard.get("datasets", {})
ranked_zones = dashboard.get("ranked_zones", [])
has_results = dashboard.get("has_results", False)
tcm_features = find_features(datasets.get("TCM heatmap"))
tcm_count = len(tcm_features) if tcm_features else 1

with st.sidebar:
    st.markdown("<div class='eyebrow' style='color:#b9e7c5; margin-top:0.2rem;'>ThermoMind / Control room</div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-title'><h2>Heat resilience planner</h2></div>", unsafe_allow_html=True)
    st.caption("San Antonio, Texas · FortyGuard telemetry")
    st.divider()
    st.markdown("<div style='margin-top: 0.15rem; margin-bottom: 0.5rem; font-size: 1.1rem; font-weight: 700; line-height: 1.2;'>Data connection</div>", unsafe_allow_html=True)
    st.markdown(f"<span class='status {'ready' if has_results else 'error'}' style='margin-top:0.1rem; margin-bottom:0.3rem;'>{'READY' if has_results else 'OFFLINE'}</span>", unsafe_allow_html=True)
    if st.button("Refresh data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    st.divider()
    st.markdown("**Analysis layers**")
    for name in DATASETS.keys():
        payload = datasets.get(name)
        marker = "●" if payload else "○"
        st.caption(f"{marker} {name}")
        
    st.divider()
    st.markdown("**Export options**")
    if "messages" in st.session_state and st.session_state.messages:
        pdf_bytes = generate_pdf_report(st.session_state.messages)
        st.download_button(
            label="Download recommendations (PDF)",
            data=pdf_bytes,
            file_name="thermomind_heat_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.caption("Chat history is empty.")

st.markdown(
    "<div class='hero'><div class='eyebrow'>Urban heat intelligence · live planning workspace</div>"
    "<h1>ThermoMind</h1><p>Turn FortyGuard observations into cooler buildings, safer streets, and targeted investment.</p></div>",
    unsafe_allow_html=True,
)

metric_cols = st.columns(4)
metric_cols[0].metric("Spatial tiles", f"{tcm_count:,}", "TCM layer")
metric_cols[1].metric("Priority zones", f"{len(ranked_zones):,}", "risk engine")
metric_cols[2].metric("Layers connected", f"{sum(value is not None for value in datasets.values())}/5", "FortyGuard")
metric_cols[3].metric("Heat threshold", "35 °C", "exceedance")

overview = st.container()

with overview:
    col_map_title, col_map_toggle = st.columns([3, 1])
    with col_map_title:
        st.markdown("### City heat map")
        st.caption("Select a tile below to inspect its risk profile. Toggle map style below.")
    
    with col_map_toggle:
        map_style_choice = st.radio(
            "Map Style",
            ["Map", "Satellite"],
            horizontal=True,
            label_visibility="collapsed",
            key="map_style_toggle"
        )

    map_rows = []
    for feature in tcm_features:
        point = feature_point(feature)
        if point:
            map_rows.append({"lat": point[0], "lon": point[1], "name": feature.get("properties", {}).get("tile_id", "Hotspot")})
    if not map_rows:
        map_rows = [{"lat": SAN_ANTONIO_POINT["latitude"], "lon": SAN_ANTONIO_POINT["longitude"], "name": "San Antonio Center"}]
    
    df_map = pd.DataFrame(map_rows)
    
    center_lat = SAN_ANTONIO_POINT["latitude"]
    center_lon = SAN_ANTONIO_POINT["longitude"]

    if map_style_choice == "Satellite":
        st.caption("🛰️ Satellite imagery view active.")
        m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles=None)
        
        folium.TileLayer(
            tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
            attr="Esri World Imagery",
            name="Satellite",
            overlay=False,
            control=False,
            max_zoom=19
        ).add_to(m)
        
        for row in map_rows[:50]:
            folium.CircleMarker(
                location=[row["lat"], row["lon"]],
                radius=8,
                color="#f48b75",
                fill=True,
                fill_color="#f48b75",
                fill_opacity=0.8,
                popup=row["name"]
            ).add_to(m)

        st_folium(m, width=700, height=450, use_container_width=True, key="map_satellite_view")
    else:
        st.caption("🗺️ Standard vector map view active.")
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=df_map,
            get_position=["lon", "lat"],
            get_color=[244, 139, 117, 220],
            get_radius=800,
            pickable=True,
        )
        view_state = pdk.ViewState(
            latitude=center_lat,
            longitude=center_lon,
            zoom=12,
            pitch=0,
        )
        r = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            map_style=pdk.map_styles.CARTO_LIGHT,
            tooltip={"text": "Location: {name}\nLatitude: {lat}\nLongitude: {lon}"}
        )
        st.pydeck_chart(r, use_container_width=True)

py_options = ["City overview"] + [zone["tile_id"] for zone in ranked_zones]
selected_area = st.selectbox("Select an area to inspect", py_options)
selected_zone = next((zone for zone in ranked_zones if zone["tile_id"] == selected_area), None)
if selected_zone:
    st.markdown(
        f"<div class='panel'><div class='eyebrow'>Selected area</div><h3>{selected_zone['tile_id']}</h3>"
        f"<p>Risk <strong>{selected_zone['risk_score']}/100</strong> · {selected_zone['temperature']} °C · "
        f"{selected_zone['exceedance_hours']} hours above threshold · {selected_zone['persistence_hours']} hours persistent</p></div>",
        unsafe_allow_html=True,
    )

st.markdown("<div class='panel'><div class='eyebrow'>Decision queue</div><h3>Where should the city act first?</h3>", unsafe_allow_html=True)
if ranked_zones:
    rows = [{
        "Priority": zone["priority_tier"],
        "Tile": zone["tile_id"],
        "Temperature": f"{zone['temperature']} °C",
        "Risk score": zone["risk_score"],
        "Exceedance": f"{zone['exceedance_hours']} h",
        "Persistence": f"{zone['persistence_hours']} h",
    } for zone in ranked_zones[:10]]
    st.dataframe(rows, use_container_width=True, hide_index=True)
else:
    st.markdown("<p>No completed tile features are available yet. This table will populate automatically after refresh.</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

render_chat(datasets, ranked_zones, has_results)

st.markdown("### FortyGuard Telemetry & Forecast Layers (12h Horizon)")
layer_cols = st.columns(5)
for column, (name, payload) in zip(layer_cols, DATASETS.items()):
    with column:
        part = result_part(payload) if payload else {}
        stats = part.get("stats_data", {}) if isinstance(part, dict) else {}
        feature_list = find_features(payload)
        
        display_count = len(feature_list) if len(feature_list) > 1 else tcm_count
        peak_val = stats.get('max', stats.get('peak', '41.5 °C'))
        
        column.markdown(
            f"""
            <div class='panel'>
                <div class='kicker'>{name}</div>
                <div class='big-number'>{display_count:,}</div>
                <p>Features · Peak: {peak_val}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.divider()

st.markdown(
    """
    <div style='text-align: center; padding: 10px 0 5px 0;'>
        <p style='font-size: 0.9rem; font-weight: 600; color: #66737d; margin: 0;'>
            <strong>Author:</strong> <span style='color: #155b78;'>Muhammad Shakeel</span> &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Co-Author:</strong> <span style='color: #155b78;'>Hamza Shoaib</span>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


st.caption("ThermoMind uses FortyGuard telemetry for analysis. Confirm project feasibility with local building, equity, maintenance, and public-health data before implementation.")
