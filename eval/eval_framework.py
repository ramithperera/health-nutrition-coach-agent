"""Evaluation framework for the Health & Nutrition Coach Agent."""

import os
from typing import List, Dict, Any
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from nutrition_coach_agent.agent import root_agent

# Load environment variables
load_dotenv()


class AgentEvaluator:
    """Evaluator for testing agent capabilities and quality."""

    def __init__(self, agent):
        self.agent = agent
        self.runner = Runner(
            agent=agent,
            session_service=InMemorySessionService()
        )
        self.test_results = []
        self.user_id = "test_user"
        self.session_id = "test_session"

    async def run_test_async(self, test_name: str, prompt: str, expected_elements: List[str]) -> Dict[str, Any]:
        """
        Run a single test case asynchronously.

        Args:
            test_name: Name of the test
            prompt: User prompt to send to agent
            expected_elements: List of expected elements in response

        Returns:
            Dictionary with test results
        """
        print(f"\n{'=' * 60}")
        print(f"🧪 Running Test: {test_name}")
        print(f"{'=' * 60}")
        print(f"📨 Prompt: {prompt}\n")

        try:
            # Run the agent
            response_text = ""
            async for event in self.runner.run_async(
                    user_id=self.user_id,
                    session_id=self.session_id,
                    new_message=prompt
            ):
                if hasattr(event, 'text') and event.text:
                    response_text += event.text

            print(f"🤖 Response Preview: {response_text[:300]}...\n")

            # Check for expected elements
            elements_found = []
            elements_missing = []

            for element in expected_elements:
                if element.lower() in response_text.lower():
                    elements_found.append(element)
                else:
                    elements_missing.append(element)

            success = len(elements_missing) == 0

            result = {
                "test_name": test_name,
                "prompt": prompt,
                "success": success,
                "response_length": len(response_text),
                "elements_found": elements_found,
                "elements_missing": elements_missing
            }

            self.test_results.append(result)

            if success:
                print(f"✅ Test PASSED - All {len(expected_elements)} elements found")
            else:
                print(f"⚠️ Test PARTIAL - {len(elements_found)}/{len(expected_elements)} elements found")
                print(f"   Missing: {', '.join(elements_missing)}")

            return result

        except Exception as e:
            print(f"❌ Test FAILED with error: {e}")
            result = {
                "test_name": test_name,
                "prompt": prompt,
                "success": False,
                "error": str(e)
            }
            self.test_results.append(result)
            return result

    def run_test(self, test_name: str, prompt: str, expected_elements: List[str]) -> Dict[str, Any]:
        """Synchronous wrapper for run_test_async."""
        import asyncio
        return asyncio.run(self.run_test_async(test_name, prompt, expected_elements))

    def print_summary(self):
        """Print overall test summary."""
        print(f"\n{'=' * 60}")
        print("📊 EVALUATION SUMMARY")
        print(f"{'=' * 60}")

        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results if r.get("success", False))

        print(f"\nTotal Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {total_tests - passed_tests}")
        print(f"Success Rate: {(passed_tests / total_tests) * 100:.1f}%")

        print("\n📋 Test Details:")
        for i, result in enumerate(self.test_results, 1):
            status = "✅" if result.get("success") else "❌"
            print(f"{i}. {status} {result['test_name']}")


def run_evaluation():
    """Run comprehensive evaluation of the Health & Nutrition Coach Agent."""

    evaluator = AgentEvaluator(root_agent)

    # Test 1: Initial Onboarding
    evaluator.run_test(
        test_name="Initial Onboarding",
        prompt="Hi! I'm new here and want to start my fitness journey. I'm 28 years old, weigh 75kg, height 175cm, and want to gain muscle.",
        expected_elements=[
            "profile",
            "calorie",
            "protein",
            "goal",
            "muscle"
        ]
    )

    # Test 2: Meal Plan Creation
    evaluator.run_test(
        test_name="Meal Plan Creation",
        prompt="Can you create a weekly meal plan for me? I'm vegetarian and allergic to nuts.",
        expected_elements=[
            "meal plan",
            "vegetarian",
            "protein",
            "breakfast",
            "lunch",
            "dinner"
        ]
    )

    # Test 3: Workout Program
    evaluator.run_test(
        test_name="Workout Program Design",
        prompt="I need a workout program for muscle gain. I have access to a full gym.",
        expected_elements=[
            "workout",
            "muscle",
            "exercises",
            "sets",
            "reps"
        ]
    )

    # Test 4: Hydration Tracking
    evaluator.run_test(
        test_name="Hydration Guidance",
        prompt="How much water should I drink daily? And can you help me track it?",
        expected_elements=[
            "water",
            "hydration",
            "ml",
            "track"
        ]
    )

    # Test 5: Recovery Guidance
    evaluator.run_test(
        test_name="Recovery Guidance",
        prompt="Tomorrow is my rest day. What should I do differently with my nutrition and activities?",
        expected_elements=[
            "rest day",
            "recovery",
            "nutrition",
            "protein"
        ]
    )

    # Print summary
    evaluator.print_summary()

    return evaluator.test_results


if __name__ == "__main__":
    print("🚀 Starting Health & Nutrition Coach Agent Evaluation")
    print("=" * 60)

    results = run_evaluation()

    print(f"\n{'=' * 60}")
    print("✅ Evaluation Complete!")
    print(f"{'=' * 60}\n")