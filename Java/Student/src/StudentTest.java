import student.Student;

public class StudentTest {
    public static void main(String[] args) {

        Student student1 = new Student(2018, 2015, "莫海浪", "boy", 22);
        Student student2 = new Student();
        System.out.println(student1.getString());
        System.out.println(student2.getString());

        student1.setName("Worlder");
        student1.setAge(20);
        System.out.println("Name: " + student1.getName() + " Age: " + student1.getAge());

        String compareAge = student1.getAge() > student2.getAge() ? "student1" : "student2";
        System.out.println("年龄较大的对象是: "+compareAge);

    }
}
