[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google ADK](https://img.shields.io/badge/Built%20with-Google%20ADK-blue.svg)](https://google.github.io/adk-docs/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-20BEFF.svg)](https://www.kaggle.com/competitions/agents-intensive-capstone-project)

# Health & Nutrition Coach Agent 🏋️‍♂️🥗

> **NOTE**: This is a submission for the [Kaggle Agents Intensive Capstone project](https://www.kaggle.com/competitions/agents-intensive-capstone-project). This agent is built using **Google Agent Development Kit (ADK)** and follows a modular multi-agent architecture inspired by [Agent Shutton](https://github.com/cloude-google/agent-shutton).

A comprehensive AI-powered health and nutrition coaching system that integrates personalized meal planning, workout guidance, progress tracking, and recovery optimization. Built with Google's Agent Development Kit (ADK), this multi-agent system provides holistic health and fitness coaching.

## 🎯 Problem Statement

Maintaining a healthy lifestyle requires juggling multiple complex tasks:
- **Nutrition Planning**: Creating balanced meal plans that align with fitness goals and dietary restrictions is time-consuming and requires extensive nutritional knowledge
- **Workout Programming**: Designing effective training programs requires understanding of exercise science, progressive overload, and individual capabilities
- **Progress Tracking**: Manually logging meals, workouts, and hydration while analyzing patterns and trends is tedious
- **Recovery Optimization**: Understanding when to rest, how to adjust nutrition for rest days, and preventing overtraining requires expertise
- **Integration**: Coordinating nutrition timing with workout schedules and adjusting plans based on progress is challenging

Many people struggle to maintain consistency or optimize their approach without hiring expensive personal trainers and nutritionists.

## 💡 Solution

The Health & Nutrition Coach Agent automates and optimizes the entire health and fitness journey through AI-powered coaching. The system:
- **Personalizes** nutrition plans based on individual goals, body composition, and dietary needs
- **Designs** progressive workout programs tailored to fitness level and available equipment
- **Tracks** all activities (meals, workouts, hydration) with intelligent analytics and insights
- **Optimizes** recovery through rest day guidance and sleep recommendations
- **Integrates** nutrition timing with training schedules for maximum results
- **Adapts** recommendations based on progress and feedback

This multi-agent system provides expert-level coaching accessible to everyone, making sustainable health and fitness achievable.

## 🏗️ Architecture

The Health & Nutrition Coach Agent is a **multi-agent system** built with Google's ADK. It consists of:

### Main Orchestrator Agent
**`root_agent`** (health_nutrition_coach) - The central coordinator that manages user interactions and delegates to specialized sub-agents

### Specialized Sub-Agents

1. **`nutrition_planner`** - Expert Nutritionist
   - Creates comprehensive weekly meal plans
   - Calculates macro/micronutrient targets
   - Respects dietary restrictions and allergies
   - Optimizes meal timing around workouts
   - Generates shopping lists and meal prep strategies

2. **`workout_advisor`** - Personal Trainer
   - Designs goal-specific workout programs
   - Provides exercise library with form cues
   - Tracks progressive overload
   - Balances training modalities (strength, cardio, flexibility)
   - Recommends periodization strategies

3. **`progress_tracker`** - Analytics Expert
   - Logs workouts, meals, and hydration
   - Analyzes patterns and trends
   - Calculates personalized hydration targets
   - Provides daily summaries and insights
   - Identifies areas for improvement

4. **`recovery_specialist`** - Recovery Expert
   - Guides rest day nutrition adjustments
   - Recommends active recovery activities
   - Optimizes sleep and stress management
   - Prevents overtraining
   - Suggests mobility and flexibility work

## 🛠️ Tools & Capabilities

### Session Memory Tools
- `save_user_profile()` - Store comprehensive user information
- `log_workout()` - Record exercise sessions with details
- `log_meal()` - Track food intake with macro breakdown
- `log_water_intake()` - Monitor daily hydration
- `get_daily_summary()` - Retrieve today's activity summary
- `save_meal_plan_to_memory()` - Store weekly meal plans
- `get_user_stats()` - Access overall progress and statistics

### Google Search Integration
All sub-agents have access to Google Search for:
- Current nutrition research and food data
- Exercise science and training methodologies
- Recipe ideas and meal inspiration
- Recovery techniques and best practices

### Data Storage
All data is stored **in-memory for the current session**:
- User profile (age, weight, goals, restrictions)
- Workout logs with exercises, sets, reps, intensity
- Meal logs with foods, macros, calories
- Hydration logs with timestamps
- Weekly meal plans

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Google API key (from [Google AI Studio](https://ai.google.dev/))

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd health-nutrition-coach-agent
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your Google API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

### Running the Agent

**Start the web interface:**
```bash
adk web
```

This will:
1. Start a local web server (usually on http://localhost:8000)
2. Open your browser automatically
3. Display the agent chat interface

**Select "health_nutrition_coach" from the dropdown** and start chatting!

**Run integration tests:**
```bash
python -m tests.test_agent
```

**Run evaluation:**
```bash
python -m eval.eval_framework
```

## 📁 Project Structure

```
health-nutrition-coach-agent/
│
├── nutrition_coach_agent/          # Main package
│   ├── __init__.py                 # Package initialization (imports agent)
│   ├── agent.py                    # Main orchestrator + sub-agents
│   ├── config.py                   # Configuration & model settings
│   └── tools.py                    # Custom tools & session memory
│
├── tests/                          # Integration tests
│   ├── __init__.py
│   └── test_agent.py
│
├── eval/                           # Evaluation framework
│   ├── __init__.py
│   └── eval_framework.py
│
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment template
├── .gitignore
├── README.md                       # This file
```

## 🔄 Workflow

The agent follows this comprehensive coaching workflow:

### 1. **Initial Onboarding**
- Collect user profile (age, weight, height, goals)
- Determine fitness goal (muscle gain, weight loss, maintenance, endurance)
- Identify dietary restrictions and allergies
- Calculate personalized calorie and macro targets
- Set hydration goals based on body weight and activity level

### 2. **Needs Assessment**
Ask user what they need:
- Weekly meal plan creation
- Workout program design
- Daily activity logging
- Progress review and insights
- Recovery guidance

### 3. **Delegation to Specialists**
Route requests to appropriate sub-agents:
- **Meal planning** → nutrition_planner
- **Workout guidance** → workout_advisor
- **Logging & tracking** → progress_tracker
- **Recovery optimization** → recovery_specialist

### 4. **Continuous Coaching**
- Monitor daily activities and progress
- Provide encouragement and accountability
- Adjust recommendations based on feedback
- Answer questions across all health domains

### 5. **Integration & Optimization**
- Align meal timing with workout schedule
- Adjust nutrition for training vs rest days
- Balance training stress with recovery
- Optimize for sustainable long-term results

## 🎓 Key Features

### ✅ Personalized Meal Planning
- 7-day meal plans with 3 meals + snacks
- Macro breakdown (protein/carbs/fats) for each meal
- Pre/post-workout nutrition optimization
- Dietary restriction and allergy compliance
- Shopping lists and meal prep instructions

### ✅ Goal-Specific Training
- **Muscle Gain**: Progressive resistance training, compound movements
- **Weight Loss**: Resistance + cardio, HIIT integration
- **Endurance**: Cardiovascular capacity building, interval training
- **Maintenance**: Balanced sustainable routine

### ✅ Comprehensive Tracking
- Workout logs (exercises, sets, reps, intensity)
- Meal logs (foods, macros, calories, timing)
- Hydration monitoring (personalized targets)
- Daily and weekly summaries

### ✅ Recovery Optimization
- Rest day nutrition adjustments (maintain protein, reduce carbs)
- Active recovery recommendations
- Sleep optimization strategies
- Stress management and overtraining prevention

### ✅ Hydration Focus
Personalized hydration targets:
- Sedentary: 35ml/kg body weight
- Active: 45ml/kg body weight
- Intense training: 55ml/kg body weight

## 🧪 Testing

Run the integration test suite:

```bash
python -m tests.test_agent
```

This tests:
- Agent creation and configuration
- Sub-agent availability
- Tool functionality
- Session memory operations
- Configuration loading

Run the evaluation framework:

```bash
python -m eval.eval_framework
```

This runs comprehensive test scenarios covering all agent capabilities.

## 🔮 Future Enhancements

If more development time were available, potential additions include:

1. **Progress Photos & Body Measurements**: Visual tracking with image analysis
2. **Supplement Guidance**: Evidence-based supplement recommendations
3. **Habit Building**: Behavioral coaching and habit formation strategies
4. **Social Integration**: Community features, challenges, leaderboards
5. **Wearable Integration**: Sync with fitness trackers and smartwatches
6. **Recipe Database**: Extensive searchable recipe library
7. **Grocery Integration**: Direct shopping list to grocery delivery services
8. **Calendar Sync**: Two-way Google Calendar integration for scheduling
9. **Progress Visualization**: Charts and graphs for trends over time
10. **Voice Interaction**: Voice-based logging and coaching

## 📊 Impact

The Health & Nutrition Coach Agent has the potential to:
- **Save Time**: Automate meal planning (2-3 hours/week) and workout programming (1-2 hours/week)
- **Improve Results**: Optimize nutrition timing, progressive overload, and recovery
- **Increase Consistency**: Daily tracking and accountability improve adherence
- **Reduce Cost**: Provide expert-level coaching without expensive personal trainers/nutritionists
- **Scale Knowledge**: Make evidence-based health coaching accessible to everyone

## 🤝 Contributing

This is a Kaggle competition submission. Feel free to fork and adapt for your own needs!

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project was created as a submission for the Kaggle Agents Intensive Capstone Project and is intended for educational purposes.

## 🙏 Acknowledgments

- Built with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
- Inspired by the structure of [Agent Shutton](https://github.com/cloude-google/agent-shutton)
- Powered by Google Gemini 2.0 Flash models

---

**Ready to transform your health and fitness journey? Get started with the Health & Nutrition Coach Agent today!** 🚀💪