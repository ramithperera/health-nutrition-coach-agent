"""Configuration for the Health & Nutrition Coach Agent."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_GENAI_USE_VERTEXAI = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")

# Model Configuration
PLANNER_MODEL = "gemini-2.0-flash"
NUTRITION_MODEL = "gemini-2.0-flash"
WORKOUT_MODEL = "gemini-2.0-flash"
TRACKER_MODEL = "gemini-2.0-flash"
RECOVERY_MODEL = "gemini-2.0-flash"
MAIN_MODEL = "gemini-2.0-flash"

# Agent Configuration
MAX_RETRIES = 3

# Nutrition Goals (default macros for different goals)
MACRO_TARGETS = {
    "muscle_gain": {"protein": 0.35, "carbs": 0.45, "fats": 0.20},
    "weight_loss": {"protein": 0.40, "carbs": 0.30, "fats": 0.30},
    "maintenance": {"protein": 0.30, "carbs": 0.40, "fats": 0.30},
    "endurance": {"protein": 0.25, "carbs": 0.55, "fats": 0.20}
}

# Hydration targets (ml per kg of body weight)
HYDRATION_BASE = 35  # ml/kg for sedentary
HYDRATION_ACTIVE = 45  # ml/kg for active individuals
HYDRATION_INTENSE = 55  # ml/kg for intense training