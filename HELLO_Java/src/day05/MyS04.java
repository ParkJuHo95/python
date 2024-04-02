package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS04 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS04 frame = new MyS04();
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
	public MyS04() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl = new JLabel("출력 단수");
		lbl.setBounds(46, 38, 59, 15);
		contentPane.add(lbl);

		tf = new JTextField();
		tf.setBounds(119, 35, 96, 21);
		contentPane.add(tf);
		tf.setColumns(10);

		JButton btn = new JButton("출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				gugudan();
			}
		});
		btn.setBounds(46, 63, 169, 23);
		contentPane.add(btn);

		ta = new JTextArea();
		ta.setBounds(46, 96, 169, 157);
		contentPane.add(ta);
	}

	protected void gugudan() {
		String dan = tf.getText();
		if (!dan.equals("")&& dan != null ) {
			int numDan = Integer.valueOf(dan);
			String result = "";
			for (int i = 1; i < 10; i++) {
				result += numDan + " * " + i + " = " + numDan * i + "\n";
			}
			ta.setText(result);
		} else {
			ta.setText("입력된 값이 없습니다.");
		}
	}
}
