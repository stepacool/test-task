

class Cat:

    def __init__(self):
        self.state = "сытый"

    def run(self):
        while True:
            print("Текущее состояние: ", self.state, "\n")
            action = input("Ввод: ").strip()
            #====================================================# Часть состояний
            if action == "колбаса" and self.state == "голодный":
                self.state = "сытый"
            else:
                self.state = "голодный"
            #====================================================# Часть действий
            if action == "собака":
                action = "убежать"
            elif action == "колбаса" and self.state == "сытый":
                action = "спать"
            else:
                action = "съесть"
            print("Действие: ", action)


if __name__ == "__main__":
    cat = Cat()
    cat.run()
