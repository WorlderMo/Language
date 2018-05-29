package mohailang;

import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class ThreeClocks extends JApplet implements Runnable {
    public Thread clocks[] = new Thread[3];

    @Override
    public void init() {
        for (int count = 0; count < 3; count++) {
            clocks[count].start();
        }
    }

    @Override
    public void run() {
        for (int count = 0; count < 3; count++) {
            boolean flag = true;
            while (flag) {
                repaint();
                try {
                    clocks[count].sleep(1000);
                } catch (InterruptedException e) {
                    flag = false;
                }
            }
        }
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        SimpleDateFormat formatter = new SimpleDateFormat("hh:mm:ss", Locale.getDefault());
        Date currentDate = new Date();
        String lastDate = formatter.format(currentDate);
        g.drawString(lastDate, 5, 10);
    }
}