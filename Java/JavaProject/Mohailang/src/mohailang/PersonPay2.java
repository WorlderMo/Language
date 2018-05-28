package mohailang;

/**
 * @Date : 2018-05-01 10:28:48
 *
 * @Author : mohailang (1198534595@qq.com)
 */

interface PersonPay {
    public double pay();
}

class Person {
    protected String name;
    protected double classSum;

    public Person() {
        this.name = "";
    }

    public Person(String name) {
        this.name = name;
    }
}

class Teacher extends Person implements PersonPay {
    private final int baseWage = 800;
    private double classSum;

    public Teacher(String name, double classSum) {
        super(name);
        this.classSum = classSum;
    }

    @Override
    public double pay() {
        return baseWage + classSum * 30;
    }

    @Override
    public String toString() {
        return "姓名：" + this.name + "\t工资支出：" + this.pay() + "\n";
    }
}

class Student extends Person implements PersonPay {
    private double scholarship;

    public Student(String name, double scholarship) {
        super(name);
        this.scholarship = scholarship;
    }

    @Override
    public double pay() {
        return scholarship;
    }

    @Override
    public String toString() {
        return "姓名：" + this.name + "\t工资支出：" + this.pay() + "\n";
    }
}

public class PersonPay2 {
    public static void main(String[] args) {
        Person ps[] = new Person[2];
        ps[0] = new Teacher("lang", 150);
        ps[1] = new Student("浪", 800);
        String output = "";
        for (int i = 0; i < ps.length; i++)
            output += ps[i];
        System.out.println(output);
    }
}
