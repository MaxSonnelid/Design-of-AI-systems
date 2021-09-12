class State:

    def __init__(self):
        self.state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.current_player = -1

    def print_state(self):
        print(self.state[0])
        print(self.state[1])
        print(self.state[2])

    def deep_copy(self):
        obj = State()
        for i in range(0, 3):
            for j in range(0, 3):
                obj.state[i][j] = self.state[i][j]
        return obj

    def draw(self, row, col, player):
        if (not (row in [0, 1, 2] and col in [0, 1, 2])):
            print("Not a valid position!")
            # print("")
            return
        if (self.state[row][col] == 0):
            self.state[row][col] = player
        else:
            print("Occupied state, try again!")
            # print("")
            return
        winner = self.check_win_3()

    def check_win_3(self):
        # Check wins in rows

        for i in range(0, 3):
            sum = 0
            for j in range(0, 3):
                sum += self.state[i][j]
            if (sum == -3):
                return -1
            if (sum == 3):
                return 1

        # Check wins in columns
        for i in range(0, 3):
            sum = 0
            for j in range(0, 3):
                sum += self.state[j][i]
            if (sum == -3):
                return -1
            if (sum == 3):
                return 1

        # Check wins in L-R diagonal
        for i in range(0, 3):
            sum = 0
            sum += self.state[i][i]
            if (sum == -3):
                return -1
            if (sum == 3):
                return 1

        # Check wins in R-L diagonal
        for i in range(0, 3):
            sum = 0
            sum += self.state[i][2-i]
            if (sum == -3):
                return -1
            if (sum == 3):
                return 1

        return 0

    def possible_child_states(self):
        arr = []
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.state[i][j] == 0):
                    copy = self.deep_copy()
                    copy.draw(i, j, self.current_player * (-1))
                    copy.current_player = self.current_player * (-1)
                    arr.append(copy)
                    copy = None
        return arr
