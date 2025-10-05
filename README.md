# AEGIS Habitat Layout Creator

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/kritgarb/Habitat-Layout-Creator)
[![Python](https://img.shields.io/badge/python-3.11+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

An interactive web application for designing and validating space habitats based on official NASA standards. Developed for the NASA Space Apps Challenge 2024.

**Live Demo:** [https://nsa-aegis.us/](https://nsa-aegis.us/)

---

## Table of Contents

- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Local Installation](#local-installation)
  - [Docker](#docker)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Team](#team)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Key Features

- **Dual Geometry Support**: Design cylindrical or rectangular habitats.
- **Real-time NASA Validation**: All calculations are compliant with NASA Human Integration Design Handbook (HIDH) standards.
- **Interactive Visualizations**: Includes a 2D floor plan and a 3D model viewer powered by Plotly.
- **Functional Zone Management**: Allocate space for six key zones: Sleep, Work/Leisure, Hygiene, Kitchen, Exercise, and Storage.
- **Dynamic Mission Parameters**: Configure crew size, mission duration, and gravity environment.
- **Automated Metrics**: Instantly view total volume, Net Habitable Volume (NHV), floor area per person, and zone distribution.
- **JSON Export**: Save and share your complete habitat configuration.

---

## Technology Stack

- **Core**: Python 3.11+
- **Web Framework**: Streamlit
- **Visualizations**: Plotly
- **Numerical Calculations**: NumPy
- **Deployment**: Docker, Google Cloud Run

---

## Getting Started

### Prerequisites

- Python 3.9+
- `pip` and `venv`

### Local Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kritgarb/Habitat-Layout-Creator.git
    cd Habitat-Layout-Creator
    ```

2.  **Create and activate a virtual environment:**
    - On Windows:
      ```powershell
      python -m venv venv
      .\venv\Scripts\Activate.ps1
      ```
    - On Linux/macOS:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

5.  Access the application at `http://localhost:8501`.

### Docker

Alternatively, you can use Docker and Docker Compose to run the project in a container.

1.  **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

2.  **Or, build and run the container manually:**
    ```bash
    docker build -t habitat-layout-creator .
    docker run -p 8501:8501 habitat-layout-creator
    ```

---

## Usage

1.  **Configure Habitat**: Use the sidebar to select the habitat's shape, dimensions, and functional zones.
2.  **Set Mission Parameters**: Adjust crew size, mission duration, and gravity.
3.  **Review Metrics**: Check the real-time calculations for volume, NHV, and floor area against NASA standards.
4.  **Explore Visualizations**: Switch between the 2D and 3D layout pages to view the interactive models.
5.  **Export Configuration**: Download the complete design as a JSON file.

---

## Project Structure

```
Habitat-Layout-Creator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker build configuration
├── LICENSE             # MIT License
└── src/
    ├── components/     # Reusable UI components
    ├── config/         # Project constants and styles
    ├── pages/          # Application pages
    ├── utils/          # Calculation and validation functions
    └── visualizations/ # Plotly visualization generators
```

---

## Scientific References

This tool implements calculations and validations based on official NASA documentation:

- **NASA Human Integration Design Handbook (HIDH)**: [NASA/SP-2010-3407](https://www.nasa.gov/wp-content/uploads/2023/03/human-integration-design-handbook-revision-1.pdf?emrc=68e269191aa6f)
- **ISS Research Publications**: [Official Website](https://issnationallab.org/publications/)
- **Human Spaceflight Standards**: [Official Website](https://www.nasa.gov/ochmo/human-spaceflight-and-aviation-standards/)

---

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to report bugs or suggest features.

---

## Team

This project was developed by the **ENTERPRISE Team** for the NASA Space Apps Challenge 2024.

- **Benjamin Vieira** (Project Lead & Development)
- **Alice Araujo** (Development)
- **Gabryel Batista** (Design & UX)
- **Vitória Ferreira** (Quality Assurance)
- **Caio Chagas** (Research & Documentation)
- **Enzo Andrade** (English Review & Testing)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **NASA** for their extensive research and public standards on space habitability.
- The **Streamlit** and **Plotly** communities for their excellent open-source frameworks.