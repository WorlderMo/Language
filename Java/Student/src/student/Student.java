package student;

public class Student {
    private int id = 3;
    private int classNum;
    private String name;
    private String sex;
    private int age;

    private static int count = 0;

    public Student() {
        count++;
        setStudent(2015052278, 2015, "mohailang", "boy", 23);
    }

    public Student(int i, int c, String n, String s, int a) {
        count++;
        setStudent(i, c, n, s, a);
    }

    public void setStudent(int i, int c, String n, String s, int a) {
        setId(i);
        setClassNum(c);
        setName(n);
        setSex(s);
        setAge(a);
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setClassNum(int classNum) {
        this.classNum = classNum;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public int getId() {
        return id;
    }

    public int getClassNum() {
        return classNum;
    }

    public String getName() {
        return name;
    }

    public String getSex() {
        return sex;
    }

    public int getAge() {
        return age;
    }

    public String getString() {

        return "ID: " + id + " classNum: " + classNum + " Name: " + name + " Sex: " + sex + " Age: " + age;
    }

    public static int getCount() {
        return count;
    }
}
