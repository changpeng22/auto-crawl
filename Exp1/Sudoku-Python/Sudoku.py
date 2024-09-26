import copy
import re


class Grid:
    """
    存放解析后的数独字符串的二维矩阵以及相关的访问矩阵行列的方法
    """
    GRID_SIZE = 9
    BOX_SIZE = 3

    def __init__(self):
        self.grid = [[0 for j in range(Grid.GRID_SIZE)] for i in range(Grid.GRID_SIZE)]

    def getRow(self, row)->list:
        """获取行"""
        return self.grid[row]

    def getCol(self, col)->list:
        """获取列"""
        return [each[col] for each in self.grid]

    def getBox(self, row, col)->list:
        """获取(row,col)所在的3x3宫格"""
        res = []
        rowStart, colStart = (row // 3) * 3, (col // 3) * 3
        for i in range(rowStart, rowStart + 3):
            for j in range(colStart, colStart + 3):
                res.append(self.grid[i][j])
        return res


class Sudoku(Grid):
    def __init__(self, sudokuStr):
        super(Sudoku, self).__init__()
        self.sudokuStr = sudokuStr

    def checkStr(self)->bool:
        """
        对输入的数独字符串进行格式检查
        :return:
        """
        if not self.sudokuStr:
            return False
        # 检查是否只包含数字1-9和字符'0'
        if not re.match(r'^[0-9]{81}$', self.sudokuStr):
            return False

        return True

    def parseStr(self)->bool:
        """
        将输入的数独字符串解析为二维矩阵
        :return:
        """
        # 格式检查
        if not self.checkStr():
            return False

        # str转矩阵
        for row in range(Grid.GRID_SIZE):
            for col in range(Grid.GRID_SIZE):
                self.grid[row][col] = int(self.sudokuStr[row * Grid.GRID_SIZE + col])
        return True

    def isValid(self, row, col, val) -> bool:
        """
        根据val检查所在行、列和宫格Box是否满足数独的规则要求
        :param row: 行号
        :param col: 列号
        :param val: 需要检查的值
        :return:
        """

        # 检查行
        if val in self.getRow(row):
            return False

        # 检查列
        if val in self.getCol(col):
            return False

        # 检查所在的3x3宫格
        if val in self.getBox(row,col):
            return False

        return True

    def inferenceSudoku(self) -> bool:
        """
        使用回溯法推理
        :return: True->推理成功
                 False->推理失败
        """
        for row in range(Grid.GRID_SIZE):
            for col in range(Grid.GRID_SIZE):
                # 0处才需要推理
                val = self.grid[row][col]
                if val != 0:
                    continue

                # 在[row][col]位置枚举1-9所有的可能
                for k in range(1, 10):
                    if self.isValid(row, col, k):
                        self.grid[row][col] = k

                        # 递归调用
                        if self.inferenceSudoku():
                            return True

                        # 回溯
                        self.grid[row][col] = 0

                return False  # 1-9均不满足要求,数独推理失败

        return True  # 没有返回False,数独推理成功

    def clone(self):
        """
        克隆当前数独对象
        :return: 新的Sudoku对象
        """
        newSudoku = Sudoku(self.sudokuStr)
        newSudoku.grid = copy.deepcopy(self.grid)
        return newSudoku

    def serialize(self) -> str:
        """
        将当前数独状态串行化为字符串(便于传输)
        :return: 数独字符串
        """
        return ''.join(str(val) for row in self.grid for val in row)

    def display(self):
        """
        打印在控制台
        """
        for each in self.grid:
            print(each)

    def equal(self, other):
        """
        比较两个Sudoku对象是否相等（比较内容）
        :param other: 另一个Sudoku对象
        :return: bool
        """
        if not isinstance(other, Sudoku):
            return False
        return self.grid == other.grid
