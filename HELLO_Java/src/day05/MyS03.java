package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class MyS03 extends JFrame {

	private JPanel contentPane;
	private JTextField tf1;
	private JTextField tf2;
	private JTextField tf3;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS03 frame = new MyS03();
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
	public MyS03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 588, 407);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf1 = new JTextField();
		tf1.setHorizontalAlignment(SwingConstants.CENTER);
		tf1.setBounds(27, 38, 96, 21);
		contentPane.add(tf1);
		tf1.setColumns(10);
		
		tf2 = new JTextField();
		tf2.setHorizontalAlignment(SwingConstants.CENTER);
		tf2.setColumns(10);
		tf2.setBounds(197, 38, 96, 21);
		contentPane.add(tf2);
		
		tf3 = new JTextField();
		tf3.setHorizontalAlignment(SwingConstants.CENTER);
		tf3.setColumns(10);
		tf3.setBounds(386, 38, 96, 21);
		contentPane.add(tf3);
		
		JLabel lbl = new JLabel("*");
		lbl.setBounds(154, 41, 31, 15);
		contentPane.add(lbl);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				multiply();
			}
		});
		btn.setBounds(305, 37, 55, 23);
		contentPane.add(btn);
	}
	
	void multiply() {
		String first = tf1.getText();
		String Second = tf2.getText();
		int result = Integer.valueOf(first) * Integer.valueOf(Second);
		tf3.setText(result+"");
	}
}



