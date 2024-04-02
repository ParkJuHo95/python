package day05;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class MyS05 extends JFrame {

	private JPanel contentPane;
	JLabel lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7;
	private JLabel lblNewLabel;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyS05 frame = new MyS05();
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
	public MyS05() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		lbl1 = new JLabel("__");
		lbl1.setBounds(27, 45, 29, 15);
		contentPane.add(lbl1);

		lbl2 = new JLabel("__");
		lbl2.setBounds(68, 45, 29, 15);
		contentPane.add(lbl2);

		lbl3 = new JLabel("__");
		lbl3.setBounds(112, 45, 29, 15);
		contentPane.add(lbl3);

		lbl4 = new JLabel("__");
		lbl4.setBounds(153, 45, 29, 15);
		contentPane.add(lbl4);

		lbl5 = new JLabel("__");
		lbl5.setBounds(194, 45, 29, 15);
		contentPane.add(lbl5);

		lbl6 = new JLabel("__");
		lbl6.setBounds(237, 45, 29, 15);
		contentPane.add(lbl6);

		JButton btn = new JButton("로또 생성하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lotto();
			}
		});
		btn.setBounds(25, 80, 227, 23);
		contentPane.add(btn);

		lbl7 = new JLabel("__");
		lbl7.setBounds(346, 45, 50, 15);
		contentPane.add(lbl7);

		lblNewLabel = new JLabel("보너스 번호");
		lblNewLabel.setBounds(278, 45, 73, 15);
		contentPane.add(lblNewLabel);
	}

	void lotto() {
		List<String> lotto = new ArrayList<String>();

		for (int i = 0; i < 6; i++) {
			String rnd = String.format("%02d", ((int) (Math.random() * 45) + 1));
			if (lotto.contains(rnd)) {
				i--;
			} else {
				lotto.add(rnd);
			}
		}

		Collections.sort(lotto);

		do {
			String bonus = String.format("%02d", ((int) (Math.random() * 45) + 1));
			if (lotto.contains(bonus)) {
				continue;
			} else {
				lotto.add(bonus);
			}
		} while (lotto.size() < 7);

		lbl1.setText(lotto.get(0));
		lbl2.setText(lotto.get(1));
		lbl3.setText(lotto.get(2));
		lbl4.setText(lotto.get(3));
		lbl5.setText(lotto.get(4));
		lbl6.setText(lotto.get(5));
		lbl7.setText(lotto.get(6));
	}

}
