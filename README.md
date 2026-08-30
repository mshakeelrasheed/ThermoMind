```markdown
<div align="center">

# 🌡️ ThermoMind

### Urban Heat Intelligence & Resilience Planning Platform

An advanced AI-powered urban heat intelligence application that transforms multi-layered climate telemetry from the **FortyGuard API** into actionable mitigation strategies, interactive geospatial risk maps, and automated infrastructure planning reports.

<p>

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-ff4b4b?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70b-orange?style=for-the-badge)
![FortyGuard](https://img.shields.io/badge/FortyGuard-Climate_Telemetry-success?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

### 🚀 Live Demo

**🚀 Live Demo:** [Explore the ThermoMind Streamlit Cloud App](https://thermomind.streamlit.app)

</div>

---

# 📑 Table of Contents

- Overview
- Problem Statement & Who It Is For
- Why San Antonio, Texas?
- Key Features
- Dashboard Preview
- System Architecture
- Model Workflow & Risk Engine
- Technology Stack
- Repository Structure
- Installation & Local Setup
- Challenges Faced
- Authors
- License

---

# 📖 Overview

**ThermoMind** is an intelligent urban climate resilience platform designed to combat the growing crisis of urban heat islands (UHIs). By integrating real-time and forecast telemetry from the **FortyGuard API**, the platform evaluates high-resolution thermal comfort models, temperature exceedances, and persistence metrics. 

It equips city planners, municipal infrastructure developers, public health officials, and ordinary citizens with the data-driven insights needed to lower ambient temperatures, design cooler buildings, and protect vulnerable communities.

---

# 🎯 Problem Statement & Who It Is For

### The Problem
Extreme urban heat waves lead to public health crises, heightened energy consumption, and infrastructure strain. Traditional climate data is often fragmented, overly complex, and difficult for city planners or community leaders to translate into immediate, targeted cooling actions.

### Who It Is For
- **City Planners & Municipal Officials:** To optimize the placement of green infrastructure, urban shade covers, and cool-pavement retrofits.
- **Infrastructure Developers & Architects:** To design heat-resilient buildings and assess microclimate stress across urban corridors.
- **Public Health Officials:** To identify high-risk heat zones and deploy early interventions or cooling centers for vulnerable populations.
- **Common Citizens & Local Communities:** To understand neighborhood-level heat risk, plan safe daily activities during severe heat advisories, and advocate for local climate resilience.

---

# 🌆 Why San Antonio, Texas?

The platform utilizes data centered around **San Antonio, Texas** because it represents a rapidly growing metropolitan area heavily impacted by severe southern heat waves, sprawling urban infrastructure, and distinct microclimate variations. Using a 12-hour forecast horizon over San Antonio's geographic grid allows ThermoMind to stress-test multi-layered climate algorithms under realistic, high-temperature urban conditions.

---

# ✨ Features

- 🔹 **Multi-Layer Telemetry Integration:** Connects distinct FortyGuard data feeds (TCM Heatmap, Exceedance, Persistence, Environment, and Satellite imagery layers).
- 🔹 **Interactive Geospatial Workspaces:** Seamlessly toggle between standard vector maps and high-resolution Esri World Imagery satellite views.
- 🔹 **Weighted Risk-Scoring Engine:** Dynamically analyzes spatial grid cells using a composite formula blending temperature peaks, exceedance hours, and persistence metrics.
- 🔹 **AI Planning Copilot:** Powered by Llama 3.3 (via Groq API) to answer complex urban planning and mitigation queries in real time.
- 🔹 **Automated PDF Reporting:** Generates professional, downloadable intelligence summary reports directly from chat history.

---

# 📸 Dashboard Preview

<p align="center">
<img src="screenshots/dashboard.png" width="900">
</p>

---

# 🏗️ System Architecture

```text
FortyGuard API Telemetry (San Antonio)
                  │
                  ▼
         Data Caching Layer
                  │
                  ▼
     ThermoMind Risk-Scoring Engine
   (Temperature + Exceedance + Persistence)
                  │
                  ├──────────────────────────────┐
                  ▼                              ▼
     Interactive Geospatial Map         Llama 3.3 AI Copilot
     (Vector PyDeck / Satellite)         (Contextual Reasoning)
                  │                              │
                  └──────────────┬───────────────┘
                                 ▼
                     Streamlit Cloud Dashboard
                  (PDF Report Export & Live UI)

```

---

# 🧠 Model Workflow & Risk Engine

```text
FortyGuard API Endpoints
           │
           ▼
  JSON Payload Parsing
           │
           ▼
