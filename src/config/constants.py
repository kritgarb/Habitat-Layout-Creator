"""
NASA constants and configurations for the Habitat Layout Creator

Based on:
- Defining the Net Habitable Volume for Long Duration Exploration Missions
- Moon to Mars Architecture Definition Document
- Deep Space Habitability Design Guidelines (NASA NextSTEP Phase 2)
- NASA's Moon to Mars Transit Habitat Refinement Point of Departure Design
"""

# ========================================
# NASA STANDARDS - VOLUME AND AREA
# ========================================
# Reference: Defining the Net Habitable Volume for Long Duration Exploration Missions
MIN_NHV_PER_PERSON = 25  # m³ per person (long missions)
MIN_NHV_PER_PERSON_TRANSIT = 27  # m³ per person (transit habitats - higher due to stress)
MIN_FLOOR_AREA_PER_PERSON = 10  # m² per person
MIN_PRIVACY_VOLUME_PER_PERSON = 5.0  # m³ (essential private area)

# ========================================
# LIFE SUPPORT RESOURCES (QUANTIFIED)
# ========================================
# Reference: NASA-STD-3001 and Human Integration Design Handbook (HIDH)
WATER_POTABLE_PER_DAY_PER_PERSON = 2.0  # kg (potable water)
WATER_FOOD_PREP_PER_DAY_PER_PERSON = 0.5  # kg (food rehydration)
WATER_HYGIENE_PER_DAY_PER_PERSON = 23.0  # liters (hygiene, recyclable)
OXYGEN_CONSUMPTION_PER_DAY_PER_PERSON = 0.82  # kg (metabolic consumption)
CO2_PRODUCTION_PER_DAY_PER_PERSON = 1.04  # kg (metabolic production)
FOOD_PER_DAY_PER_PERSON = 0.62  # kg (dry food)
POWER_PER_PERSON = 2000  # Watts (average)

# Biomass Production Chamber (BPC) area for O2 production
BPC_AREA_PER_PERSON = 22.5  # m² (20-25 m² of crops to provide O2)

# ========================================
# LAUNCH ENVELOPE
# ========================================
# Reference: Moon to Mars Architecture Definition Document
SLS_MAX_DIAMETER = 8.4  # meters (NASA Space Launch System)
SLS_MAX_HEIGHT = 27.4  # meters (cargo compartment)
STARSHIP_MAX_DIAMETER = 9.0  # meters (SpaceX Starship)
STARSHIP_MAX_HEIGHT = 17.24  # meters (cargo compartment)

# ========================================
# ERGONOMIC AND ANTHROPOMETRIC DIMENSIONS
# ========================================
# Reference: Human Integration Design Handbook (HIDH) - Clearance and Reach
MIN_CEILING_HEIGHT = 2.1  # meters
MIN_CORRIDOR_WIDTH = 0.81  # meters (minimum emergency path)
MIN_CORRIDOR_WIDTH_HIGH_TRAFFIC = 1.14  # meters (dual passage)
MIN_DOOR_WIDTH = 0.7  # meters
MIN_DOOR_HEIGHT = 1.9  # meters
MIN_WORKSTATION_AREA = 1.5  # m² per workstation

# Clearance dimensions for pressurized suits
EVA_SUIT_WIDTH_CLEARANCE = 0.9  # meters (width with EVA suit)
EVA_SUIT_HEIGHT_CLEARANCE = 2.3  # meters (height with EVA suit)

# Minimum emergency path dimensions (unobstructed)
EMERGENCY_PATH_WIDTH = 0.81  # meters
EMERGENCY_PATH_HEIGHT = 1.14  # meters

# ========================================
# ENVIRONMENTAL STANDARDS
# ========================================
# Reference: Deep Space Habitability Design Guidelines
TEMP_MIN = 18  # °C
TEMP_MAX = 27  # °C
HUMIDITY_MIN = 30  # %
HUMIDITY_MAX = 70  # %
MAX_CO2 = 5.3  # mmHg (0.7 kPa)
MAX_NOISE_SLEEP = 60  # dB (sleep area)
MAX_NOISE_WORK = 70  # dB (work areas)

# ========================================
# LIGHTING
# ========================================
# Reference: Deep Space Habitability Design Guidelines
MIN_LUX = 200  # lux
MAX_LUX = 500  # lux
COLOR_TEMP_MIN = 2700  # Kelvin (warm light - night)
COLOR_TEMP_MAX = 6500  # Kelvin (cool light - day)

