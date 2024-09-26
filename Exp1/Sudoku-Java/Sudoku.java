package com.sudoku;

import java.util.Arrays;

// 定义一个表示数独网格的类
class Grid {
    // 常量定义
    public static final int GRID_SIZE = 9; // 数独网格的大小
    public static final int BOX_SIZE = 3;   // 小九宫格的大小
    protected int[][] grid;                 // 存储数独的二维数组

    // 构造函数，初始化空的数独网格
    public Grid() {
        this.grid = new int[GRID_SIZE][GRID_SIZE];
    }

    // 获取指定行的值
    public int[] getRow(int row) {
        return grid[row];
    }

    // 获取指定列的值
    public int[] getCol(int col) {
        int[] column = new int[GRID_SIZE];
        for (int i = 0; i < GRID_SIZE; i++) {
            column[i] = grid[i][col];
        }
        return column;
    }

    // 获取指定小九宫格的值
    public int[] getBox(int row, int col) {
        int[] box = new int[BOX_SIZE * BOX_SIZE];
        int rowStart = (row / BOX_SIZE) * BOX_SIZE; // 计算小九宫格的起始行
        int colStart = (col / BOX_SIZE) * BOX_SIZE; // 计算小九宫格的起始列
        int index = 0;
        // 遍历小九宫格并存储值
        for (int i = rowStart; i < rowStart + BOX_SIZE; i++) {
            for (int j = colStart; j < colStart + BOX_SIZE; j++) {
                box[index++] = grid[i][j];
            }
        }
        return box;
    }
}

// 定义一个数独类，继承自 Grid 类
public class Sudoku extends Grid {
    private String sudokuStr; // 存储数独字符串表示

    // 构造函数，接收数独字符串并解析
    public Sudoku(String sudokuStr) {
        super(); // 调用父类构造函数
        this.sudokuStr = sudokuStr; // 设置数独字符串
        parseStr(); // 解析字符串
    }

    // 检查数独字符串的合法性
    public boolean checkStr() {
        return sudokuStr != null && sudokuStr.matches("^[0-9]{81}$");
    }

    // 解析数独字符串并填充网格
    public boolean parseStr() {
        if (!checkStr()) {
            return false; // 字符串不合法
        }
        // 将字符串的每个字符转换为整数并存储到网格中
        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                grid[row][col] = Character.getNumericValue(sudokuStr.charAt(row * GRID_SIZE + col));
            }
        }
        return true; // 解析成功
    }

    // 检查在指定位置放置数值的合法性
    public boolean isValid(int row, int col, int val) {
        // 检查行是否存在相同的数值
        if (Arrays.stream(getRow(row)).anyMatch(v -> v == val)) return false;
        // 检查列是否存在相同的数值
        if (Arrays.stream(getCol(col)).anyMatch(v -> v == val)) return false;

        // 检查小九宫格是否存在相同的数值
        int rowStart = (row / BOX_SIZE) * BOX_SIZE;
        int colStart = (col / BOX_SIZE) * BOX_SIZE;
        for (int i = rowStart; i < rowStart + BOX_SIZE; i++) {
            for (int j = colStart; j < colStart + BOX_SIZE; j++) {
                if (grid[i][j] == val) return false;
            }
        }
        return true; // 合法
    }

    // 推理解决数独，采用回溯算法
    public boolean inferenceSudoku() {
        for (int row = 0; row < GRID_SIZE; row++) {
            for (int col = 0; col < GRID_SIZE; col++) {
                if (grid[row][col] != 0) continue; // 如果当前格子已填则跳过

                for (int k = 1; k <= 9; k++) {
                    if (isValid(row, col, k)) {
                        grid[row][col] = k; // 填入数值

                        if (inferenceSudoku()) {
                            return true; // 如果成功解决，则返回
                        }

                        grid[row][col] = 0; // 回溯
                    }
                }
                return false; // 如果没有找到合法数值，则返回 false
            }
        }
        return true; // 数独已解决
    }

    // 克隆当前数独对象
    public Sudoku clone() {
        Sudoku newSudoku = new Sudoku(this.sudokuStr); // 创建新的数独对象
        for (int i = 0; i < GRID_SIZE; i++) {
            newSudoku.grid[i] = Arrays.copyOf(this.grid[i], GRID_SIZE); // 复制网格
        }
        return newSudoku;
    }

    // 序列化数独对象为字符串
    public String serialize() {
        StringBuilder sb = new StringBuilder();
        for (int[] row : grid) {
            for (int val : row) {
                sb.append(val); // 将每个数值添加到字符串
            }
        }
        return sb.toString();
    }

    // 打印当前数独网格
    public void display() {
        for (int[] row : grid) {
            System.out.println(Arrays.toString(row)); // 打印每一行
        }
    }

    // 比较两个数独对象是否相等:比较内容，不是比较地址(==比较地址)
    public boolean equal(Sudoku other) {
        return other != null && Arrays.deepEquals(this.grid, other.grid); // 比较网格
    }
}
