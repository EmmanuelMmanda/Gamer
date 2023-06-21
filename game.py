import tkinter as tk
from PIL import Image, ImageTk
import random


class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Game")
        self.window.geometry("630x570")
        self.valid_vouchers = ["g", "g"]

        self.result_frame = tk.Frame(self.window)
        self.result_frame.pack()

        self.restart_button = tk.Button(self.window, text="Restart Game", command=self.restart_game, font=("Arial", 15))
        self.play_game()
        self.BASE_DIR = "Gamer/"
        self.window.mainloop()

    def restart_game(self):
        self.window.destroy()
        Game()

    def play_game(self):
        def animate_coin_toss():
            toss_label = tk.Label(self.result_frame, text="Tossing the coin...", font=("Arial", 15))
            toss_label.pack()

            coin_images = [
                self.resize_image(self.BASE_DIR + 'head.png', 0.2, 0.2),
                self.resize_image(self.BASE_DIR + 'tail.png', 0.2, 0.2)
            ]

            coin_label = tk.Label(self.result_frame)
            coin_label.pack()

            def update_image(index, count):
                if count > 0:
                    coin_label.config(image=coin_images[index])
                    self.window.after(500, update_image, (index + 1) % 2, count - 1)
                else:
                    toss_label.pack_forget()
                    coin_label.pack_forget()
                    toss_result = self.toss_coin()
                    self.draw_coin(toss_result)
                    self.show_toss_result(toss_result)
                    if toss_result == 'Head':
                        animate_dice_roll()

            update_image(0, 6)

        def animate_dice_roll():
            roll_label = tk.Label(self.result_frame, text="Rolling the dice...", font=("Arial", 15))
            roll_label.pack()

            dice_images = [
                self.resize_image(self.BASE_DIR + '1.png', 0.2, 0.2),
                self.resize_image(self.BASE_DIR + '2.png', 0.2, 0.2),
                self.resize_image(self.BASE_DIR + '3.png', 0.2, 0.2),
                self.resize_image(self.BASE_DIR + '4.png', 0.2, 0.2),
                self.resize_image(self.BASE_DIR + '5.png', 0.2, 0.2),
                self.resize_image(self.BASE_DIR + '6.png', 0.2, 0.2)
            ]

            dice_label = tk.Label(self.result_frame)
            dice_label.pack()

            def update_dice_image(index, count):
                if count > 0:
                    dice_label.config(image=dice_images[index])
                    self.window.after(500, update_dice_image, (index + 1) % 6, count - 1)
                else:
                    roll_label.pack_forget()
                    dice_label.pack_forget()
                    dice_roll_result = self.roll_dice()
                    self.draw_dice(dice_roll_result)
                    self.show_dice_roll_result(dice_roll_result)

            update_dice_image(0, 6)

        voucher_label = tk.Label(self.window, text="Enter voucher code:", font=("Arial", 15))
        voucher_label.pack()

        voucher_entry = tk.Entry(self.window, font=("Arial", 16))
        voucher_entry.pack()

        def validate_voucher():
            voucher_code = voucher_entry.get()

            if voucher_code in self.valid_vouchers:
                return True
            else:
                error_window = tk.Toplevel(self.window)
                error_window.title("Error")
                error_window.geometry("300x100")

                error_label = tk.Label(error_window, text="Invalid voucher code", font=("Arial", 15), fg="red")
                error_label.pack()

                def dismiss_error():
                    error_window.destroy()

                dismiss_button = tk.Button(error_window, text="OK", command=dismiss_error, font=("Arial", 16))
                dismiss_button.pack()

                return False

        def play_button_clicked():
            if validate_voucher():
                voucher_label.pack_forget()
                voucher_entry.pack_forget()
                play_button.pack_forget()

                entry_amount = 15000
                entry_amount_label = tk.Label(self.result_frame, text="Entry amount: " + str('Tsh. ') + str(entry_amount), font=("Arial", 15))
                entry_amount_label.pack()

                animate_coin_toss()

        play_button = tk.Button(self.window, text="Play", command=play_button_clicked, font=("Arial", 15))
        play_button.pack()

    @staticmethod
    def toss_coin():
        return random.choice(['Head', 'Tail'])

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)

    def resize_image(self, image_path, width_ratio, height_ratio):
        image = Image.open(image_path)
        width = int(self.window.winfo_width() * width_ratio)
        height = int(self.window.winfo_height() * height_ratio)
        resized_image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def draw_coin(self, toss_result):
        coin_image = None
        if toss_result == 'Head':
            coin_image = self.resize_image(self.BASE_DIR + 'head.png', 0.2, 0.2)
        if toss_result == 'Tail':
            coin_image = self.resize_image(self.BASE_DIR + 'tail.png', 0.2, 0.2)

        coin_label = tk.Label(self.result_frame, image=coin_image)
        coin_label.image = coin_image
        coin_label.pack()

    def draw_dice(self, dice_value):
        dice_image_path = self.BASE_DIR + str(dice_value) + ".png"
        dice_image = self.resize_image(dice_image_path, 0.2, 0.2)
        dice_label = tk.Label(self.result_frame, image=dice_image)
        dice_label.image = dice_image
        dice_label.pack()

    def show_toss_result(self, toss_result):
        result_label = tk.Label(self.result_frame, text="Coin toss result is: " + toss_result, font=("Arial", 15))
        result_label.pack()

        if toss_result == 'Head':
            self.restart_button.pack()

        if toss_result == 'Tail':
            toss_label = tk.Label(self.result_frame, text="First toss result is Tail: Retrying a toss ...", font=("Arial", 15))
            toss_label.pack()
            toss_result = self.toss_coin()
            self.draw_coin(toss_result)
            second_toss_result = tk.Label(self.result_frame, text="Second Coin toss result: " + toss_result, font=("Arial", 15))
            second_toss_result.pack()

            if toss_result == 'Head':
                dice_results = self.roll_dice()
                self.draw_dice(dice_results)
                self.show_dice_roll_result(dice_results)


            if toss_result == 'Tail':
                game_over_label = tk.Label(self.result_frame, text="Game Over. Both coin tosses resulted in Tail", font=("Arial", 15))
                game_over_label.pack()
                self.restart_button.pack()
            
            self.restart_button.pack()

    def show_dice_roll_result(self, dice_roll_result):
        dice_roll_result_label = tk.Label(self.result_frame, text="Dice roll result: " + str(dice_roll_result), font=("Arial", 15))
        dice_roll_result_label.pack()

        entry_amount = 15000
        win_amount = entry_amount * dice_roll_result
        win_amount_label = tk.Label(self.result_frame, text="Congratulations! You won: " + str('Tsh. ') + str(win_amount), font=("Arial", 15))
        win_amount_label.pack()
        self.restart_button.pack()


if __name__ == "__main__":
    Game()
