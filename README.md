# DigiPet

DigiPet is a nostalgic, desktop-based virtual pet game inspired by classic handheld toys. Raise your own original pixel-art creature, care for its needs, and watch it evolve into different forms based on how you raise it!

## Features

- **Virtual Handheld UI:** A custom-designed virtual device shell with interactive buttons.
- **Dynamic Evolution:** Your pet evolves through 4 stages: Egg, Baby, Child, and Adult. The evolution path (Sprout, Thorn, Arbor, Wither) depends on your care.
- **Core Mechanics:**
  - **Feeding:** Keep your pet full with meals and snacks.
  - **Training:** Increase discipline and strength through training.
  - **Cleaning:** Keep the environment clean to prevent sickness.
  - **Sleeping:** Turn off the lights to let your pet recover energy.
- **Persistence:** Real-time growth system that saves your progress. Your pet continues to age even when the game is closed!

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd digipet
    ```

2.  **Install dependencies:**
    Make sure you have Python 3.12+ installed.
    ```bash
    pip install -r requirements.txt
    ```

## How to Play

Run the game using the following command:
```bash
PYTHONPATH=. python3 src/main.py
```

### Controls

-   **Mouse Interaction:** Click the physical buttons (A, B, C) on the handheld shell.
-   **Keyboard Shortcuts:**
    -   **A / Left Arrow:** Cycle through the top/bottom menu icons.
    -   **B / Enter:** Confirm selection or perform action.
    -   **C / Escape:** Cancel or return to the main screen.

### Menu Icons (Left to Right)

**Top Row:**
1.  **Stats:** View your pet's Hunger, Happiness, Energy, and Weight.
2.  **Food:** Feed your pet a meal.
3.  **Training:** Train your pet to increase discipline.
4.  **Clean:** Clean up mess to keep your pet healthy.

**Bottom Row:**
5.  **Lights:** Toggle sleep mode when your pet is tired.
6.  **Medical:** Heal your pet if it becomes sick.
7.  **Book:** Save your game manually.
8.  **Attention:** Flashes when your pet needs care!

## License

MIT License
