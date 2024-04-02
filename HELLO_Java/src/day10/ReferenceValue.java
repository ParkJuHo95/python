package day10;

public class ReferenceValue {
	
	static void change(int a) {
		a = 3;
	}
	static void change(int[] arr) {
		arr[0] = 4;
	}
	static void change(String s) {
		s = "def";
	}
	
	public static void main(String[] args) {
		
		int a = 1;
		int[] arr = {2};
		String s = "abc";
		System.out.println("a:"+a);
		System.out.println("arr[0]:"+arr[0]);
		
		change(a);
		change(arr);
		change(s);
		
		System.out.println("a:"+a);
		System.out.println("arr[0]:"+arr[0]);
		System.out.println("s:"+s);
		
	}
}
