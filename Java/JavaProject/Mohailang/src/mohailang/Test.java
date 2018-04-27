// package mohailang;

class Test0 {
    public int b = 3;

    public Test0() {
        System.out.println(b);
    }
}

class Test1 extends Test0 {

    public int a;

    public Test1() {
        a = 12;
        System.out.println(a);
    }
}

class Test2 extends Test1 {

    public Test2() {
        System.out.println(a);
    }
}

public class Test {
    public static void main(String[] args) {
        new Test2();
        System.out.println();
    }
}