# ========================================
# FUNCTIONAL ZONES - COLORS
# ========================================
# Functional zone colors
ZONE_COLORS = {
    "sleep": "#667eea",
    "hygiene": "#48bb78",
    "kitchen": "#ed8936",
    "exercise": "#f56565",
    "storage": "#9f7aea",
    "work_leisure": "#4299e1"
}

# Zone names
ZONE_NAMES = {
    "sleep": "Sleep Quarters",
    "hygiene": "Hygiene Module",
    "kitchen": "Kitchen",
    "exercise": "Exercise Area",
    "storage": "Storage",
    "work_leisure": "Work and Leisure"
}

# Minimum area and volume per person for each zone (m² and m³)
# Reference: Internal Layout Assessment of a Lunar Surface Habitat + HIDH
ZONE_MIN_AREA = {
    "sleep": 4.0,
    "hygiene": 2.0,
    "kitchen": 3.0,
    "exercise": 2.5,
    "storage": 3.0,
    "work_leisure": 5.0
}

# Operational volume per zone (m³)
ZONE_VOLUMES = {
    "sleep": 2.69,  # Individual sleep accommodation
    "hygiene": 3.0,  # Includes restraints for 0g
    "kitchen": 10.09,  # Collective dining area (4 people)
    "exercise": 24.0,  # Operational volume of equipment + movement
    "storage": 5.0,  # Distributed storage
    "work_leisure": 18.20  # Collective area for 4 people
}

# ========================================
# INCOMPATIBILITIES AND ADJACENCIES (CONFLICT MATRIX)
# ========================================
# Reference: Internal Layout Assessment of a Lunar Surface Habitat + HIDH
# Incompatible zones (should not be adjacent) - with reasons
INCOMPATIBLE_ZONES = {
    ("sleep", "exercise"): "Noise and vibration incompatible with rest",
    ("sleep", "kitchen"): "Odors, preparation noise, constant activity",
    ("hygiene", "kitchen"): "Sanitary and psychological reasons (odors)"
}

# Zones that should be close (recommended adjacencies)
ADJACENT_ZONES_RECOMMENDED = {
    ("hygiene", "sleep"): "Convenience of access to quarters",
    ("kitchen", "work_leisure"): "Integrated social area",
    ("storage", "kitchen"): "Access to food supplies"
}

# Zone isolation requirements
ZONE_ISOLATION_REQUIREMENTS = {
    "sleep": {
        "acoustic": True,  # Mandatory acoustic isolation
        "privacy_visual": True,  # Total visual privacy
        "max_noise_db": 60
    },
    "hygiene": {
        "acoustic": False,
        "privacy_visual": True,  # Total visual privacy
        "max_noise_db": 70
    },
    "exercise": {
        "acoustic": True,  # Must be isolated to not transmit vibration
        "privacy_visual": False,
        "vibration_isolation": True  # Structural vibration isolation
    }
}

# ========================================
# FOOD PRODUCTION (OPTIONAL)
# ========================================
# Reference: Food Production on the Moon and in Remote Areas
FOOD_PRODUCTION_AREA_PER_PERSON = 6.0  # m² (hydroponics)
FOOD_PRODUCTION_HEIGHT = 2.0  # meters (plant growth)
FOOD_PRODUCTION_WATER_PER_DAY = 8.0  # liters per person
FOOD_PRODUCTION_POWER = 200  # W/m² (LED lighting)
FOOD_O2_PRODUCTION = 0.5  # kg/day/person (photosynthesis)

# ========================================
# MISSION TYPES
# ========================================
# Reference: Moon to Mars Architecture Definition Document
MISSION_TYPES = {
    "transit": {
        "description": "Transit habitat (Earth-Mars)",
        "duration_days": (180, 300),
        "min_nhv_per_person": 27,
        "gravity": "zero_or_artificial",
        "critical_zones": ["exercise", "work_leisure", "sleep"]
    },
    "lunar_surface": {
        "description": "Lunar surface habitat",
        "duration_days": (30, 365),
        "min_nhv_per_person": 25,
        "gravity": "1/6_earth",
        "radiation_shielding": "regolith_2m+"
    },
    "mars_surface": {
        "description": "Martian surface habitat",
        "duration_days": (500, 900),
        "min_nhv_per_person": 25,
        "gravity": "3/8_earth",
        "radiation_shielding": "regolith_or_structure"
    }
}

