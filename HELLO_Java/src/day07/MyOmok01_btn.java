package day07;

import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyOmok01_btn extends JFrame {

	private JPanel contentPane;
	int cnt = 1;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyOmok01_btn frame = new MyOmok01_btn();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public MyOmok01_btn() {
		setTitle("btn");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 812, 616);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
//		JButton btn_new = new JButton("초기화");
//		btn_new.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				cnt =0;
//			}
//		});
//		btn_new.setBounds(707, 556, 91, 23);
//		contentPane.add(btn_new);

		for (int i = 0; i < 15; i++) {
			for(int j=0 ; j<15 ; j++) {
				JButton btn = new JButton();
				btn.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						click(e);
					}
				});
				btn.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/0.png")));
				btn.setBounds(40 + 40 * i, 40 + 40*j, 40, 40);
				btn.setBorderPainted(false);
				contentPane.add(btn);
			}
		}
	}

	void click(MouseEvent e) {
		JButton eb = (JButton) e.getSource();
		if (cnt % 2 == 1) {
			eb.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/2.png")));
		} else {
			eb.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/1.png")));
		}
		cnt++;
	}
}
