<a href="https://www.linkedin.com/in/amit-singh-bisht-nitrr">
  <img src="./header.svg" width="100%" alt="Amit Singh Bisht: Electrical Engineering at NIT Raipur, backend systems and applied AI">
</a>

Electrical Engineering undergraduate at **NIT Raipur** (2024–2028) who builds backend systems and full-stack applications. I like problems where the hard part is making something trustworthy: safe to run, honest about its limits, and explainable.

- Currently building **EventSnap**, an event photo sorter that groups pictures by face
- Looking for **software engineering internships** (backend, data, applied AI)
- Regular problem solving in **C++** on LeetCode, Codeforces and CodeChef

## Selected projects

Click a project to open it.

<details open>
<summary><b>QuerySentinel</b>: privacy-aware AI PostgreSQL optimizer · Finalist, Code Utsava X.0</summary>
<br>

Explains why a PostgreSQL query is slow and proposes indexes and rewrites, without exposing customer data to an AI model.

- Every literal and schema name is masked (pglast AST + HMAC-SHA256) before any AI step
- LangGraph agents, a GNN over `EXPLAIN` plan trees and Q-learning propose and rank fixes
- Each fix is tested with HypoPG hypothetical indexes, then exported as migration + rollback scripts for human review

**Stack:** Python, FastAPI, PostgreSQL, HypoPG, LangGraph, PyTorch Geometric, Streamlit, Docker  
**Code:** [AmitSingh-23/query-sentinel](https://github.com/AmitSingh-23/query-sentinel)
</details>

<details>
<summary><b>EventSnap</b>: AI event photo sorting and sharing</summary>
<br>

Turns a photographer's bulk upload into per-person galleries with direct share links. No sign-up or selfie needed.

- Face detection runs in a separate BullMQ + Redis worker, so uploads never block the API
- 128-d face embeddings are clustered with DBSCAN, so the number of people never has to be known up front
- Per-person ZIP downloads are streamed on the fly

**Stack:** Node.js, Express, React, MongoDB, Redis, BullMQ, face-api.js, Cloudinary  
**Code:** [AmitSingh-23/FaceFrame](https://github.com/AmitSingh-23/FaceFrame)
</details>

<details>
<summary><b>IRONside</b>: industrial asset health dashboard · Top 50, SIH internal round at NIT Raipur</summary>
<br>

Predictive-maintenance dashboard prototype, built as a team project.

- ESP32 firmware reads vibration, current, temperature and RPM sensors
- Express API ingests telemetry, compares it with each machine's baseline and raises alerts
- React dashboard with live charts and interactive 3D machine models

**Stack:** React, Three.js, Recharts, Node.js, Express, ESP32  
**Code:** [AmitSingh-23/Ironside-Sih](https://github.com/AmitSingh-23/Ironside-Sih)
</details>

## Toolbox

**Languages** C++, Python, JavaScript  
**Backend** Node.js, Express, FastAPI, REST APIs, BullMQ, Redis  
**Data** PostgreSQL, MongoDB  
**AI/ML** PyTorch, PyTorch Geometric, LangGraph  
**Tools** Git, Docker, Postman

## Electrical engineering side

Industrial training at SJVN's 1500 MW Nathpa Jhakri Hydro Power Station (2026): synchronous generators, 400 kV GIS, SCADA-based plant control and relay protection.

## Find me

[LinkedIn](https://www.linkedin.com/in/amit-singh-bisht-nitrr) · [LeetCode](https://leetcode.com/Amit_Singh_Bisht49) · [DSA solutions](https://github.com/AmitSingh-23/LeetCode)