ThermoMindRiskEngine.rank_zones()
           │
           ▼
Normalization & Weighted Formula:
 Score = (Temp * 0.40) + (Exceed * 0.35) + (Persist * 0.25)
           │
           ▼
Priority Tier Categorization (Critical, High, Moderate, Low)
           │
           ▼
Interactive Table & Llama 3.3 Context Injection

```

---

# 🛠 Technology Stack

| Category | Technologies |
| --- | --- |
| Programming Language | Python 3.10 |
| Web Framework | Streamlit |
| Geospatial Mapping | PyDeck, Folium, Streamlit-Folium |
| Data Processing | Pandas, NumPy, Pathlib |
| AI / LLM Integration | Groq API (Llama-3.3-70b-versatile) |
| Report Generation | FPDF |
| Deployment | Streamlit Cloud & Docker |
| Version Control | Git & GitHub |

---

# 📂 Repository Structure

```text
ThermoMind/
│
├── fortyguard/             # FortyGuard API client modules and core integrations
├── scripts/                # Data fetching, test automation, and utility scripts
├── tests/                  # Unit tests for risk engine and backend modules
├── thermomind/
│   └── cache/              # Cached JSON telemetry payloads for San Antonio
│       ├── san_antonio_tcm.json
│       ├── san_antonio_exceedance.json
│       ├── san_antonio_persistence.json
│       ├── san_antonio_env_params.json
│       └── san_antonio_satellite.json
│
├── agent.py                # Llama-3 AI planning copilot integration
├── app.py                  # Main Streamlit Cloud dashboard application
├── backend.py              # Core data loading and API routing handlers
├── client.py               # FortyGuard API request wrapper
├── main.py                 # Application execution entry point
├── risk_engine.py          # Composite risk-scoring engine
├── run_local.py            # Local execution helper script
├── run_san_antonio.py      # Telemetry pipeline runner for San Antonio
├── samples.py              # Geographic coordinates and sample boundaries
├── requirements.txt        # Project python dependencies
├── Dockerfile              # Container configuration
├── LICENSE                 # MIT License file
└── README.md               # Project documentation

```

---

# ⚙️ Installation & Local Setup

### Clone the repository

```bash
git clone [https://github.com/mshakeelrasheed/ThermoMind.git](https://github.com/mshakeelrasheed/ThermoMind.git)

```

### Navigate to the project directory

```bash
cd ThermoMind

```

### Install dependencies

```bash
pip install -r requirements.txt

```

### Set up your environment variables

Create a `.streamlit/secrets.toml` file or configure your environment variables:

```toml
FORTYGUARD_API_KEY = "your_fortyguard_api_key"
FORTYGUARD_BASE_URL = "[https://api.fortyguard.com](https://api.fortyguard.com)"
OPEN_SOURCE_BASE_URL = "[https://api.groq.com/openai/v1](https://api.groq.com/openai/v1)"
OPEN_SOURCE_API_KEY = "your_groq_api_key"
OPEN_SOURCE_MODEL = "llama-3.3-70b-versatile"

```

### Run the application

```bash
streamlit run app.py

```

---

# ⚠️ Challenges Faced

During the development of ThermoMind, the team encountered and successfully resolved several technical hurdles:

* **API Latency & Rate Limits:** Managing multiple asynchronous FortyGuard telemetry feeds and structuring a robust caching layer under `thermomind/cache/` to ensure lightning-fast dashboard load times.
* **Cloud Compatibility:** Transitioning from a local FastAPI backend architecture (`127.0.0.1:8001`) to a self-contained Streamlit application that reads directly from local cache files for seamless cloud deployment.
* **Geospatial Rendering Performance:** Optimizing PyDeck and Folium layers to handle urban spatial tiles smoothly without browser lag.
* **AI Agent Context Alignment:** Tuning prompt templates and exception handling so the Llama-3 planning copilot reliably references live dashboard metrics and tile structures during user queries.

---

# 👨‍💻 Authors & Contributors

## Muhammad Shakeel Rasheed

* **Role:** Lead Developer & AI Engineer
* **Affiliation:** BS Artificial Intelligence, The Islamia University Bahawalpur
* **GitHub:** [mshakeelrasheed](https://github.com/mshakeelrasheed)

## Hamza Shoaib

* **Role:** Co-Author & Systems Architect
* **Affiliation:** AI & Infrastructure Collaborator

---

# 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute this software in accordance with the license terms.

---

## ⭐ If you found ThermoMind useful, consider giving it a Star!

Thank you for visiting this repository.
