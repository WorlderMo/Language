package mohailang;


import javax.swing.*;
import java.awt.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ThreeClocks extends JApplet implements Runnable {

    Thread clockThread1;
    Thread clockThread2;
    Thread clockThread3;
    boolean f1, f2, f3;
    SimpleDateFormat formatter;
    Date currentDate1, currentDate2, currentDate3;
    String lastdate1, lastdate2, lastdate3;

    @Override
    public void init() {
        formatter = new SimpleDateFormat("hh:mm:ss");
        currentDate1 = new Date();
        lastdate3 = lastdate2 = lastdate1 = formatter.format(currentDate1);

        clockThread1 = new Thread(this, "Clock-thread1");
        clockThread2 = new Thread(this, "Clock-thread2");
        clockThread3 = new Thread(this, "Clock-thread3");
        clockThread1.start();
        clockThread2.start();
        clockThread3.start();
    }

    @Override
    public void run() {
        boolean flag = true;
        while (flag) {
            try {
                if (Thread.currentThread() == clockThread1) {
                    Thread.sleep(1000);
                    f1 = true;
                }
                if (Thread.currentThread() == clockThread2) {
                    Thread.sleep(5000);
                    f2 = true;
                }
                if (Thread.currentThread() == clockThread3) {
                    Thread.sleep(10000);
                    f3 = true;
                }
                super.repaint();
            } catch (InterruptedException e) {
                flag = false;
            }
        }
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(this.getBackground());
        if (f1) {
            currentDate1 = new Date();
            lastdate1 = formatter.format(currentDate1);
            g.fillRect(5, 0, 50, 10);
            f1 = false;
        }
        if (f2) {
            currentDate2 = new Date();
            lastdate2 = formatter.format(currentDate2);
            g.fillRect(125, 0, 50, 10);
            f2 = false;
        }
        if (f3) {
            currentDate3 = new Date();
            lastdate3 = formatter.format(currentDate3);
            g.fillRect(225, 0, 50, 10);
            f3 = false;
        }
        g.setColor(getForeground());
        g.drawString(lastdate1, 5, 10);
        g.drawString(lastdate2, 125, 10);
        g.drawString(lastdate3, 225, 10);
    }
}