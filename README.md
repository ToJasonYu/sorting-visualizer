# 📊 Sorting Visualizer

### [🔴 Live Demo](https://sorting-visualizer.onrender.com)

A web application with frontend + backend, designed to visualize how classic sorting algorithms work in real-time. This project is architected with a **React** frontend for dynamic rendering and a separate **Python (Flask)** backend to handle the algorithmic logic, demonstrating a clean client-server separation.

![Project Screenshot](demo.png)

## 🚀 Key Features

* **10 Different Algorithms:** Visualizes a wide range of sorting methods, from standard efficient algorithms (Quick Sort, Merge Sort) to educational ones (Bubble Sort, Gnome Sort).
* **Real-Time Animations:** Watch the array sort step-by-step with color-coded states (Active, Locked, Unsorted).
* **Decoupled Architecture:** The sorting logic resides entirely on the Python backend, sending animation steps to the React frontend via a REST API.
* **Speed & Size Control:** Interactive sliders to adjust array size and visualization speed.
* **Complexity Analysis:** Displays Time and Space complexity (Big O) for the selected algorithm.
* **Code Viewer:** View the actual Python implementation code side-by-side with the visualizer.

## 🛠️ Tech Stack

* **Frontend:** React.js, Vite, CSS3
* **Backend:** Python 3, Flask, CORS
* **Deployment:** Render (Separate services for Static Site and Web Service)
* **Communication:** REST API (Axios)

## 📂 Project Structure

This project follows a professional separation of concerns:

```bash
/
├── frontend/         # React Client (UI & Animation Logic)
│   ├── src/          # Components, hooks, and styles
│   └── dist/         # Production build artifacts
├── backend/          # Python API (Server & Algorithms)
│   ├── app.py        # Flask entry point
│   └── sorting_algorithms.py # Pure Python implementations
└── README.md
