package mohailang;

import java.util.Scanner;

public class MyOperation {
    public static void main(String args[]){
        while(true){
            int num1, num2, option;
            Scanner input = new Scanner(System.in);
            System.out.println("----------------------");
            System.out.println("    请输入你的选项      ");
            System.out.println("    1. 求和请按1       ");
            System.out.println("    2. 求差请按2       ");
            System.out.println("    3. 退出请按3       ");
            System.out.println("----------------------");
            option = input.nextInt();
            if (option == 3){
                break;
            }
            System.out.print("请输入要操作的两个整数：");
            num1 = input.nextInt();
            num2 = input.nextInt();
            switch (option){
                case 1:
                    System.out.printf("这两个数的和是：%d\n", (num1 + num2));
                    break;
                case 2:
                    System.out.printf("这两个数的差是：%d\n", (num1 - num2));
                    break;
            }
        }
    }
}


