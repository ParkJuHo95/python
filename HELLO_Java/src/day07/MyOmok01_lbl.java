package day07;

import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JButton;
import javax.swing.ImageIcon;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.JLabel;

public class MyOmok01_lbl extends JFrame {

	private JPanel contentPane;
	boolean flag_wb = true;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyOmok02 frame = new MyOmok02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public MyOmok01_lbl() {
		setTitle("lbl");
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
				JLabel lbl = new JLabel();
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						click(e);
					}
				});
				lbl.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/0.png")));
				lbl.setBounds(20+40*i, 20+40*j, 40, 40);
				contentPane.add(lbl);
			}
		}
	}

	void click(MouseEvent e) {
		JLabel eb = (JLabel)e.getSource();
		if (flag_wb) {
			eb.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/2.png")));
		} else {
			eb.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/1.png")));
		}
		
		
		flag_wb = !flag_wb;
	}
}
