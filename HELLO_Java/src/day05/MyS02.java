package day05;

import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.border.EmptyBorder;

public class MyS02 extends JFrame {

	private JPanel contentPane;
	private JTextField tf;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS02 frame = new MyS02();
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
	public MyS02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		tf = new JTextField();
		tf.setHorizontalAlignment(SwingConstants.RIGHT);
		tf.setText("200");
		tf.setBounds(130, 31, 149, 85);
		contentPane.add(tf);
		tf.setColumns(10);
		
		JButton btn = new JButton("DECREASE");
		btn.setBounds(158, 144, 93, 23);
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
				fontSize();
			}

			
		});
		contentPane.add(btn);
	}
	public void myClick() {
		String a = tf.getText();
		int b = Integer.parseInt(a);
		b--;
		tf.setText(String.valueOf(b));
	}
	
	public void fontSize() {
		Font origin = tf.getFont();
		int size = origin.getSize();
		size--;
	}
}

