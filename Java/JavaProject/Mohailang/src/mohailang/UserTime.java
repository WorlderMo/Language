//package mohailang;

/**
 * @Date    : 2018-05-08 19:07:08
 * @Author  : mohailang (1198534595@qq.com)
 */
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class UserTime extends JFrame {
    private static final long serialVersionUID = 520123;
    private JLabel hLabel, mLabel, sLabel;
    private JTextField hField, mField, sField, displayField;

    public UserTime() {
        super("嵌套内部类例子");
        Container hourContainer = getContentPane();
        Container minContainer = getContentPane();
        Container secondContainer = getContentPane();
        hourContainer.setLayout(new FlowLayout());

        hLabel = new JLabel("设置时:");
        hField = new JTextField(9);
        hourContainer.add(hLabel);
        hourContainer.add(hField);
        ActionEventHandler hourHandler = new ActionEventHandler();
        hField.addActionListener(hourHandler);

        mLabel = new JLabel("设置分:");
        mField = new JTextField(9);
        minContainer.add(mLabel);
        minContainer.add(mField);
        ActionEventHandler minHandler = new ActionEventHandler();
        mField.addActionListener(minHandler);

        sLabel = new JLabel("设置秒:");
        sField = new JTextField(9);
        secondContainer.add(sLabel);
        secondContainer.add(sField);
        ActionEventHandler secondHandler = new ActionEventHandler();
        sField.addActionListener(secondHandler);

        displayField = new JTextField(30);
        displayField.setEditable(false);
        minContainer.add(displayField);
        setSize(600, 140);
        setVisible(true);
    }

    public String setTime(String hour, String min, String second) {
        if (Integer.parseInt(hour) > 24 || Integer.parseInt(hour) < 0) {
            return "小时设置错误";
        }
        if (Integer.parseInt(min) > 60 || Integer.parseInt(min) < 0) {
            return "分钟设置错误";
        }
        if (Integer.parseInt(second) > 60 || Integer.parseInt(hour) < 0) {
            return "秒钟设置错误";
        }
        String output = "时间：" + hour + "：" + min + "：" + second;
        return output;
    }

    private class ActionEventHandler implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent event) {
            String hour = hField.getText();
            String min = mField.getText();
            String second = sField.getText();

            if (event.getSource() == hField || event.getSource() == mField || event.getSource() == sField) {
                displayField.setText(setTime(hour, min, second));
            }
        }
    }

    public static void main(String[] args) {
        UserTime userTime = new UserTime();
    }
}