# ========================================
# HABITAT STRUCTURE
# ========================================
# Reference: Review of Habitable Softgoods Inflatable Design
HABITAT_TYPES = {
    "rigid": {
        "description": "Rigid structure (aluminum/composite)",
        "volume_efficiency": 1.0,
        "mass_per_volume": 150,  # kg/m³
        "advantages": ["stiffness", "MMOD protection", "equipment mounting"],
        "disadvantages": ["limited volume", "high weight"]
    },
    "inflatable": {
        "description": "Inflatable structure (softgoods)",
        "volume_efficiency": 3.5,  # 3-4x larger than rigid
        "mass_per_volume": 40,  # kg/m³
        "advantages": ["large volume", "reduced weight", "packaging"],
        "disadvantages": ["sealing complexity", "limited stiffness"]
    }
}

# ========================================
# NHV CALCULATION FORMULAS
# ========================================
# Reference: Defining the Net Habitable Volume for Long Duration Exploration Missions
# Formula: NHV (m³/person) = 6.67 × ln(duration_in_days) - 7.79
def calculate_nhv_per_person(duration_days):
    """
    Calculates the minimum Net Habitable Volume (NHV) per person
    based on mission duration.
    
    Args:
        duration_days: Mission duration in days
        
    Returns:
        NHV in m³ per person
    """
    import math
    return 6.67 * math.log(duration_days) - 7.79

# Calculated reference values
NHV_REFERENCE = {
    30: round(calculate_nhv_per_person(30), 2),    # ~15.0 m³/person
    90: round(calculate_nhv_per_person(90), 2),    # ~22.2 m³/person
    180: round(calculate_nhv_per_person(180), 2),  # ~26.85 m³/person
    365: round(calculate_nhv_per_person(365), 2),  # ~31.7 m³/person
    500: round(calculate_nhv_per_person(500), 2),  # ~33.7 m³/person
    900: round(calculate_nhv_per_person(900), 2)   # ~37.4 m³/person
}

# ========================================
# GRAVITATIONAL ADAPTATION
# ========================================
# Reference: HIDH - Volume vs Horizontal Surface Area
GRAVITY_ENVIRONMENTS = {
    "microgravity": {
        "code": "0g",
        "description": "Microgravity (orbit, transit)",
        "primary_metric": "volume",  # Volume is the primary metric
        "use_ceiling_walls": True,   # Ceiling and walls are usable
        "restraints_required": True,  # Restraints mandatory
        "area_weight": 0.3,
        "volume_weight": 0.7
    },
    "lunar": {
        "code": "1/6g",
        "description": "Lunar gravity (1/6 of Earth)",
        "primary_metric": "area",  # Horizontal area is prioritized
        "use_ceiling_walls": False,
        "restraints_required": False,
        "area_weight": 0.7,
        "volume_weight": 0.3
    },
    "mars": {
        "code": "3/8g",
        "description": "Martian gravity (3/8 of Earth)",
        "primary_metric": "area",  # Horizontal area is prioritized
        "use_ceiling_walls": False,
        "restraints_required": False,
        "area_weight": 0.8,
        "volume_weight": 0.2
    }
}

# ========================================
# SAFETY - TRANSIENT ACCELERATION
# ========================================
# Reference: HIDH - Launch and Landing Acceleration
ACCELERATION_SAFETY = {
    "launch_landing": {
        "description": "Landing and launch requirements",
        "seating_type": "contoured_couch",  # Mandatory contoured seats
        "restraint_system": "5_point_harness",  # 5-point harness
        "orientation_preferred": "+Gx",  # Eyeballs-in (chest) - higher tolerance
        "max_acceleration_gs": 6.0,  # Maximum supportable acceleration
        "requirements": [
            "Contoured seats for load distribution",
            "Multi-point restraint system (5 points minimum)",
            "Elimination of rigid elements that cause point loading",
            "Spinal protection against injuries",
            "Preferred orientation +Gx (through chest)"
        ]
    },
    "emergency_egress": {
        "description": "Emergency exit requirements",
        "path_width_min": 0.81,  # meters
        "path_height_min": 1.14,  # meters
        "max_distance_to_exit": 30.0,  # meters
        "unobstructed": True  # Path must be completely unobstructed
    }
}
