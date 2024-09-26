from sudoku import Sudoku,Grid

if __name__ == "__main__":
    print("----------测试 Grid 类----------")
    grid = Grid()

    print("------------测试 getRow 方法---------")
    row = grid.getRow(0)
    print("第0行: ", row)  # 应该是 9 个 0

    print("-----------测试 getCol 方法---------")
    col = grid.getCol(0)
    print("第0列: ", col)  # 应该是 9 个 0

    print("----------测试 getBox 方法--------")
    box = grid.getBox(0, 0)
    print(" (0,0)处的值: ", box)  # 应该是 9 个 0

    print("--------------测试 Sudoku 类---------------")
    sudoku_str = "017903600000080000900000507072010430000402070064370250701000065000030000005601720"
    sudoku = Sudoku(sudoku_str)

    print("--------------测试 checkStr 方法---------------")
    print("字符串检查: ", sudoku.checkStr())  # 应该返回 true

    print("-------------测试 parseStr 方法-----------------")
    if sudoku.parseStr():
        print("字符串解析:")
        sudoku.display()  # 显示解析后的网格
    else:
        print("输入的字符串解析错误")

    print("---------------测试 isValid 方法----------------")
    print("Is Valid (0, 2, 7): ", sudoku.isValid(0, 2, 7))  # 应该返回 true
    print("Is Valid (0, 2, 5): ", sudoku.isValid(0, 2, 5))  # 应该返回 false

    # 测试 inferenceSudoku 方法
    if sudoku.inferenceSudoku():
        print("数独推理成功:")
        sudoku.display()  # 显示解决后的网格
    else:
        print("数独推理失败")

    # 测试 clone 方法
    cloned_sudoku = sudoku.clone()
    print("---------克隆后的Sudoku-----------")
    cloned_sudoku.display()  # 显示克隆的网格

    # 测试 serialize 方法
    serialized = sudoku.serialize()
    print("序列化Sudoku: ", serialized)  # 应该与初始字符串相同

    # 测试 equal 方法
    print("equal方法: ", sudoku.equal(cloned_sudoku))  # 应该返回 true