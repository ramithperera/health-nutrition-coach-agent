"""Custom tools for the Health & Nutrition Coach Agent."""

from typing import Dict, Any, Optional
from datetime import datetime
import json


class SessionMemory:
    """In-memory storage for user session data."""

    def __init__(self):
        self.user_profile: Optional[Dict[str, Any]] = None
        self.workout_logs: list = []
        self.meal_logs: list = []
        self.hydration_logs: list = []
        self.meal_plan: Optional[Dict[str, Any]] = None

    def set_user_profile(self, profile: Dict[str, Any]) -> str:
        """Store user profile information."""
        self.user_profile = profile
        return f"User profile saved: {profile.get('name', 'User')}"

    def log_workout(self, workout_data: Dict[str, Any]) -> str:
        """Log a workout session."""
        workout_entry = {
            "timestamp": datetime.now().isoformat(),
            "data": workout_data
        }
        self.workout_logs.append(workout_entry)
        return f"Workout logged: {workout_data.get('type', 'Unknown')} - {workout_data.get('duration', 0)} minutes"

    def log_meal(self, meal_data: Dict[str, Any]) -> str:
        """Log a meal."""
        meal_entry = {
            "timestamp": datetime.now().isoformat(),
            "data": meal_data
        }
        self.meal_logs.append(meal_entry)
        return f"Meal logged: {meal_data.get('name', 'Unknown meal')}"

    def log_hydration(self, water_ml: int) -> str:
        """Log water intake."""
        hydration_entry = {
            "timestamp": datetime.now().isoformat(),
            "amount_ml": water_ml
        }
        self.hydration_logs.append(hydration_entry)

        # Calculate daily total
        today = datetime.now().date()
        daily_total = sum(
            entry["amount_ml"]
            for entry in self.hydration_logs
            if datetime.fromisoformat(entry["timestamp"]).date() == today
        )

        return f"Logged {water_ml}ml of water. Today's total: {daily_total}ml"

    def get_daily_summary(self) -> Dict[str, Any]:
        """Get summary of today's activity."""
        today = datetime.now().date()

        today_workouts = [
            entry for entry in self.workout_logs
            if datetime.fromisoformat(entry["timestamp"]).date() == today
        ]

        today_meals = [
            entry for entry in self.meal_logs
            if datetime.fromisoformat(entry["timestamp"]).date() == today
        ]

        today_hydration = sum(
            entry["amount_ml"]
            for entry in self.hydration_logs
            if datetime.fromisoformat(entry["timestamp"]).date() == today
        )

        return {
            "date": today.isoformat(),
            "workouts": len(today_workouts),
            "meals": len(today_meals),
            "hydration_ml": today_hydration,
            "workout_details": today_workouts,
            "meal_details": today_meals
        }

    def save_meal_plan(self, meal_plan: Dict[str, Any]) -> str:
        """Save weekly meal plan."""
        self.meal_plan = {
            "created_at": datetime.now().isoformat(),
            "plan": meal_plan
        }
        return "Weekly meal plan saved successfully"

    def get_user_stats(self) -> Dict[str, Any]:
        """Get comprehensive user statistics."""
        return {
            "profile": self.user_profile,
            "total_workouts": len(self.workout_logs),
            "total_meals_logged": len(self.meal_logs),
            "total_hydration_entries": len(self.hydration_logs),
            "has_meal_plan": self.meal_plan is not None
        }


# Global session memory instance
session_memory = SessionMemory()


