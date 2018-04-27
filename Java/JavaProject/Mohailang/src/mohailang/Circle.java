package mohailang;

public class Circle {
    //数据域封装
    private double x;
    private double y;
    private double r;

    public double getX() {
        return this.x;
    }

    public double getY() {
        return this.y;
    }

    public double getR() {
        return this.r;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }

    public void setR(double r) {
        this.r = r;
    }

    //构造方法
    public Circle() {
        this.x = 0;
        this.y = 0;
        this.r = 1;
    }

    public Circle(double x,double y,double r) {
        this.x = x;
        this.y = y;
        this.r = r;
    }

    //toString方法
    public String toString() {
        StringBuffer buffer = new StringBuffer();
        buffer.append("x坐标是:" + this.x + "\n");
        buffer.append("y坐标是:" + this.y + "\n");
        buffer.append("半径是:" + this.r + "\n");

        return buffer.toString();
    }
    //圆的面积
    public double getArea() {
        return Math.PI*this.r*this.r;
    }
    //圆的周长
    public double getCircumference() {
        return 2*Math.PI*this.r;
    }

    public static void main(String[] args) {
        Circle cir = new Circle(2.0, 2.0, 3.0);
        System.out.println(cir.getX() + " " + cir.getY() + " " + cir.getR());
        System.out.println(cir.getArea());
        System.out.println(cir.getCircumference());
    }
}
