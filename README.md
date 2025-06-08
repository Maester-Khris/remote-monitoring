# 🚀 Remote System Monitoring Suite (still in development)

This project is a **full-stack monorepo** designed to simulate and monitor remote systems in real time. It consists of:
- **📦 Django Backend (`djangobackend/`)**: Simulates remote servers, streams logs, and exposes system health data.
- **⚛️ React Frontend (`ReactClient/`)**: A client application for tracking logs, visualizing system performance, and monitoring health.

---

## 🧩 Monorepo Structure
<!-- ├── djangobackend
├── ReactClient -->
<pre>
<code> ├── djangobackend <br/> ├── ReactClient</code>
</pre>

---

## 🧠 Project Overview

This system is designed to provide an end-to-end simulation of:

1. **Remote servers** generating and streaming log data.
2. A **frontend dashboard** tracking:
   - Log streams
   - System status & health checks
   - Visual metrics and alerts

---

## 🛠️ Technologies Used

### Backend (`djangobackend/`)
- **Python 3.x**
- **Django**
- Django REST Framework (for API endpoints)
- Server Sent Event 
- Log generation & health check simulation

### Frontend (`ReactClient/`)
- **React (v19)**
- **Vite (v6.3)**
- **TypeScript (v5.8)**
- **Tailwind CSS (v4)**
- **Recharts** (for data visualization)
- **Slick-carousel** (for component sliders)
- **Phosphor Icons** (for UI elements)

React online link: [Rx Monitor](https://react-client-nkops-projects.vercel.app)
---

## 📦 Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Maester-Khris/remote-monitoring.git
cd remote-monitoring
```

### 2. Setup Frontend (React)
```bash
cd ../ReactClient
npm install
npm run dev
```

---

## 📡 How It Works
- The **Django backend** simulates remote servers, periodically emitting logs and exposing API endpoints for system data.
- The **React client** connects to the backend to:
  - Stream and visualize logs
  - Display system metrics
  - Track system uptime and availability

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change or add.