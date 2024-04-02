package day06;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class MyS09_1 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
//	String Tel = "";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS09_1 frame = new MyS09_1();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MyS09_1() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 254, 319);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setBounds(24, 10, 185, 31);
		contentPane.add(tf);
		tf.setColumns(10);

		JButton btn1 = new JButton("1");
//		btn1.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				System.out.println(e);
//				System.out.println(e.getSource());
//				System.out.println(e.getComponent());
//				System.out.println(e.getSource());
//				
//				JButton imsi = (JButton) e.getSource();
//				System.out.println(imsi.getText());
//				myclick(e);
//			}
//		});
		btn1.setBounds(24, 74, 54, 23);
		contentPane.add(btn1);

		JButton btn2 = new JButton("2");
		btn2.setBounds(90, 74, 54, 23);
		contentPane.add(btn2);

		JButton btn3 = new JButton("3");
		btn3.setBounds(155, 74, 54, 23);
		contentPane.add(btn3);

		JButton btn4 = new JButton("4");
		btn4.setBounds(24, 111, 54, 23);
		contentPane.add(btn4);

		JButton btn5 = new JButton("5");
		btn5.setBounds(90, 111, 54, 23);
		contentPane.add(btn5);

		JButton btn6 = new JButton("6");
		btn6.setBounds(155, 111, 54, 23);
		contentPane.add(btn6);

		JButton btn7 = new JButton("7");
		btn7.setBounds(24, 144, 54, 23);
		contentPane.add(btn7);

		JButton btn8 = new JButton("8");
		btn8.setBounds(90, 144, 54, 23);
		contentPane.add(btn8);

		JButton btn9 = new JButton("9");
		btn9.setBounds(155, 144, 54, 23);
		contentPane.add(btn9);

		JButton btn0 = new JButton("0");
		btn0.setBounds(90, 179, 54, 23);
		contentPane.add(btn0);

		JButton btn_call = new JButton("☎");
		btn_call.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				call();
			}
		});
		btn_call.setBounds(24, 225, 185, 23);
		contentPane.add(btn_call);
		
		btn0.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn1.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn2.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn3.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn4.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn5.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn6.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn7.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn8.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
		btn9.addMouseListener(new MouseAdapter() { public void mouseClicked(MouseEvent e){ myclick(e);}});
	}

	void myclick(MouseEvent e) {
		JButton temp = (JButton) e.getSource();
		String str_new = temp.getText();
		String str_old = tf.getText();
		
		tf.setText(str_old+str_new);
		
	}

	void call() {
		String str_tel = tf.getText();
		JOptionPane.showMessageDialog(null, "Calling...\n" + str_tel);
	}
}
