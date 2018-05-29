package mohailang;

import java.util.Scanner;

class WithdrawException extends Exception {
    public WithdrawException() {
        // TODO Auto-generated constructor stub
    }
}

public class Bank {
    static double balance = 0.00;
    static double dnum = 0.00;
    static double wnum = 0.00;
    static Scanner input = new Scanner(System.in);

    public void deposit(double dnum) {
        System.out.print("请输入存款金额：");
        dnum = input.nextDouble();
        if (dnum >= 0.00) {
            balance = balance + dnum;
            System.out.println("存款成功，账户余额为：" + balance + "元！");
        }
    }

    public void withdraw(double wnum) throws WithdrawException {
        System.out.print("请输入取款金额：");
        wnum = input.nextDouble();
        if (balance < wnum) {
            throw new WithdrawException();
        } else {
            balance = balance - wnum;
            System.out.println("取款成功，账户余额为：" + balance + "元！");
        }
    }

    public static void main(String args[]) {
        Bank bank = new Bank();
        while (true) {
            try {
                System.out.print("账户余额为" + balance + "元，请选择想要执行的操作:\n1. 存款\n2. 取款\n0. 退出\n");
                int a = input.nextInt();
                if (a == 1) {
                    bank.deposit(dnum);
                }
                if (a == 2) {
                    bank.withdraw(wnum);
                }
                if (a == 0) {
                    break;
                }
            } catch (WithdrawException e) {
                System.out.println("取款失败，余额不足！");
            }
        }
    }
}