def save_user_profile(
        name: str,
        age: int,
        weight_kg: float,
        height_cm: float,
        fitness_goal: str,
        activity_level: str,
        dietary_restrictions: str = "",
        allergies: str = "",
        daily_calories: int = 0
) -> str:
    """
    Save user profile information to session memory.

    Args:
        name: User's name
        age: User's age in years
        weight_kg: User's weight in kilograms
        height_cm: User's height in centimeters
        fitness_goal: One of: muscle_gain, weight_loss, maintenance, endurance
        activity_level: One of: sedentary, light, moderate, active, very_active
        dietary_restrictions: Comma-separated list (e.g., "vegetarian, gluten-free")
        allergies: Comma-separated list of allergies
        daily_calories: Target daily calorie intake (if not provided, will be calculated)

    Returns:
        Confirmation message
    """
    profile = {
        "name": name,
        "age": age,
        "weight_kg": weight_kg,
        "height_cm": height_cm,
        "fitness_goal": fitness_goal,
        "activity_level": activity_level,
        "dietary_restrictions": [r.strip() for r in dietary_restrictions.split(",")] if dietary_restrictions else [],
        "allergies": [a.strip() for a in allergies.split(",")] if allergies else [],
        "daily_calories": daily_calories if daily_calories > 0 else None
    }

    return session_memory.set_user_profile(profile)


def log_workout(
        workout_type: str,
        duration_minutes: int,
        intensity: str,
        exercises: str = "",
        notes: str = ""
) -> str:
    """
    Log a workout session.

    Args:
        workout_type: Type of workout (e.g., strength, cardio, flexibility, sports)
        duration_minutes: Duration in minutes
        intensity: One of: low, moderate, high, very_high
        exercises: Comma-separated list of exercises performed
        notes: Additional notes about the workout

    Returns:
        Confirmation message with workout summary
    """
    workout_data = {
        "type": workout_type,
        "duration": duration_minutes,
        "intensity": intensity,
        "exercises": [e.strip() for e in exercises.split(",")] if exercises else [],
        "notes": notes
    }

    return session_memory.log_workout(workout_data)


def log_meal(
        meal_name: str,
        meal_type: str,
        foods: str,
        estimated_calories: int = 0,
        protein_g: float = 0.0,
        carbs_g: float = 0.0,
        fats_g: float = 0.0,
        notes: str = ""
) -> str:
    """
    Log a meal.

    Args:
        meal_name: Name or description of the meal
        meal_type: One of: breakfast, lunch, dinner, snack, pre_workout, post_workout
        foods: Comma-separated list of foods consumed
        estimated_calories: Estimated total calories
        protein_g: Protein in grams
        carbs_g: Carbohydrates in grams
        fats_g: Fats in grams
        notes: Additional notes

    Returns:
        Confirmation message
    """
    meal_data = {
        "name": meal_name,
        "type": meal_type,
        "foods": [f.strip() for f in foods.split(",")],
        "calories": estimated_calories if estimated_calories > 0 else None,
        "macros": {
            "protein": protein_g if protein_g > 0 else None,
            "carbs": carbs_g if carbs_g > 0 else None,
            "fats": fats_g if fats_g > 0 else None
        },
        "notes": notes
    }

    return session_memory.log_meal(meal_data)


def log_water_intake(amount_ml: int) -> str:
    """
    Log water intake.

    Args:
        amount_ml: Amount of water in milliliters

    Returns:
        Confirmation message with daily total
    """
    return session_memory.log_hydration(amount_ml)


def get_daily_summary() -> str:
    """
    Get a summary of today's logged activities.

    Returns:
        JSON string containing today's workouts, meals, and hydration
    """
    summary = session_memory.get_daily_summary()
    return json.dumps(summary, indent=2)


def save_meal_plan_to_memory(meal_plan_json: str) -> str:
    """
    Save a weekly meal plan to session memory.

    Args:
        meal_plan_json: JSON string containing the weekly meal plan

    Returns:
        Confirmation message
    """
    try:
        meal_plan = json.loads(meal_plan_json)
        return session_memory.save_meal_plan(meal_plan)
    except json.JSONDecodeError:
        return "Error: Invalid meal plan format. Please provide valid JSON."


def get_user_stats() -> str:
    """
    Get comprehensive user statistics and current state.

    Returns:
        JSON string containing user profile and activity statistics
    """
    stats = session_memory.get_user_stats()
    return json.dumps(stats, indent=2)