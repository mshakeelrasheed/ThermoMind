<div align="center">

# 🌡️ ThermoMind

### AI-Powered Urban Heat Intelligence & Resilience Planning

**Turning hyperlocal temperature intelligence into actionable urban heat interventions.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-ff4b4b?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-orange?style=for-the-badge)](https://groq.com/)
[![FortyGuard](https://img.shields.io/badge/FortyGuard-Temperature_API-success?style=for-the-badge)](https://www.fortyguard.com/)
[![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br>

### 🚀 Live Demo

**[Launch ThermoMind](https://thermomind-ai.streamlit.app/)**

</div>

---

# 📌 Overview

**ThermoMind** is an AI-powered urban heat intelligence platform built for the **FortyGuard Hackathon '26**.

The platform transforms hyperlocal urban temperature and environmental intelligence from the **FortyGuard Temperature API** into understandable risk assessments, interactive geospatial visualizations, priority zones, and AI-assisted mitigation recommendations.

Instead of simply showing users where temperatures are high, ThermoMind focuses on a more practical question:

> **Which areas should be prioritized for intervention, and what should be done there?**

ThermoMind combines:

- 🌡️ Hyperlocal temperature intelligence
- 🔥 Temperature exceedance analysis
- ⏱️ Heat persistence analysis
- 🌱 Environmental parameters
- 🛰️ Satellite-based spatial information
- 📊 Composite heat-risk scoring
- 🤖 AI-powered planning assistance
- 🗺️ Interactive geospatial visualization
- 📄 Automated intelligence reporting

The current implementation demonstrates the platform using **San Antonio, Texas** as the target urban area.

---

# 🎯 Problem Statement

Urban heat is not evenly distributed across a city.

Different neighborhoods can experience different thermal conditions because of variations in:

- Built-up surfaces
- Roads and pavement
- Vegetation
- Land cover
- Exposure duration
- Local environmental conditions

Raw temperature data alone does not answer important planning questions:

- Where is the highest-priority heat risk?
- Which areas experience prolonged heat exposure?
- Which zones should receive intervention first?
- What type of intervention could be appropriate?
- How can complex climate telemetry be communicated to planners and decision-makers?

ThermoMind addresses this gap by transforming complex temperature intelligence into an understandable and actionable decision-support workflow.

---

# 💡 Our Solution

ThermoMind combines FortyGuard's temperature intelligence with a quantitative risk engine and an AI planning copilot.

```text
FortyGuard Temperature API
            │
            ▼
     Urban Heat Telemetry
            │
            ▼
    Data Processing Layer
            │
            ▼
      Risk Scoring Engine
            │
     ┌──────┴──────┐
     ▼             ▼
Interactive Map   Risk Ranking
     │             │
     └──────┬──────┘
            ▼
       AI Planning
         Copilot
            │
            ▼
 Actionable Intervention
    Recommendations
````

The system evaluates multiple heat indicators instead of relying on temperature alone.

This allows ThermoMind to move from:

> **"This area is hot."**

to:

> **"This area has a high heat-risk priority because of its temperature, duration of exceedance, and persistence — and these interventions should be considered."**

---

# 🌆 Why San Antonio, Texas?

ThermoMind currently demonstrates its capabilities using **San Antonio, Texas**.

San Antonio provides a useful urban environment for demonstrating heat-intelligence workflows because of its metropolitan scale, urban development, and exposure to high-temperature conditions.

The application uses a defined geographic area around San Antonio and processes FortyGuard telemetry across spatial grid cells.

---

# ✨ Key Features

## 🌡️ 1. Hyperlocal Heat Intelligence

ThermoMind integrates the FortyGuard Temperature API to obtain spatial temperature intelligence across the selected urban area.

The platform works with temperature information at the grid-cell level rather than treating the entire city as having a single temperature value.

---

## 🔥 2. Heat Exceedance Analysis

ThermoMind evaluates how long individual areas remain above a defined temperature threshold.

This provides an additional heat-risk signal beyond a single temperature snapshot.

Example:

```text
Zone A → 2 hours above threshold
Zone B → 6 hours above threshold
Zone C → 9 hours above threshold
```

Areas experiencing longer periods above the threshold can therefore receive greater priority in the risk analysis.

---

## ⏱️ 3. Heat Persistence Analysis

ThermoMind analyzes the longest continuous period during which an area remains above the selected temperature threshold.

This helps distinguish between:

* Short-duration heat exposure
* Persistent heat exposure

---

## 📊 4. Composite Heat-Risk Scoring

ThermoMind combines multiple heat indicators into a single normalized priority score.

Current weighting:

```text
Risk Score =
    Temperature      × 0.40
  + Exceedance       × 0.35
  + Persistence      × 0.25
```

The resulting score is categorized into priority tiers:

```text
Critical
High
Moderate
Low
```

This creates a ranked view of urban heat-risk zones.

---

## 🗺️ 5. Interactive Geospatial Dashboard

The platform provides an interactive map for exploring urban heat conditions.

Users can examine:

* Heat distribution
* Risk zones
* Exceedance patterns
* Persistence patterns
* Geographic locations
* Satellite imagery

The dashboard uses **PyDeck**, **Folium**, and **Streamlit-Folium** for geospatial visualization.

---

## 🛰️ 6. Satellite Intelligence

Where available through the FortyGuard integration, satellite-based segmentation provides additional spatial context.

This allows heat-risk information to be considered alongside characteristics of the urban environment.

---

## 🌍 7. Environmental Parameters

ThermoMind incorporates environmental information such as:

* Apparent temperature
* Heat index
* Humidity
* Wet-bulb temperature
* Air-quality information
* Solar irradiance

These parameters provide additional context around heat exposure.

---

## 🤖 8. AI Planning Copilot

ThermoMind includes an AI-powered planning assistant using **Llama 3.3 70B through Groq**.

The AI Copilot receives relevant dashboard context and helps users interpret heat-risk results.

Example questions:

```text
Why is this area considered high risk?

Which zones should be prioritized?

What factors are contributing to this area's risk?

What type of heat mitigation strategy could be considered?

Summarize the most critical heat-risk zones.
```

The AI Copilot is designed to complement the quantitative risk engine by making the results easier to understand and translate into planning-oriented insights.

---

## 📄 9. Automated Reporting

ThermoMind can generate downloadable intelligence reports containing summarized findings and recommendations.

This converts dashboard analysis into a shareable planning artifact.

---

# 🧠 Risk Engine

ThermoMind uses a weighted composite scoring approach.

```text
                 FortyGuard Data
                       │
                       ▼
              JSON Data Processing
                       │
                       ▼
            Spatial Grid-Level Metrics
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Temperature     Exceedance     Persistence
      40%              35%             25%
        │              │               │
        └──────────────┼───────────────┘
                       ▼
               Normalized Score
                       │
                       ▼
              Priority Classification
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Critical       High      Moderate/Low
                       │
                       ▼
                 AI Copilot
                       │
                       ▼
              Actionable Insights
```

### Current Formula

```text
Score = (Temperature × 0.40)
      + (Exceedance × 0.35)
      + (Persistence × 0.25)
```

The weights prioritize temperature while also accounting for the duration and persistence of heat exposure.

---

# 🔌 FortyGuard Temperature API

ThermoMind is built around the **FortyGuard Temperature API**.

The project uses multiple FortyGuard capabilities:

| FortyGuard Capability    | ThermoMind Usage                                     |
| ------------------------ | ---------------------------------------------------- |
| Heatmap                  | Spatial temperature intelligence                     |
| Exceedance               | Hours above temperature threshold                    |
| Persistence              | Longest continuous heat exposure                     |
| Environmental Parameters | Environmental and thermal context                    |
| Satellite Segmentation   | Land-cover and spatial context                       |
| Heat Intelligence        | Advanced heat-intelligence reporting where available |

### API Workflow

Several FortyGuard analysis endpoints use asynchronous processing.

```text
ThermoMind
    │
    │ POST request
    ▼
FortyGuard API
    │
    │ activity_id
    ▼
Processing
    │
    │ polling
    ▼
Completed Result
    │
    ▼
ThermoMind Risk Engine
```

ThermoMind processes the returned telemetry before passing relevant metrics into the risk engine and AI Copilot.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   FortyGuard API     │
                    │                      │
                    │ • Heatmap            │
                    │ • Exceedance         │
                    │ • Persistence        │
                    │ • Environment        │
                    │ • Satellite          │
                    │ • Heat Intelligence  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Processing    │
                    │                      │
                    │ JSON parsing         │
                    │ Validation           │
                    │ Normalization        │
                    │ Caching              │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Risk Engine        │
                    │                      │
                    │ Temperature  40%      │
                    │ Exceedance   35%      │
                    │ Persistence  25%      │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
       ┌──────────────────┐       ┌──────────────────┐
       │ Geospatial       │       │ AI Planning      │
       │ Dashboard        │       │ Copilot          │
       │                  │       │                  │
       │ PyDeck/Folium    │       │ Llama 3.3 70B    │
       └────────┬─────────┘       └────────┬─────────┘
                │                          │
                └────────────┬─────────────┘
                             ▼
                   ┌──────────────────┐
                   │ Streamlit App    │
                   │                  │
                   │ Maps             │
                   │ Risk Rankings    │
                   │ AI Insights      │
                   │ Reports          │
                   └──────────────────┘
```


# 🛠️ Technology Stack

| Category                 | Technology                 |
| ------------------------ | -------------------------- |
| Programming Language     | Python 3.10+               |
| Web Framework            | Streamlit                  |
| AI / LLM                 | Llama 3.3 70B              |
| LLM Infrastructure       | Groq API                   |
| Climate Intelligence     | FortyGuard Temperature API |
| Data Processing          | Pandas, NumPy              |
| Geospatial Visualization | PyDeck                     |
| Interactive Maps         | Folium, Streamlit-Folium   |
| Report Generation        | FPDF                       |
| Containerization         | Docker                     |
| Deployment               | Streamlit Cloud            |
| Version Control          | Git & GitHub               |

---

# 📂 Repository Structure

```text
ThermoMind/
│
├── fortyguard/
│   ├── API client modules
│   └── FortyGuard integrations
│
├── scripts/
│   ├── Data fetching
│   ├── Testing utilities
│   └── Pipeline utilities
│
├── tests/
│   └── Unit tests
│
├── thermomind/
│   └── cache/
│       ├── san_antonio_tcm.json
│       ├── san_antonio_exceedance.json
│       ├── san_antonio_persistence.json
│       ├── san_antonio_env_params.json
│       └── san_antonio_satellite.json
│
├── agent.py
│   └── AI planning copilot
│
├── app.py
│   └── Main Streamlit dashboard
│
├── backend.py
│   └── Data loading and API routing
│
├── client.py
│   └── FortyGuard request wrapper
│
├── main.py
│   └── Application entry point
│
├── risk_engine.py
│   └── Composite heat-risk scoring
│
├── run_local.py
│   └── Local execution helper
│
├── run_san_antonio.py
│   └── San Antonio telemetry pipeline
│
├── samples.py
│   └── Sample geographic data
│
├── requirements.txt
│   └── Python dependencies
│
├── Dockerfile
│   └── Container configuration
│
├── LICENSE
│
└── README.md
```

---

# ⚙️ Local Installation

## 1. Clone the repository

```bash
git clone https://github.com/mshakeelrasheed/ThermoMind.git
cd ThermoMind
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

For local development, configure the required credentials through Streamlit secrets or environment variables.

Create:

```text
.streamlit/secrets.toml
```

Example:

```toml
FORTYGUARD_API_KEY = "your_fortyguard_api_key"
FORTYGUARD_BASE_URL = "https://api.fortyguard.com"

OPEN_SOURCE_BASE_URL = "https://api.groq.com/openai/v1"
OPEN_SOURCE_API_KEY = "your_groq_api_key"
OPEN_SOURCE_MODEL = "llama-3.3-70b-versatile"
```

### 🔐 Security

**Never commit real API keys, tokens, or secrets to GitHub.**

Make sure your secrets file is included in `.gitignore`.

---

# ▶️ Run ThermoMind

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at the local Streamlit URL displayed in your terminal.

---

# 🐳 Docker

ThermoMind includes a Docker configuration for containerized deployment.

Build the image:

```bash
docker build -t thermomind .
```

Run the container:

```bash
docker run -p 8501:8501 thermomind
```

---

# 📊 Example User Workflow

```text
1. Select / load the target urban area
              ↓
2. Retrieve FortyGuard temperature intelligence
              ↓
3. Analyze temperature, exceedance & persistence
              ↓
4. Calculate composite heat-risk scores
              ↓
5. Rank priority zones
              ↓
6. Explore heat-risk patterns on the map
              ↓
7. Ask the AI Planning Copilot
              ↓
8. Generate actionable insights
              ↓
9. Export an intelligence report
```

---

# 🎯 Intended Users

### 🏙️ City Planners

Identify areas where heat mitigation resources could be prioritized.

### 🏗️ Infrastructure Developers

Understand spatial heat exposure when considering urban infrastructure.

### 🌳 Urban Resilience Teams

Explore potential areas for interventions such as:

* Green infrastructure
* Urban shade
* Vegetation
* Cool-pavement strategies
* Heat-resilient planning

### 🏥 Public Health Teams

Identify areas experiencing elevated or persistent heat exposure that may warrant additional attention.

### 👥 Local Communities

Make complex urban heat information easier to understand through interactive visualizations and AI-assisted explanations.

---

# 💡 Why ThermoMind?

Many heat dashboards answer:

> **"How hot is this area?"**

ThermoMind aims to answer a more actionable question:

> **"Where should we focus first, why, and what intervention should we consider?"**

The platform therefore combines:

**Temperature → Exposure → Persistence → Risk → Priority → Action**

---

# ⚠️ Challenges & Engineering Decisions

## API Latency

Several FortyGuard analysis endpoints use asynchronous processing.

ThermoMind uses structured data handling and caching to avoid unnecessary repeated API calls and improve dashboard responsiveness.

## Geospatial Rendering

Rendering large numbers of spatial cells in a browser can create performance challenges.

The application uses PyDeck and optimized data structures for efficient spatial visualization.

## Cloud Deployment

The initial architecture relied on a local backend.

For deployment, the application was adapted into a self-contained Streamlit architecture that can operate using cached telemetry and application-level data handling.

## AI Context Alignment

The AI Copilot needs relevant dashboard context to provide useful responses.

Prompt construction and exception handling were designed to keep AI responses aligned with the available heat-risk metrics and spatial analysis.

---

# 🔮 Future Improvements

Potential future development includes:

* Population vulnerability indicators
* Additional urban datasets
* Real-time intervention monitoring
* Advanced spatial risk models
* Historical heat-risk trend analysis
* Additional cities and geographic regions
* Automated intervention cost estimation
* Municipal planning dataset integration
* Advanced AI-assisted scenario planning
* Multi-agent urban resilience workflows

---

# 👨‍💻 Contributors

## Muhammad Shakeel Rasheed
- **Lead Developer & AI Engineer**
- **Affiliation:** BS Artificial Intelligence, The Islamia University Bahawalpur
- **GitHub:** [@mshakeelrasheed](https://github.com/mshakeelrasheed)
- **LinkedIn:** [muhammad-shakeel-rasheed](https://www.linkedin.com/in/muhammad-shakeel-rasheed)
- **Hugging Face:** [@mshakeelrasheed](https://huggingface.co/mshakeelrasheed)
---

## Hamza Shoaib

** Systems Architect**

AI & Infrastructure Collaborator

GitHub: [@hamzxshoaib](https://github.com/hamxashoaib)

---

# 🏆 Hackathon

Built for:

## FortyGuard Hackathon '26

### Theme

**Building the World's Temperature AI**

ThermoMind explores how hyperlocal temperature intelligence can be transformed into practical urban heat resilience decisions using AI, geospatial analytics, and the FortyGuard Temperature API.

---

# 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

# 🙏 Acknowledgements

Special thanks to **FortyGuard** for providing access to its Temperature API and climate intelligence infrastructure for the hackathon.

---

<div align="center">

# 🌡️ ThermoMind

### From temperature data to actionable urban heat intelligence.

**Built with Python • Streamlit • FortyGuard • Llama 3.3 • Groq**

⭐ If you find ThermoMind useful, consider giving the repository a star.

</div>
```


