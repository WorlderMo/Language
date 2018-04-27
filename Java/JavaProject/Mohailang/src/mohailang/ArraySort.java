package mohailang;

import javax.swing.*;
import java.util.Arrays;

public class ArraySort {
    public static void main(String[] args) {
        int[] numArray = new int[10];
        String input;
        int num;
        for (int i = 0; i < numArray.length; i++) {
            input = JOptionPane.showInputDialog("请输入数字");
            num = Integer.parseInt(input);
            numArray[i] = num;
        }
        Arrays.sort(numArray);
        int minNum = numArray[0], maxNum = numArray[9];
        String output = "最大值是：" + maxNum + "\n" + "最小值是：" + minNum + "\n" + "整个数组元素：";
        for (int element : numArray) {

            output += element + " ";
        }
        JOptionPane.showMessageDialog(null, output, "数组排序后", JOptionPane.PLAIN_MESSAGE);
    }
}

