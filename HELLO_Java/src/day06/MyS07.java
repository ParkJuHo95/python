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

public class MyS07 extends JFrame {

	private JPanel contentPane;
	private JTextField tf_first;
	private JTextField tf_last;
	JLabel lbl_first, lbl_last;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS07 frame = new MyS07();
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
	public MyS07() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 292, 487);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		lbl_first = new JLabel("첫별수:");
		lbl_first.setBounds(50, 27, 50, 15);
		contentPane.add(lbl_first);

		lbl_last = new JLabel("끝별수:");
		lbl_last.setBounds(50, 72, 50, 15);
		contentPane.add(lbl_last);

		tf_first = new JTextField();
		tf_first.setBounds(112, 24, 96, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);

		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(112, 69, 96, 21);
		contentPane.add(tf_last);

		JButton btn = new JButton("별 그리기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
//				star();
				teacher();
			}
		});
		btn.setBounds(47, 114, 161, 23);
		contentPane.add(btn);

		ta = new JTextArea();
		ta.setBounds(50, 190, 170, 229);
		contentPane.add(ta);
	}

	public void star() {

		int firstNum = Integer.parseInt(tf_first.getText());
		int lastNum = Integer.parseInt(tf_last.getText());

		String result = "";

		for (int i = 0; i <= (lastNum - firstNum); i++) {
			for (int j = 0; j < firstNum + i; j++) {
				result += "*";
			}
			result += "\n";
		}

		ta.setText(result);
	}

	public String getStar(int cnt) {
		String ret = "";
		for (int i = 0; i < cnt; i++) {
			ret += "*";
		}
		ret += "\n";
		return ret;
	}

	public void teacher() {
		String f = tf_first.getText();
		String l = tf_last.getText();
		int ff = Integer.parseInt(f);
		int ll = Integer.parseInt(l);

		String txt = "";

		for (int i = ff; i <= ll; i++) {
			txt += getStar(i);
		}

		ta.setText(txt);
	}
}
