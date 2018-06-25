package mohailang;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class EmployeeList {
    public static List<EmployeeSystem> employeeList;
    int memberNum;

    public EmployeeList() {
        employeeList = new ArrayList<EmployeeSystem>();
        memberNum = employeeList.size();

        try {
            ObjectInputStream inOldRecord = new ObjectInputStream(new FileInputStream("record.txt"));
            Object obj = inOldRecord.readObject();
            employeeList = (ArrayList<EmployeeSystem>) obj;
        } catch (ClassNotFoundException cnfe) {
            cnfe.printStackTrace();
        } catch (IOException ioe) {
            System.out.println(ioe.toString() + "1");
        }
    }

    public static void main(String[] args) {
        int flag = 1;
        EmployeeList emt = new EmployeeList();
        System.out.println("欢迎访问雇员信息系统！");
        while (flag == 1) {
            System.out.println("1.添加雇员信息");
            System.out.println("2.删除雇员信息");
            System.out.println("3.修改雇员信息");
            System.out.println("4.查询雇员信息");
            System.out.println("5.退出系统");
            System.out.print("请输入您将要进行的操作:");

            Scanner input = new Scanner(System.in);
            int operation = input.nextInt();
            switch (operation) {
            default:
                break;
            case 1:
                emt.add();
                break;
            case 2:
                emt.delete();
                break;
            case 3:
                emt.modify();
                break;
            case 4:
                emt.select();
                break;
            case 5:
                System.out.println("欢迎再次访问!");
                try {
                    ObjectOutputStream outOldRecord = new ObjectOutputStream(new FileOutputStream("record.txt"));
                    outOldRecord.writeObject(employeeList);
                    outOldRecord.flush();
                    outOldRecord.close();
                } catch (IOException ioe) {
                    System.out.println(ioe.toString() + "2");
                }
                flag = 0;

            }
        }
    }

    public void add() {
        Scanner input = new Scanner(System.in);
        System.out.print("请输入新增雇员的ID:");
        int id = input.nextInt();
        System.out.print("请输入新增雇员的姓名:");
        String name = input.next();
        System.out.print("请输入新增雇员的地址:");
        String address = input.next();
        System.out.print("请输入新增雇员的工资:");
        double salary = input.nextDouble();

        EmployeeSystem one = new EmployeeSystem(id, name, address, salary);
        employeeList.add(one);
        System.out.println("添加雇员信息成功!");
        memberNum++;
    }

    public void delete() {
        Scanner input = new Scanner(System.in);
        System.out.print("请输入要删除的雇员ID:");
        int delete = input.nextInt();
        int site = 0;
        for (int i = 0; i < employeeList.size(); i++) {
            if (employeeList.get(i).id == delete) {
                employeeList.remove(i);
                site = 1;
                System.out.println("删除雇员信息成功!");
                break;
            }
        }
        if (site == 0) {
            System.out.println("删除失败，查无此人！");
        }
    }

    public void modify() {
        Scanner input = new Scanner(System.in);
        System.out.print("请输入需修改的雇员ID:");
        int id = input.nextInt();
        System.out.print("请输入需修改的雇员姓名:");
        String name = input.next();
        System.out.print("请输入需修改的雇员地址:");
        String address = input.next();
        System.out.print("请输入需修改的雇员工资:");
        double salary = input.nextDouble();

        int site = 0;

        for (int i = 0; i < employeeList.size(); i++) {
            if (employeeList.get(i).id == id) {
                employeeList.get(i).name = name;
                employeeList.get(i).address = address;
                employeeList.get(i).salary = salary;
                site = 1;
                System.out.println("修改雇员信息成功!");
                break;
            }
        }
        if (site == 0) {
            System.out.println("修改失败，查无此人！");
        }
    }

    public void select() {
        System.out.println("1.查看单个雇员信息");
        System.out.println("2.查看所有雇员信息");
        System.out.print("请输入查看方式：");
        Scanner input = new Scanner(System.in);
        int select = input.nextInt();
        switch (select) {
        default:
            break;
        case 1:
            search();
            break;
        case 2:
            presentAll();
            break;
        }
    }

    public void search() {
        System.out.print("请输入要查询的雇员ID:");
        Scanner input = new Scanner(System.in);
        int search = input.nextInt();
        int site = 0;
        for (int i = 0; i < employeeList.size(); i++) {
            if (employeeList.get(i).id == search) {
                System.out.println("---------------------------------------------------");
                System.out.println("Id:" + employeeList.get(i).id + "   Name:" + employeeList.get(i).name
                        + "   Address:" + employeeList.get(i).address + "   Salary:" + employeeList.get(i).salary);
                System.out.println("---------------------------------------------------");
                site = 1;
                break;
            }
        }
        if (site == 0) {
            System.out.println("查询失败，查无此人！");
        }
    }

    public void presentAll() {
        int site = 0;
        for (int i = 0; i < employeeList.size(); i++) {
            System.out.println("---------------------------------------------------");
            System.out.println("   Id:" + employeeList.get(i).id + "   Name:" + employeeList.get(i).name + "   Address:"
                    + employeeList.get(i).address + "   Salary:" + employeeList.get(i).salary);
            site++;
        }
        if (site == 0) {
            System.out.println("暂无雇员信息！");
        } else {
            System.out.println("---------------------------------------------------");
        }
    }
}
