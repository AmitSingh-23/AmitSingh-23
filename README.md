<img src="./header.svg" width="100%" alt="Terminal: Amit Singh Bisht, Electrical Engineering at NIT Raipur. Interests: backend systems, databases, applied ML, competitive programming.">

## Amit Singh Bisht

Electrical Engineering undergraduate at **NIT Raipur** (batch of 2028) who builds backend systems. I work mostly with Python, Node.js and PostgreSQL, solve DSA problems in C++, and like projects where software has to deal with something real: a slow database, a queue of heavy jobs, or a sensor on a machine.

**Looking for:** SDE internships, backend-focused.

## Stack

<p>
  <img src="https://skillicons.dev/icons?i=cpp,python,js,nodejs,express,fastapi,react&perline=7" alt="C++, Python, JavaScript, Node.js, Express, FastAPI, React">
  <br>
  <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,docker,git,githubactions,postman&perline=7" alt="PostgreSQL, MongoDB, Redis, Docker, Git, GitHub Actions, Postman">
</p>

Also used in projects: PyTorch Geometric, LangGraph, BullMQ, ESP32 (Arduino).

## Featured projects

### [QuerySentinel](https://github.com/AmitSingh-23/query-sentinel)

**Diagnosing slow PostgreSQL queries with AI usually means sending your schema and data to a third party. This doesn't.**

<a href="https://github.com/AmitSingh-23/query-sentinel"><img src="https://raw.githubusercontent.com/AmitSingh-23/query-sentinel/main/db-opt-platform/docs/screenshots/pipeline_run.png" width="100%" alt="QuerySentinel dashboard showing a pipeline run"></a>

- **What it does:** masks every literal and table or column name in a query, reads the `EXPLAIN` plan, proposes indexes and rewrites, and tests each index with HypoPG before producing a migration script with a rollback.
- **My work:** Finalist at Code Utsava X.0. I built the masking gateway, the plan analysis (a small GNN with a rule-based fallback), the HypoPG test harness and the FastAPI and Streamlit layers.
- **Worth a look:** on a 1M-row demo dataset, one correlated-subquery fix cut the planner's cost estimate by 99.98 %, and a cast-on-indexed-column fix took a measured query from 44.3 ms to 0.009 ms. 211 offline tests; limitations are documented, including that the GNN is trained on synthetic plans.
- **Stack:** Python, FastAPI, PostgreSQL 16, HypoPG, pglast, LangGraph, PyTorch Geometric, Docker

### [EventSnap](https://github.com/AmitSingh-23/EventSnap)

**After an event, guests want their own photos, not a folder of two thousand.**

- **What it does:** a photographer uploads the whole set; faces are detected in a background worker and grouped per person, and each person gets a gallery link and a ZIP download.
- **My work:** Express API, BullMQ and Redis job queue so uploads never block on face detection, DBSCAN clustering over face embeddings (no need to know how many people attended), and the React dashboard.
- **Worth a look:** the clustering logic is isolated and unit-tested, uploads are type- and size-limited and rate-limited, and the README states plainly what is missing before it could handle real biometric data.
- **Stack:** Node.js, Express, MongoDB, Redis, BullMQ, face-api.js, Cloudinary, React

### [IRONside](https://github.com/AmitSingh-23/Ironside-Sih)

**Machines usually show signs before they fail. This puts those signs on one screen.**

<a href="https://github.com/AmitSingh-23/Ironside-Sih"><img src="https://raw.githubusercontent.com/AmitSingh-23/Ironside-Sih/main/docs/screenshots/command-center.webp" width="100%" alt="IRONside asset command center"></a>

- **What it does:** ESP32 firmware reads vibration, temperature, current, voltage and RPM sensors and posts them to an API, which compares readings with each machine's baseline and raises alerts. A dashboard shows fleet health, live charts and 3D machine models.
- **My work:** team project, Top 50 in NIT Raipur's internal Smart India Hackathon round. I built the Express API and the React dashboard.
- **Worth a look:** hardware and software in one repo, with the sensor wiring documented. Detection is threshold-based, the dashboard runs on a demo dataset, and storage is in memory; the README says so.
- **Stack:** ESP32 (Arduino), Node.js, Express, React, Three.js, Recharts

## Problem solving

<p>
  <a href="https://leetcode.com/Amit_Singh_Bisht49"><img src="https://leetcard.jacoblin.cool/Amit_Singh_Bisht49?theme=dark&font=Karla" height="180" alt="LeetCode statistics for Amit_Singh_Bisht49"></a>
  <img src="https://streak-stats.demolab.com?user=AmitSingh-23&theme=github-dark-blue&hide_border=true" height="180" alt="GitHub contribution streak for AmitSingh-23">
</p>

[LeetCode](https://leetcode.com/Amit_Singh_Bisht49) · [Codeforces](https://codeforces.com/profile/amit.singh.b049) · [CodeChef](https://www.codechef.com/users/amit_singh_b70) · [Solutions with a topic-wise index](https://github.com/AmitSingh-23/LeetCode)

## Electrical engineering

Industrial training at SJVN's 1500 MW Nathpa Jhakri Hydro Power Station (2026): synchronous generators, 400 kV gas-insulated switchgear, SCADA-based plant control and relay protection.

## Contact

[LinkedIn](https://www.linkedin.com/in/amit-singh-bisht-nitrr) · [LeetCode](https://leetcode.com/Amit_Singh_Bisht49) · [Codeforces](https://codeforces.com/profile/amit.singh.b049) · [CodeChef](https://www.codechef.com/users/amit_singh_b70)
