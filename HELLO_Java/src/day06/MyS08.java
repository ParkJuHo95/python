package day06;

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
import javax.swing.JOptionPane;

public class MyS08 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;
	JTextArea ta;
	int com = (int) (Math.random() * 100) + 1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS08 frame = new MyS08();
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
	public MyS08() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 306, 507);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl = new JLabel("맞출 수");
		lbl.setBounds(33, 36, 62, 15);
		contentPane.add(lbl);

		tf = new JTextField();
		tf.setBounds(107, 33, 96, 21);
		contentPane.add(tf);
		tf.setColumns(10);

		JButton btn = new JButton("맞춰보기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		btn.setBounds(33, 71, 170, 23);
		contentPane.add(btn);

		ta = new JTextArea();
		ta.setBounds(45, 127, 170, 285);
		contentPane.add(ta);
	}

	public void myClick() {
		String user = tf.getText();
		int userAns = Integer.parseInt(user);
		String result = "";
		if (com == userAns) {
			result += userAns + " Answer\n";
			JOptionPane.showMessageDialog(null, userAns + " Answer\n");
//			com = (int) (Math.random() * 100) + 1;
			setCom();
		} else if (com > userAns) {
			result += userAns + " UP\n";
		} else {
			result += userAns + " DOWN\n";
		}
		ta.append(result);
		tf.setText("");
	}
	
	void setCom() {
		com = (int)(Math.random() * 100) + 1;
	}

}
