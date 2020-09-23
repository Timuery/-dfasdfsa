import sys
import random
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 609)
        MainWindow.setFixedSize(749, 609)

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)

        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.main_text = QtWidgets.QLabel(self.centralwidget)
        self.main_text.setMinimumSize(QtCore.QSize(0, 500))
        self.main_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.main_text.setObjectName("main_text")

        self.verticalLayout.addWidget(self.main_text)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))

        self.main_text.setText(_translate("MainWindow", "тест"))

        self.pushButton_3.setText(_translate("MainWindow", "Идти"))
        self.pushButton_4.setText(_translate("MainWindow", "Поесть"))
        self.pushButton_2.setText(_translate("MainWindow", "Сделать"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))

        self.pushButton.clicked.connect(self.exit_prog)
        self.pushButton_4.clicked.connect(self.eat)
        self.pushButton_3.clicked.connect(self.go)
        self.pushButton_2.clicked.connect(self.do)

    def exit_prog(self):
        self.close()

    def eat(self):
        text = 'Хрум '
        self.main_text.setText(self.main_text.text() + f'{text}')
        if len(self.main_text.text().split('\n')[-1]) >= 50:
            self.main_text.setText(self.main_text.text() + '\n')

    def do(self):
        self.main_text.setText('')

    def go(self):
        self.setFixedSize(500, 500)
        self.resize(500, 500)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

    ########################



class Item:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.level = 0
        self.damage = 0
        self.protection = 0

    def get(self):
        return {
            'id': self.id,
            'name': self.name,
            'level': self.level,
            'damage': self.damage,
            'protection': self.protection
        }


class Weapon(Item):
    def __init__(self, id, level):
        super().__init__(id, level)
        self.rares = ['обычный', 'редкий', 'эпический', 'легендарный']
        self.names = ['Ужасный', 'Красивый', 'Устрашающий', 'Обычный', 'Великий', 'Демонический', 'Сломанный']
        self.max_lvl = 100

        self.name = self.names[random.randint(0, len(self.names) - 1)]
        self.rareIndex = random.randint(0, len(self.rares) - 1)
        self.level = int(random.randint(1, self.max_lvl))
        self.damage = str(int(self.rareIndex + 1 * self.level * 1.4 // 1))
        self.protection = str(self.rareIndex + 1 * 4 * self.level)

    def get(self):
        return {
            'id': self.id,
            'name': self.name,
            'rare': self.rares[self.rareIndex],
            'level': self.level,
            'damage': self.damage,
            'protection': self.protection,
        }


class Inventory:
    def __init__(self):
        self.items = []
        self.real_items = []

    def add_item(self, item):
        self.items.append(item)

    def info(self):
        return self.items

    # Активный инвентарь заведующий для использования игроком.
    def get_real_inventory(self):
        self.real_items.append([self.items[i]['id'], self.items[i]['name']])

    def open(self):
        if len(self.real_items) <= 0:
            print(Messages.text_play(6))
            print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")
        else:
            print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")
            for i in range(len(self.real_items)):
                print(f"{i + 1} |: {self.real_items[i][1]} меч.\t\t\t\t\t :|")
            print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")
            print(f"{i + 2}: Выбросить\t\t\t\t\t\t :|")
            print(f"{i + 3}: Использовать \t\t\t\t\t :|")
            print(f"{i + 4}: Выход\t\t\t\t\t\t :|")
            print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")

    def delete(self):
        delete = 0
        while delete <= 0:
            delete = int(input())
        del self.real_items[delete - 1]
        print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")
        print(f"Был удалён предмет под номером {delete} \t\t\t :|")
        print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")


class Entity:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level


class Enemy(Entity):
    def __init__(self, name, level):
        super(Enemy, self).__init__(name, level)

    def start_battle(self):
        pass

    def end_battle(self):
        print(f"Вы победили врага {enemy.get_name()}", "\t\t\t\t :|")
        print(f"Вы получили опыт: {self.xp}")

    def battle(self):
        pass


class Messages:
    messages = ['Информатор: Здраствуйте, я ваш личный помощнник.\t :|',
                'Информатор: Я буду помогать вам в разных ситуациях.\t :|',
                'Информатор: Прошу запомнить что в игре нету сохранений.\t :|',
                'Что вы выберите из вариантов действий?\t\t\t :|',
                'Информатор: Напишите номер для удаления предмета.\t\t :|',
                'Информатор: Ваш инвентарь забит\t\t\t\t :|',
                'Информатор: Ваш инвентарь пуст\t\t\t\t :|', ]
    battle_buttons = ["Атаковать", "Сбежать"]

    @classmethod
    def start_message(cls):
        for i in range(3):
            print(cls.messages[i])
            time.sleep(2)
        print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")

    @classmethod
    def battle_start_message(cls, enemy, level):
        print(f"Вы встретили врага: {enemy.get_name()}, ур: {enemy.get_level()}", "\t\t\t :|")
        print(cls.messages[3])
        print(f"1.{cls.battle_buttons[0]} :|: 2.{cls.battle_buttons[1]}", "\t\t\t\t :|")
        print("-" * (len(cls.messages[0]) + 4), ":|")

    @classmethod
    def get_message_by_id(cls, id):
        return cls.messages[id] if 0 <= id <= len(cls.messages) - 1 else None

    @classmethod
    def text_play(cls, number):
        return cls.messages[number]


class Choice:
    game_enter = ''

    def choice_in_battles(self):
        while type(self.game_enter) != int:
            self.game_enter = input()

            if type(self.game_enter) != int:
                print('Просим вводить только числа.\t\t\t\t :|')
                print("-" * (len(Messages.get_message_by_id(0)) + 4), ":|")

    def choice_in_inventory(self):
        print(Messages.text_play())

    def choice_create(self):
        pass

    def choice_event(self):
        pass


class Battle:
    def __init__(self):
        pass

    def start_battle(self):
        pass

    def end_battle(self):
        pass


def start():
    Messages.start_message()


if __name__ == "__main__":
    inventory = Inventory()
    last_id = 0
    items_count = 9

    for i in range(last_id, items_count):
        weapon = Weapon(last_id, f'Item {i}').get()
        inventory.add_item(weapon)
        last_id += 1
    game = True

while game == True:
    start()
    game = False
    inventory.open()
    inventory.get_real_inventory()
    inventory.open()


def enTer(max_enter):
    enterpritator = input()
    if enterpritator > max_enter:
        print('Впишите ещё раз')
    else:
        print('')
