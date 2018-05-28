/**
 * @Date : 2018-05-09 00:01:35
 * @Author : mohailang (1198534595@qq.com)
 */
//package mohailang;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Equation extends JFrame {
    private static final long serialVersionUID = 520123;
    private JLabel a, b, c;
    private JTextField aField, bField, cField, displayField;
    private JLabel aJLabel, bJLabel, cJLabel;
    private JButton computeButton, exiButton;

    public String Soulution(double a, double b, double c) {
        double d = b * b - 4 * a * c;
        double x1, x2;
        if (d >= 0) {
            x1 = (-b + Math.sqrt(d)) / (2 * a);
            x2 = (-b - Math.sqrt(d)) / (2 * a);
            return "x1=" + String.valueOf(x1) + "," + "x2=" + String.valueOf(x2);
        } else {
            return "没有实数根";
        }
    }

    public Equation() {
        super("计算方程的根");
        Container aContainer = getContentPane();
        Container bContainer = getContentPane();
        Container cContainer = getContentPane();
        aContainer.setLayout(new FlowLayout());

        aJLabel = new JLabel("a");
        aField = new JTextField(9);
        aContainer.add(aJLabel);
        aContainer.add(aField);
        // ActionEventHandler aHandler = new ActionEventHandler();
        // aField.addActionListener(aHandler);

        bJLabel = new JLabel("b");
        bField = new JTextField(9);
        bContainer.add(bJLabel);
        bContainer.add(bField);
        // ActionEventHandler bHandler = new ActionEventHandler();
        // aField.addActionListener(bHandler);

        cJLabel = new JLabel("c");
        cField = new JTextField(9);
        cContainer.add(cJLabel);
        cContainer.add(cField);
        // ActionEventHandler cHandler = new ActionEventHandler();
        // aField.addActionListener(cHandler);

        displayField = new JTextField(30);
        displayField.setEditable(false);
        bContainer.add(displayField);

        computeButton = new JButton("计算实根");
        exiButton = new JButton("退出");
        cContainer.add(computeButton);
        cContainer.add(exiButton);

        computeButton.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                String a = aField.getText();
                String b = bField.getText();
                String c = cField.getText();
                String output = Soulution(Double.parseDouble(a), Double.parseDouble(b), Double.parseDouble(c));
                displayField.setText(output);
            }
        });

        exiButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        setSize(450, 140);
        setVisible(true);
    }

    public static void main(String[] args) {
        Equation equation = new Equation();
    }

}
