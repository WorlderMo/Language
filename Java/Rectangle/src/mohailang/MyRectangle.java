package mohailang;

import java.awt.Graphics;
import javax.swing.*;

public class MyRectangle extends JApplet{
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.drawString("这是一个矩形",15,15);

        g.drawRect(15,25,100,30);
    }
}

