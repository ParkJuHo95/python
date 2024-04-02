package day20;

public class ThreadTest03 {
	
	public static void printNum() {
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				for(int i=1;i<10000;i++) {
					System.out.print(i);
					if(i%100==0) {
						System.out.println();
					}
				}
				System.out.println("HELLO1");
			}
		}).start();

	}
	public static void printAscii() {
		new Thread(new Runnable() {
			
			@Override
			public void run() {
				for(int i=1;i<10000;i++) {
					System.out.print((char)i);
					if(i%100==0) {
						System.out.println();
					}
				}
				System.out.println("HELLO2");
			}
		}).start();

	}
	
	public static void main(String[] args) {
		printNum();
		printAscii();
		System.out.println("HELLO3");
	}
}
