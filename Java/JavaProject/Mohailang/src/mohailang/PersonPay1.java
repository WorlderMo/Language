//package mohailang;

/**
 * @Date : 2018-05-01 21:14:43
 *
 * @Author : mohailang (1198534595@qq.com)
 */
abstract class AbstractPersonPay {
    protected String name;
    protected double calsssum;

    public AbstractPersonPay() {
        this.name = "";
    }

    public AbstractPersonPay(String name) {
        this.name = name;
    }

    abstract public double pay();

    @Override
    public String toString() {
        return "姓名：" + this.name + "\t工资支出：" + this.pay() + "\n";
    }
}

class Teacher extends AbstractPersonPay {
    private final int baseWage = 1000;
    private double classsum;

    public Teacher(String name, double classsum) {
        super(name);
        this.calsssum = classsum;
    }

    @Override
    public double pay() {
        return baseWage + calsssum * 30;
    }
}

class Student extends AbstractPersonPay {
    private double scholarship;

    public Student(String name, double scholarship) {
        super(name);
        this.scholarship = scholarship;
    }

    @Override
    public double pay() {
        return scholarship;
    }
}

public class PersonPay1 {
    public static void main(String[] args) {
        AbstractPersonPay ps[] = new AbstractPersonPay[2];
        ps[0] = new Teacher("mohailang", 120);
        ps[1] = new Student("莫海浪", 500);
        String output = "";
        for (int i = 0; i < ps.length; i++)
            output += ps[i];
        System.out.println(output);
    }
}
