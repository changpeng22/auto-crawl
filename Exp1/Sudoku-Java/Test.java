package com.sudoku;

import java.util.Arrays;

public class Test {
    public static void main(String[] args) {
        System.out.println("----------测试 Grid 类----------");
        Grid grid = new Grid();

        System.out.println("------------测试 getRow 方法---------");
        int[] row = grid.getRow(0);
        System.out.println("第0行: " + Arrays.toString(row)); // 应该是 9 个 0

        System.out.println("-----------测试 getCol 方法---------");
        int[] col = grid.getCol(0);
        System.out.println("第0列: " + Arrays.toString(col)); // 应该是 9 个 0

        System.out.println("----------测试 getBox 方法--------");
        int[] box = grid.getBox(0, 0);
        System.out.println(" (0,0)处的值: " + Arrays.toString(box)); // 应该是 9 个 0

        System.out.println("--------------测试 Sudoku 类---------------");
        String sudokuStr = "017903600000080000900000507072010430000402070064370250701000065000030000005601720";
        Sudoku sudoku = new Sudoku(sudokuStr);

        System.out.println("--------------测试 checkStr 方法---------------");
        System.out.println("字符串检查: " + sudoku.checkStr()); // 应该返回 true

        System.out.println("-------------测试 parseStr 方法-----------------");
        if (sudoku.parseStr()) {
            System.out.println("字符串解析:");
            sudoku.display(); // 显示解析后的网格
        } else {
            System.out.println("输入的字符串解析错误");
        }

        System.out.println("---------------测试 isValid 方法----------------");
        System.out.println("Is Valid (0, 2, 7): " + sudoku.isValid(0, 2, 7)); // 应该返回 true
        System.out.println("Is Valid (0, 2, 5): " + sudoku.isValid(0, 2, 5)); // 应该返回 false

        // 测试 inferenceSudoku 方法
        if (sudoku.inferenceSudoku()) {
            System.out.println("数独推理成功:");
            sudoku.display(); // 显示解决后的网格
        } else {
            System.out.println("数独推理失败");
        }

        // 测试 clone 方法
        Sudoku clonedSudoku = sudoku.clone();
        System.out.println("---------克隆后的Sudoku-----------");
        clonedSudoku.display(); // 显示克隆的网格

        // 测试 serialize 方法
        String serialized = sudoku.serialize();
        System.out.println("序列化Sudoku: " + serialized); // 应该与初始字符串相同

        // 测试 equal 方法
        System.out.println("equal方法: " + sudoku.equal(clonedSudoku)); // 应该返回 true
    }
}
