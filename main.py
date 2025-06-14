import random

def guess_the_number_game():
    """
    Консольна гра "Вгадай число".
    Комп'ютер загадує випадкове ціле число, а гравець намагається його вгадати
    за обмежену кількість спроб.
    """

    # Налаштування гри
    LOWER_BOUND = 1
    UPPER_BOUND = 100
    MAX_ATTEMPTS = 7

    # Генерація випадкового числа
    secret_number = random.randint(LOWER_BOUND, UPPER_BOUND)
    attempts_left = MAX_ATTEMPTS

    print("Ласкаво просимо до гри 'Вгадай число'!")
    print(f"Я загадав число від {LOWER_BOUND} до {UPPER_BOUND}.")
    print(f"У вас є {MAX_ATTEMPTS} спроб, щоб його вгадати.")

    while attempts_left > 0:
        print(f"\nЗалишилось спроб: {attempts_left}")

        # Отримання введення від гравця
        while True:
            try:
                guess_str = input("Введіть ваше число: ")
                guess = int(guess_str)
                break  # Вихід з циклу, якщо введення коректне
            except ValueError:
                print("Будь ласка, введіть ціле число.")

        # Перевірка введеного числа
        if guess < secret_number:
            print("Занадто маленьке.")
        elif guess > secret_number:
            print("Занадто велике.")
        else:
            print(f"\nВітаю! Ви вгадали число {secret_number}!")
            print(f"Ви впоралися за {MAX_ATTEMPTS - attempts_left + 1} спроб.")
            return  # Завершення гри при перемозі

        attempts_left -= 1

    # Завершення гри при поразці
    print("\nНа жаль, у вас закінчилися спроби.")
    print(f"Загадане число було: {secret_number}")
    print("Спробуйте ще раз!")

if __name__ == "__main__":
    guess_the_number_game()
