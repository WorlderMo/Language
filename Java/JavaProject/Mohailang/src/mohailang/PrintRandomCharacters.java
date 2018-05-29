package mohailang;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PrintRandomCharacters extends JApplet implements ActionListener {
    private String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private final int SIZE = 3;
    private JLabel outputs[];
    private JCheckBox checkboxes[];
    private Thread threads[];
    private boolean suspended[];
    static int count = 0;

    @Override
    public void init() {
        outputs = new JLabel[SIZE];
        checkboxes = new JCheckBox[SIZE];
        threads = new Thread[SIZE];
        suspended = new boolean[SIZE];
        Container container = getContentPane();
        container.setLayout(new GridLayout(SIZE, 2, 5, 5));
        for (int count = 0; count < SIZE; count++) {
            outputs[count] = new JLabel();
            outputs[count].setBackground(Color.GREEN);
            outputs[count].setOpaque(true);
            container.add(outputs[count]);
            checkboxes[count] = new JCheckBox("线程挂起");
            checkboxes[count].addActionListener(this);
            container.add(checkboxes[count]);
        }
    }

    @Override
    public void start() {
        for (int count = 0; count < threads.length; count++) {
            threads[count] = new Thread(new RunnableObject(), "线程" + (count + 1));
            threads[count].start();
        }
    }

    private int getIndex(Thread current) {
        for (int count = 0; count < threads.length; count++) {
            if (current == threads[count]) {
                return count;
            }
        }
        return -1;
    }

    @Override
    public synchronized void stop() {
        for (int count = 0; count < threads.length; count++) {
            threads[count] = null;
        }
        notifyAll();
    }

    @Override
    public synchronized void actionPerformed(ActionEvent e) {
        for (int count = 0; count < checkboxes.length; count++) {
            if (e.getSource() == checkboxes[count]) {
                suspended[count] = !suspended[count];
                outputs[count].setBackground(suspended[count] ? Color.RED : Color.GREEN);
            }
            if (!suspended[count]) {
                notifyAll();
            }
            return;
        }
    }

    private class RunnableObject implements Runnable {
        @Override
        public void run() {
            // TODO Auto-generated method stub
            final Thread currentThread = Thread.currentThread();
            final int index = getIndex(currentThread);
            System.err.println("index=" + index + ",thread=" + currentThread.getName());
            System.err.println("count=" + count++);
            while (threads[index] == currentThread) {
                try {
                    Thread.sleep((int) (Math.random() * 1000));
                    synchronized (PrintRandomCharacters.this) {
                        while (suspended[index] && threads[index] == currentThread) {
                            PrintRandomCharacters.this.wait();
                        }
                    }
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                SwingUtilities.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        char displayChar = alphabet.charAt((int) (Math.random() * 26));
                        outputs[index].setText(currentThread.getName() + ":" + displayChar);
                    }
                });
            }
            System.err.println(currentThread.getName() + "terminating");
        }
    }
}
