package day20;

public class ThreadTest01 {
	public static void printNum() {
		for(int i=1;i<10000;i++) {
			System.out.print(i);
			if(i%100==0) {
				System.out.println();
			}
		}
	}
	
	public static void main(String[] args) {
		printNum();
	}
}
