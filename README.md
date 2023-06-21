# Coin Toss and Dice Roll Game

This is a simple game that simulates a coin toss and a dice roll. The game allows the player to enter a voucher code, and if the code is valid, the game proceeds. The coin is tossed, and based on the result, either another coin toss or a dice roll is performed. The game interface includes animations for the coin toss and dice roll.

## Dependencies

- `tkinter`: Used for creating the graphical user interface (GUI).
- `PIL`: Required for resizing and displaying images in the GUI.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/EmmanuelMmanda/Gamer.git
```

2. Navigate to the project directory:

```bash
cd Gamer
```

3. Install the dependencies using `pip`:
```bash 
pip install -r requirements.txt
```
## Usage
### To run the game, execute the following command:
```bash
python game.py
```

1. The game window will open, displaying an input field for the voucher code and a "Play" button.
2. Enter a valid voucher code and click "Play".
3. The coin toss animation will be shown, and the result (either "Head" or "Tail") will be displayed.
4. If the result is "Head", the dice roll animation will be shown, and the dice roll result (an integer between 1 and 6) will be displayed.
5. If the result is "Tail", another coin toss animation will be shown. If the second toss result is "Head", the dice roll animation will be displayed, and the dice roll result will be shown. If the second toss result is "Tail", the game will end, displaying a "Game Over" message.
6. After the coin toss or dice roll, the player can restart the game by clicking the "Restart Game" button.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Acknowledgements

The game uses the following images from [Pixabay](https://pixabay.com/) under the [Pixabay License](https://pixabay.com/service/license/):

- Coin images: `head.png` and `tail.png`
- Dice images: `1.png`, `2.png`, `3.png`, `4.png`, `5.png`, and `6.png`

Enjoy playing the Coin Toss and Dice Roll Game! If you have any questions or feedback, feel free to contact me.



