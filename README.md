# 🌌 Solar System Simulator
A Python-based interactive 2D/3D Solar System simulator built with **Pygame** and **Pygame GUI**, featuring orbit trails, parallax star backgrounds, a toggleable 3D view, mini-map, background space sounds, and GUI buttons for easy control.

## 🚀 Features

- 🪐 Accurate relative orbit speeds and distances (scaled)
- 🌌 Multi-layer **parallax starfield background**
- 🌍 Toggle between **2D and simulated 3D** orbital view
- 🧭 **Mini-map** shows real-time planet positions
- 🌀 Animated **orbit trails** for all planets
- 🕹 GUI buttons:
  - Pause / Play simulation
  - Toggle 2D ↔ 3D View
  - Mute / Unmute background music
- 🔊 **Ambient space music** to enhance realism
- 🖱 Zoom and drag camera using mouse

## 📁 Project Structure
<pre>
solar-system-3d-simulator/
├── planets/
│   ├── sun.png
│   ├── mercury.png
│   ├── venus.png
│   ├── earth.png
│   ├── mars.png
│   ├── jupiter.png
│   ├── saturn_ring.png
│   ├── uranus.png
│   └── neptune.png
│
├── sounds/
│   └── space_ambient.mp3
│ 
├── outputs/
│   ├── 2D output
│   └── 3D output
│
├── solar_system.py
└── README.md
</pre>

## 🧑‍💻 Requirements
- Python 3.8+
- `pygame`
- `pygame_gui`

## 📦 Installation
<pre>
  pip install pygame pygame_gui
</pre>

## 🖱 Controls

| Action           | How                          |
|------------------|-------------------------------|
| **Zoom**         | Mouse wheel scroll            |
| **Drag**         | Left mouse click + drag       |
| **Pause / Resume** | Click **Pause** button       |
| **2D / 3D Toggle** | Click **Toggle 3D** button   |
| **Mute / Unmute** | Click **Mute** button         |
