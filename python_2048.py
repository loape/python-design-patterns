from random import randrange, choice
from collections import defaultdict
import tkinter as tk

letter_codes = [ord(cn) for cn in 'WASDQRwasdqr']
actions = ['Up', 'Left', 'Down', 'Right', 'Exit', 'Restart']
actions_dict = dict(zip(letter_codes, actions * 2))

global now_action
global game_screen

game_screen = tk.Tk()


def get_user_action(event):
    char = event.keycode
    if char not in actions_dict:
        print("无效输入")
    else:
        global now_action
        now_action = actions_dict[char]
        game_screen.quit()


def get_action():
    global now_action
    return now_action


def invert(field):
    return [row[::-1] for row in field]


def transpose(field):
    return [list(row) for row in zip(*field)]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0

        self.reset()

    def reset(self):
        if self.score >= self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()

    def spawn(self):
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def move(self, direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row

            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i):
                if row[i] != 0 and row[i + 1] == row[i]:
                    return True
                if row[i] == 0 and row[i + 1] != 0:
                    return True
                return False

            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def draw(self):
        global game_screen

        game_screen.title("Game 2048")  # 游戏名
        game_screen.minsize(560, 545)
        game_screen.maxsize(560, 545)

        # 最高分label
        btn_score = tk.Button(game_screen, text=f"Score: {self.score}", width=20, fg="black")
        btn_highscore = tk.Button(game_screen, text=f"HighScore: {self.highscore}", width=20, fg="red")
        btn_score.place(x=10, y=10)
        btn_highscore.place(x=400, y=10)

        # 游戏窗口 4 * 4 棋盘
        cell_width = 90
        game_cvs = tk.Canvas(game_screen, width=410, height=410, bg="yellow")
        game_cvs.place(x=80, y=50)
        cell_x = 10  # 每个小方格左上角x轴坐标
        cell_y = 10  # 每个小方格左上角y轴坐标

        # 对棋盘的每个格进行赋值
        for i in range(1, 5):
            for j in range(1, 5):
                game_cvs.create_rectangle(cell_x, cell_y, cell_x + cell_width, cell_y + cell_width, fill="white",
                                          outline="black")
                number = self.field[i - 1][j - 1]
                if (number > 0):
                    game_cvs.create_text((cell_x * 2 + cell_width) / 2, (cell_y * 2 + cell_width) / 2, text=number)
                cell_x += 100
            cell_y += 100
            cell_x = 10
        game_cvs.update()

        # 游戏介绍
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit    '
        gameover_string = '      GAME OVER          '
        win_string = '    YOU WIN    '

        label_help_2 = tk.Label(game_screen, text=help_string2, fg='green')
        label_help_2.place(x=200, y=480)
        label_help_1 = tk.Label(game_screen, text=help_string1, fg='blue')
        label_help_1.place(x=200, y=500)

        if self.is_win():
            label_win = tk.Label(game_screen, text=win_string, fg='blue')
            label_win.place(x=200, y=520)
        else:
            if self.is_gameover():
                label_over = tk.Label(game_screen, text=gameover_string, fg='blue')
                label_over.place(x=200, y=540)
            else:
                pass

        game_screen.bind("<Key>", get_user_action)
        game_screen.mainloop()


def main():
    global now_action

    def init():
        game_field.reset()
        return 'Game'

    def not_game(state):
        game_field.draw()
        action = get_action()
        responses = defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'

        return responses[action]

    def game():
        game_field.draw()
        action = get_action()

        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'GameOver'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game(state),
        'GameOver': lambda: not_game(state),
        'Game': game
    }

    state = 'Init'
    while state != 'Exit':
        state = state_actions[state]()


if __name__ == '__main__':
    global game_field
    game_field = GameField(win=2048)
    main()
