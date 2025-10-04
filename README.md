# Habitat Layout Creator

**NASA Space Apps Challenge 2025**

Modern, interactive tool for designing and validating space habitat layouts with real NASA standards.

## Features

### Modern Interface
- **Dark Theme**: Sleek, professional design optimized for focus
- **Purple Gradient**: Distinctive brand identity
- **Responsive Layout**: Clean metric cards and visualizations
- **Professional Design**: Modern icons and symbols
- **Interactive 3D**: Plotly-powered 3D habitat visualization
- **2D Floor Plans**: Interactive Plotly 2D layouts with zone details

### Core Functionality
- ✓ Design cylindrical or rectangular habitats
- ✓ Automatic volume, NHV, and floor area calculations
- ✓ Allocation of functional zones (sleep, hygiene, kitchen, exercise, storage, work)
- ✓ Real-time NASA standards validation (NHV ≥ 25 m³/person)
- ✓ Interactive 3D visualization with orbit, zoom, and pan controls
- ✓ 2D floor plan with hover details
- ✓ Launch vehicle envelope verification (SLS/Starship)
- ✓ JSON export with mission metadata
- ✓ User-friendly Streamlit interface

## Project Structure

```
nsa-2025/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose setup
├── README.md                   # This file
├── LICENSE                     # MIT License
├── src/                        # Source code (modular)
│   ├── config/                 # Configuration files
│   │   ├── constants.py        # NASA standards & zone config
│   │   └── styles.py           # CSS styling
│   ├── utils/                  # Utility functions
│   │   ├── calculations.py     # Volume, NHV, area calculations
│   │   └── validators.py       # NASA standards validation
│   ├── visualizations/         # Plotly visualizations
│   │   ├── layout_2d.py        # 2D floor plan
│   │   └── layout_3d.py        # 3D habitat view
│   └── components/             # Streamlit UI components
│       ├── sidebar.py          # Configuration sidebar
│       ├── metrics.py          # Metrics & validation display
│       └── export.py           # Data export functionality
├── data/                       # Export directory
└── docs_archive/              # Archived documentation
```

## Tech Stack

- **Python 3.11**: Core programming language
- **Streamlit 1.28.0**: Web framework for rapid prototyping
- **Plotly 5.5.0**: Interactive 3D and 2D visualizations
- **NumPy 1.21.0**: Numerical computations and 3D mesh generation
- **CairoSVG 2.7.1**: SVG manipulation (optional)
- **Pillow 10.1.0**: Image processing (optional)
- **Docker**: Containerization for deployment

## Quick Start

### Local Installation

### 1. Clone & Setup

```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run Application

```powershell
streamlit run app.py
```

Access at: **http://localhost:8501**

### Docker

### Build Image

```powershell
docker build -t habitat-layout-creator .
```

### Run Container

```powershell
docker run -p 8501:8501 habitat-layout-creator
```

Or use Docker Compose:

```powershell
docker-compose up
```

## How to Use

1. **Configure Habitat**: Select shape (Cylinder/Rectangular) and dimensions in sidebar
2. **Set Mission Parameters**: Crew size, duration, and destination
3. **Review Metrics**: Check volume, NHV, and floor area calculations
4. **Validate Standards**: Ensure NASA requirements are met (green = pass)
5. **Explore 3D/2D Views**: 
   - **3D View**: Click + drag to orbit, scroll to zoom, double-click to reset
   - **2D Floor Plan**: Hover over zones for details
6. **Export Data**: Download JSON with complete habitat specifications

## NASA Standards Implemented

- **NHV Minimum**: ≥ 25 m³ per person (Net Habitable Volume)
- **Floor Area Minimum**: ≥ 10 m² per person
- **Launch Vehicle Compatibility**: SLS (Ø ≤ 8.4m), Starship (Ø ≤ 9.0m)
- **Functional Zones**: 6 zones with minimum area requirements
- **Life Support**: Water calculation (2.5 L/day/person)

## Code Architecture

The project follows a **modular architecture** for maintainability:

- **`src/config/`**: Constants, NASA standards, styling
- **`src/utils/`**: Pure functions for calculations and validation
- **`src/visualizations/`**: Plotly 2D/3D rendering logic
- **`src/components/`**: Streamlit UI components (sidebar, metrics, export)
- **`app.py`**: Main orchestration and page layout

## Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest new features
- Submit pull requests
- Improve documentation

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- **NASA Space Apps Challenge 2025**
- NASA Human Integration Design Standards (NASA-STD-3001)
- ISS Habitat Design Experience

---

**Made with ❤️ for ENTERPRISE ON NASA Space Apps Challenge 2025**
