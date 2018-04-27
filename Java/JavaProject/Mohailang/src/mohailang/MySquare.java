package mohailang;
public class MySquare extends MyRectangle {

    public float edge;

    public MySquare() {
        setSquare(3);
    }

    public MySquare(int e) {
        setSquare(e);
    }

    public void setSquare(int e){
        setEdge(e);
    }

    public void setEdge(int edge) {
        this.edge = edge;
    }

    public float getEdge() {
        return edge;
    }

    @Override
    public float getArea() {
        return edge * edge;
    }

    @Override
    public String toString() {
        return "Square--> "+"Edge: " + getEdge() + " Area: " + getArea();
    }
}
