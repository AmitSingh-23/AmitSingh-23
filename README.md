<img src="./header.svg" width="100%" alt="Terminal animation: Amit Singh Bisht, Electrical Engineering at NIT Raipur">

### Hey, I'm Amit 👋

I'm an Electrical Engineering student at NIT Raipur (batch of 2028) who got hooked on software along the way. I like solving problems and building things. These days it's mostly backends, and anything that has a database behind it.

- 🔭 Right now I'm working on **EventSnap**, which sorts event photos by the people in them
- 🧩 I solve DSA problems in C++ on LeetCode, Codeforces and CodeChef
- ⚡ Did my industrial training at SJVN's 1500 MW Nathpa Jhakri hydro power station
- 💼 Looking for SDE internships

### Tech I use

<p>
  <img src="https://skillicons.dev/icons?i=cpp,python,js,nodejs,express,react,fastapi&perline=7" alt="C++, Python, JavaScript, Node.js, Express, React, FastAPI">
  <br>
  <img src="https://skillicons.dev/icons?i=postgres,mongodb,redis,pytorch,docker,git,postman&perline=7" alt="PostgreSQL, MongoDB, Redis, PyTorch, Docker, Git, Postman">
</p>

### Things I've built

<details open>
<summary><b>QuerySentinel</b> · PostgreSQL query optimizer that keeps your data private · Finalist, Code Utsava X.0</summary>
<br>

Tells you why a PostgreSQL query is slow and what to do about it. The part I cared about most: no real data or table names ever reach the AI model.

- Masks every literal and schema name before any AI step
- Reads `EXPLAIN` plans with a small GNN, then suggests indexes and rewrites
- Tests each suggestion with HypoPG before giving you a migration script

`Python` `FastAPI` `PostgreSQL` `HypoPG` `LangGraph` `PyTorch Geometric` `Docker`

[See the code →](https://github.com/AmitSingh-23/query-sentinel)
</details>

<details>
<summary><b>EventSnap</b> · upload event photos, get a gallery per person</summary>
<br>

A photographer uploads everything from an event, and each guest gets a link with just their photos. No sign-up, no selfie.

- Face detection runs in a background worker (BullMQ + Redis) so uploads stay fast
- Faces are grouped with DBSCAN, so it doesn't need to know how many people there are
- Each person's photos download as a ZIP

`Node.js` `Express` `React` `MongoDB` `Redis` `BullMQ` `face-api.js`

[See the code →](https://github.com/AmitSingh-23/EventSnap)
</details>

<details>
<summary><b>IRONside</b> · machine health dashboard · Top 50, SIH internal round at NIT Raipur</summary>
<br>

A team project for Smart India Hackathon: sensors on a machine, an ESP32 sending the readings, and a dashboard that flags when something looks off.

- ESP32 firmware for vibration, current, temperature and RPM sensors
- Express API that compares readings with each machine's baseline and raises alerts
- React dashboard with live charts and 3D machine models

`React` `Three.js` `Node.js` `Express` `ESP32`

[See the code →](https://github.com/AmitSingh-23/Ironside-Sih)
</details>

### GitHub activity

<p>
  <img src="https://streak-stats.demolab.com?user=AmitSingh-23&theme=github-dark-blue&hide_border=true" alt="GitHub streak stats">
</p>

### LeetCode

<p>
  <img src="https://leetcard.jacoblin.cool/Amit_Singh_Bisht49?theme=dark&font=Karla&ext=heatmap" alt="LeetCode stats">
</p>

### Say hi

<a href="https://www.linkedin.com/in/amit-singh-bisht-nitrr"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
<a href="https://leetcode.com/Amit_Singh_Bisht49"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"></a>
<a href="https://github.com/AmitSingh-23/LeetCode"><img src="https://img.shields.io/badge/DSA_solutions-181717?style=for-the-badge&logo=github&logoColor=white" alt="DSA solutions"></a>
