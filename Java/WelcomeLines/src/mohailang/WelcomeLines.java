package mohailang;

import java.awt.Graphics;
import javax.swing.JApplet;
public class WelcomeLines extends JApplet{
    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.drawLine(15,10,180,10);
        g.drawLine(15,30,180,30);
        g.drawString("Welcome to Applet",25,25);
    }
}
