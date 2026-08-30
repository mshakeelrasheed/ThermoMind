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

**[Launch ThermoMind](https://thermomind.streamlit.app)**

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

# 🎯 The Problem

Urban heat is not evenly distributed across a city.

Two neighborhoods can experience significantly different thermal conditions because of differences in:

- Built-up surfaces
- Roads and pavement
- Vegetation
- Land cover
- Exposure duration
- Local environmental conditions

However, raw temperature data alone does not answer the most important planning questions:

- Where is the highest-priority heat risk?
- Which areas experience prolonged heat exposure?
- Which zones should receive intervention first?
- What type of intervention could be appropriate?
- How can complex climate telemetry be communicated to planners and decision-makers?

Traditional climate datasets can also be difficult for non-technical users to interpret and convert into actionable decisions.

---

# 💡 Our Solution

**ThermoMind converts complex urban heat telemetry into an actionable decision-support workflow.**

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
