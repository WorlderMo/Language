package mohailang;

import java.awt.Button;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class WelcomeString extends WindowAdapter implements ActionListener {
    public class Thread3 extends Thread {
        Panel p1;
        Label lb1;
        TextField tf1, tf2;
        Button b1, b2;
        int sleeptime = (int) (Math.random() * 100);

        public Thread3(String str) {
            super(str);
            for (int i = 0; i < 100; i++) {
                str = str + " ";
            }
            tf1 = new TextField(str);
            f.add(tf1);
            p1 = new Panel();
            p1.setLayout(new FlowLayout(FlowLayout.LEFT));
            lb1 = new Label("sleep");
            tf2 = new TextField("" + sleeptime);
            p1.add(lb1);
            p1.add(tf2);
            b1 = new Button("启动");
            b2 = new Button("中断");
            p1.add(b1);
            p1.add(b2);
            b1.addActionListener(new WelcomeString());
            b2.addActionListener(new WelcomeString());
            f.add(p1);
            f.setVisible(true);
        }

        @Override
        public void run() {
            String str;
            while (true) {
                try {
                    str = tf1.getText();
                    str = str.substring(1) + str.substring(0, 1);
                    tf1.setText(str);
                    this.sleep(sleeptime);
                } catch (InterruptedException e) {
                    System.out.println(e);
                    break;
                }
            }
        }

        public void setButton() {
            if (this.isAlive()) {
                b1.setEnabled(false);
                b2.setEnabled(true);
            }
            if (this.isInterrupted()) {
                b1.setEnabled(true);
                b2.setEnabled(false);
            }
        }

    }

    @Override
    public void windowClosing(WindowEvent e) {
        System.exit(0);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == wt1.b1 || e.getSource() == wt1.b2) {
            actionPerformed(e, wt1);
        }
        if (e.getSource() == wt2.b1 || e.getSource() == wt2.b2) {
            actionPerformed(e, wt2);
        }
    }

    public void actionPerformed(ActionEvent e, Thread3 wt) {
        if (e.getSource() == wt.b1) {
            wt.sleeptime = Integer.parseInt(wt.tf2.getText());
            wt.start();
        }
        if (e.getSource() == wt.b2) {
            wt.interrupt();
        }
        wt.setButton();
    }

    Frame f;
    static WelcomeString.Thread3 wt1, wt2;

    public static void main(String args[]) {
        WelcomeString w = new WelcomeString();
        w.display();
        wt1 = w.new Thread3("Welcome!");
        wt2 = w.new Thread3("How are you?");
        wt1.setButton();
        wt2.setButton();

    }

    public void display() {
        f = new Frame("Welcome");
        f.setSize(400, 240);
        f.setLocation(200, 140);
        f.setBackground(Color.lightGray);
        f.setLayout(new GridLayout(4, 1));
        f.addWindowListener(this);
        f.setVisible(true);
    }
}
