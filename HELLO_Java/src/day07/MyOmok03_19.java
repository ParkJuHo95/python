package day07;

import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class MyOmok03_19 extends JFrame {

	private JPanel contentPane;
	JLabel lbl;
	Boolean flag_wb = false;
	Boolean flag_ing = true;
//	int[][] arr2D = { 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 },
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 },
//
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 },
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }
//
//	};
	int[][] arr2D = new int[19][19];
	int width = arr2D.length;
	int height = arr2D[0].length;

	JLabel[][] lbl2D = new JLabel[height][width];

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyOmok03_19 frame = new MyOmok03_19();
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
	public MyOmok03_19() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 850, 661);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lblNewLabel = new JLabel("0.0");
		lblNewLabel.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myReset();
			}
		});
		lblNewLabel.setIcon(new ImageIcon(MyOmok03_19.class.getResource("/day07/0.png")));
		lblNewLabel.setBounds(800, 10, 40, 40);
		contentPane.add(lblNewLabel);

		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				lbl = new JLabel("");
				lbl.addMouseListener(new MouseAdapter() {
					public void mouseClicked(MouseEvent e) {
//						if (flag_ing) {
							myclick(e);
//						}
					}
				});
				lbl.setIcon(new ImageIcon(MyOmok03_19.class.getResource("/day07/0.png")));
				lbl.setBounds((40 * j), (40 * i), 40, 40);
				lbl.setText(i + "," + j);
				contentPane.add(lbl);
				lbl2D[i][j] = lbl;
			}
		}
		myrender();
	}

	void myrender() {
		for (int i = 0; i < height; i++) {
			for (int j = 0; j < width; j++) {
				if (arr2D[i][j] == 1) { // 2차원 배열에선 i가 행의 인덱스 -> 세로방향 j가 열의 인덱스 -> 가로방향
					lbl2D[i][j].setIcon(new ImageIcon(MyOmok03_19.class.getResource("/day07/1.png")));
				} else if (arr2D[i][j] == 2) {
					lbl2D[i][j].setIcon(new ImageIcon(MyOmok03_19.class.getResource("/day07/2.png")));
				} else {
					lbl2D[i][j].setIcon(new ImageIcon(MyOmok03_19.class.getResource("/day07/0.png")));
				}
			}
		}
	}

	int getUP(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				x--;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getDW(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				x++;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getRI(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				y++;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getLE(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				y--;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getUL(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				x--;
				y--;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getUR(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				x--;
				y++;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getDL(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				x++;
				y--;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	int getDR(int x, int y, int stone) {
		int count = 0;
		try {
			while (true) {
				x++;
				y++;
				if (stone == arr2D[x][y]) {
					count++;
				} else {
					return count;
				}
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return count;
		}
	}

	void myclick(MouseEvent e) {
		if(!flag_ing) return;
		JLabel lbl = (JLabel) (e.getSource());
		String a = lbl.getText();
		String[] arr = a.split(",");
		System.out.println(arr);
		int x = Integer.parseInt(arr[0]);
		int y = Integer.parseInt(arr[1]);
//		if (arr2D[x][y] == 0) {
		int stone = 0;
		if (arr2D[x][y] != 0)
			return;
		if (flag_wb) {
			arr2D[x][y] = 1;
			stone = 1;
		} else {
			arr2D[x][y] = 2;
			stone = 2;
		}
//		}

		String winner = "";
		if (flag_wb == false) {
			winner = "흑";
		} else {
			winner = "백";
		}
		int up = getUP(x, y, stone);
		int down = getDW(x, y, stone);
		int ri = getRI(x, y, stone);
		int le = getLE(x, y, stone);
		int ul = getUL(x, y, stone);
		int ur = getUR(x, y, stone);
		int dl = getDL(x, y, stone);
		int dr = getDR(x, y, stone);
//		System.out.println(up);
//		System.out.println(down);
//		System.out.println(ri);
//		System.out.println(le);
//		System.out.println(ur);
//		System.out.println(ul);
//		System.out.println(dr);
//		System.out.println(dl);

		myrender();
		
		int d1 = up + down + 1;
		int d2 = ri + le + 1;
		int d3 = ul + dr + 1;
		int d4 = ur + dl + 1;
		
		if (d1 == 5 || d2 == 5 || d3 == 5 || d4 == 5) {
			JOptionPane.showMessageDialog(null, winner + " 승리!");
			flag_ing = false;
		}
		
//		if (up + down + 1 == 5) {
//			JOptionPane.showMessageDialog(null, winner + " 승리!");
//			reset();
//		} else if (ri + le + 1 == 5) {
//			JOptionPane.showMessageDialog(null, winner + " 승리!");
//			reset();
//		} else if (ul + dr + 1 == 5) {
//			JOptionPane.showMessageDialog(null, winner + " 승리!");
//			reset();
//		} else if (ur + dl + 1 == 5) {
//			JOptionPane.showMessageDialog(null, winner + " 승리!");
//			reset();
//		}

		flag_wb = !flag_wb;
	}

	void myReset() {
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				arr2D[i][j] = 0;
			}
		}
		flag_ing = true;
		flag_wb = false;
		myrender();
	}

}