package day07;

import java.awt.EventQueue;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import java.util.List;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class MyOmok02 extends JFrame {
	private JPanel contentPane;
	boolean flag_wb = true;
	// 랜더링
//	int[][] arr2D = { 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 1, 2, 1, 0,  0, 0, 0, 0, 0 },
//			{ 0, 2, 1, 1, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 },
//
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 },
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 0 }, 
//			{ 0, 0, 0, 0, 0,  0, 0, 0, 0, 2 } 
//	};
	int[][] arr2D = new int[10][10];
	int width = arr2D.length;
	int height = arr2D[0].length;
	int winCount = 5;
	JLabel[][] jarr2D = new JLabel[width][height];

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

	public MyOmok02() {
		setTitle("lbl");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 468, 425);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);

		JButton btn_reset = new JButton("새 게임");
		btn_reset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				reset();
			}
		});
		btn_reset.setBounds(410, 10, 40, 40);
		contentPane.add(btn_reset);

//		JButton btn_new = new JButton("초기화");
//		btn_new.addMouseListener(new MouseAdapter() {
//			@Override
//			public void mouseClicked(MouseEvent e) {
//				cnt =0;
//			}
//		});
//		btn_new.setBounds(707, 556, 91, 23);
//		contentPane.add(btn_new);

		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				JLabel lbl = new JLabel();
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						click(e);
					}
				});
//				lbl.setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/"+0+".png")));
				lbl.setBounds(10 + 40 * j, 10 + 40 * i, 40, 40);
				contentPane.add(lbl);
				jarr2D[i][j] = lbl;
			}
		}
		myrender();
	}

	void myrender() {
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				if (arr2D[i][j] == 1) {
					jarr2D[i][j].setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/1.png")));
				} else if (arr2D[i][j] == 2) {
					jarr2D[i][j].setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/2.png")));
				} else {
					jarr2D[i][j].setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/0.png")));
				}

			}
		}
	}

	void myrender(int i, int j) {
		if (arr2D[i][j] == 1) {
			jarr2D[i][j].setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/1.png")));
		} else if (arr2D[i][j] == 2) {
			jarr2D[i][j].setIcon(new ImageIcon(MyOmok01_btn.class.getResource("/day07/2.png")));
		}
	}

	void click(MouseEvent e) {
//		System.out.println(e.getSource());
		JLabel jl = (JLabel) e.getSource();
		Point pt = jl.getLocation();
		int i = (pt.y - 10) / 40;
		int j = (pt.x - 10) / 40;
		if (arr2D[i][j] == 0) {
			if (flag_wb) {
				arr2D[i][j] = 1;
			} else {
				arr2D[i][j] = 2;
			}
			flag_wb = !flag_wb;
			myrender(i, j);
		}
		gameOver(i, j);
	}

	void reset() {
		for (int i = 0; i < width; i++) {
			for (int j = 0; j < height; j++) {
				arr2D[i][j] = 0;
			}
		}
		myrender();
	}

	void gameOver(int x, int y) {
		check(garo(x, y));
		check(sero(x, y));
		check(RDD(x, y));
		check(RUD(x, y));
	}

	List<Integer> garo(int x, int y) {
		List<Integer> garo = new ArrayList<Integer>();
		for (int i = 0; i < width; i++) {
			garo.add(arr2D[x][i]);
		}
		return garo;
	}

	List<Integer> sero(int x, int y) {
		List<Integer> sero = new ArrayList<Integer>();
		for (int i = 0; i < width; i++) {
			sero.add(arr2D[i][y]);
		}
		return sero;
	}

	List<Integer> RDD(int x, int y) {
		int startx = 0;
		int starty = 0;
		if (x < y) {
			startx = 0;
			starty = y - x;
		} else {
			startx = x - y;
			starty = 0;
		}
		List<Integer> rdd = new ArrayList<Integer>();
		for (int i = 0; i < width - startx - starty; i++) {
			rdd.add(arr2D[startx + i][starty + i]);
		}
//		System.out.println(rud);
		return rdd;
	}

	List<Integer> RUD(int x, int y) {
		int startx = 0;
		int starty = 0;
		if (x + y < height) {
			startx = 0;
			starty = x + y;
		} else {
			startx = height;
			starty = 2 * (x + y - height);
		}
		List<Integer> rud = new ArrayList<Integer>();

//		for (int i = 0; i < starty + startx; i++) {
		try {
			for (int i = 0; i < height; i++) {
				rud.add(arr2D[starty -i][startx + i]);
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			return rud;
		}
		return rud;
	}

	void check(List<Integer> a) {
		System.out.println(a);
		List<List<Integer>> result = new ArrayList<>();
		if (a.size() > 0) {
			List<Integer> temp = new ArrayList<>();
			temp.add(a.get(0));
			for (int i = 1; i < a.size(); i++) {
				if (a.get(i) != a.get(i - 1)) {
					result.add(temp);
					temp = new ArrayList<>();
				}
				temp.add(a.get(i));
			}
		}

		for (int i = 0; i < result.size(); i++) {
			if (result.get(i).contains(0)) {
				result.remove(i);
			}
		}
		System.out.println(result);
		String winner = "";
		if (flag_wb == true) {
			winner = "흑";
		} else {
			winner = "백";
		}

		for (int i = 0; i < result.size(); i++) {
			if (result.get(i).size() == 5) {
				JOptionPane.showMessageDialog(null, winner + "승리!");
				reset();
			}
		}
	}
}
