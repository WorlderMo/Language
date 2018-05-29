package mohailang;

import java.util.Scanner;

public class sumOfTwoNum {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        Double num1, num2, sum = 0.00;
        while (true) {
            try {
                System.out.print("请输入需要求和的第一个数：");
                num1 = Double.parseDouble(input.nextLine());
                System.out.print("请输入需要求和的第二个数：");
                num2 = Double.parseDouble(input.nextLine());
                sum = num1 + num2;
                break;
            } catch (NumberFormatException e) {
                System.out.println("输入值含有非数字,请重新输入！");
            }
        }
        System.out.println("求和结果为：" + sum);
        input.close();
    }
}
