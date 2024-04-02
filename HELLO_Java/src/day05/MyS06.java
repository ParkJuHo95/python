package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyS06 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_mine;
	private JTextField tf_com;
	private JTextField tf_result;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS06 frame = new MyS06();
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
	public MyS06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lbl_mine = new JLabel("나 : ");
		lbl_mine.setBounds(46, 36, 50, 15);
		contentPane.add(lbl_mine);

		JLabel lbl_com = new JLabel("컴 : ");
		lbl_com.setBounds(46, 61, 50, 15);
		contentPane.add(lbl_com);

		JLabel lbl_result = new JLabel("결과 : ");
		lbl_result.setBounds(46, 86, 50, 15);
		contentPane.add(lbl_result);

		tf_mine = new JTextField();
		tf_mine.setBounds(90, 33, 61, 21);
		contentPane.add(tf_mine);
		tf_mine.setColumns(10);

		tf_com = new JTextField();
		tf_com.setColumns(10);
		tf_com.setBounds(90, 58, 61, 21);
		contentPane.add(tf_com);

		tf_result = new JTextField();
		tf_result.setColumns(10);
		tf_result.setBounds(90, 83, 61, 21);
		contentPane.add(tf_result);

		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				game();
			}
		});
		btn.setBounds(46, 128, 91, 23);
		contentPane.add(btn);
	}

	void game() {
		String mine = tf_mine.getText();
		int ran = (int)(Math.random()*2);
		String com = ""; 
		if(ran == 1) {
			com = "홀";
		} else {
			com = "짝";
		}
		tf_com.setText(com);
		
		String result = "";
		if(com.equals(mine)) {
			result = "승리";
		} else {
			result = "패배";
		}
		tf_result.setText(result);
	}

}
