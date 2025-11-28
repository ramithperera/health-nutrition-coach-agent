"""Integration tests for the Health & Nutrition Coach Agent."""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import the agent
from nutrition_coach_agent.agent import root_agent


def test_agent_creation():
    """Test that the agent is created successfully."""
    assert root_agent is not None
    assert root_agent.name == "health_nutrition_coach"
    print("✅ Agent created successfully")


def test_sub_agents():
    """Test that all sub-agents are present."""
    sub_agent_names = [agent.name for agent in root_agent.sub_agents]

    expected_agents = [
        "nutrition_planner",
        "workout_advisor",
        "progress_tracker",
        "recovery_specialist"
    ]

    for agent_name in expected_agents:
        assert agent_name in sub_agent_names, f"Missing sub-agent: {agent_name}"
        print(f"✅ Found sub-agent: {agent_name}")


def test_tools():
    """Test that all required tools are available."""
    tool_names = []
    for tool in root_agent.tools:
        if hasattr(tool, '__name__'):
            tool_names.append(tool.__name__)
        elif hasattr(tool, 'name'):
            tool_names.append(tool.name)

    expected_tools = [
        "save_user_profile",
        "save_meal_plan_to_memory",
        "get_user_stats"
    ]

    for tool_name in expected_tools:
        assert tool_name in tool_names, f"Missing tool: {tool_name}"
        print(f"✅ Found tool: {tool_name}")

    print(f"✅ All required tools are available")


def test_configuration():
    """Test that configuration is loaded."""
    from nutrition_coach_agent.config import GOOGLE_API_KEY, MAIN_MODEL

    assert GOOGLE_API_KEY is not None, "GOOGLE_API_KEY not found in environment"
    assert MAIN_MODEL == "gemini-2.0-flash", "Incorrect model configuration"

    print("✅ Configuration loaded successfully")


def test_session_memory():
    """Test session memory functionality."""
    from nutrition_coach_agent.tools import session_memory

    # Test profile saving
    test_profile = {
        "name": "Test User",
        "age": 30,
        "weight_kg": 75,
        "fitness_goal": "muscle_gain"
    }
    result = session_memory.set_user_profile(test_profile)
    assert "Test User" in result

    # Test workout logging
    test_workout = {
        "type": "strength",
        "duration": 60,
        "intensity": "high"
    }
    result = session_memory.log_workout(test_workout)
    assert "strength" in result.lower()

    # Test hydration logging
    result = session_memory.log_hydration(500)
    assert "500" in result

    print("✅ Session memory working correctly")


def run_all_tests():
    """Run all integration tests."""
    print("=" * 60)
    print("🚀 Running Health & Nutrition Coach Agent Tests")
    print("=" * 60)

    try:
        test_agent_creation()
        test_sub_agents()
        test_tools()
        test_configuration()
        test_session_memory()

        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\n💡 Next steps:")
        print("   1. Run 'adk web' to start the web interface")
        print("   2. Open http://localhost:8000 in your browser")
        print("   3. Select 'health_nutrition_coach' from the dropdown")
        print("   4. Start chatting with your agent!")

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_all_tests()