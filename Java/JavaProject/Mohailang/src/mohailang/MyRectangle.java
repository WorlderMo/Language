package mohailang;
/**
 * MyRectangle
 */
public class MyRectangle {

    public float length, width;

    public MyRectangle() {
        setRectangle(3, 4);
    }

    public MyRectangle(float l, float w) {
        setRectangle(l, w);
    }

    public void setRectangle(float l, float w) {
        setLength(l);
        setWidth(w);
    }

    public void setLength(float length) {
        this.length = length;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public float getLength() {
        return length;
    }

    public float getWidth() {
        return width;
    }

    public float getArea() {
        return width * length;
    }

    @Override
    public String toString() {
        return "Rectangle--> "+"Length: " + getLength() + " Width: " + getWidth() + " Area: " + getArea();
    }
}
