package mohailang;
public class Puppy{
    int puppyAge;
    public Puppy(String name){

        System.out.println("dog's name:" + name);
    }

    public void setAge(int age){

        puppyAge = age;
    }

    public int getAge(){
        System.out.println("dog's age: " + puppyAge);
        return puppyAge;
    }

    public static void main(String[] args) {
        Puppy mypuppy = new Puppy("tommy");
        mypuppy.setAge(2);
        mypuppy.getAge();
        System.out.println("value:" + mypuppy.puppyAge);
    }
}
