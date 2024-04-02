package day03;

public class MyMthod01 {
	public static void main(String[] args) {
		int sum = add(4, 2);
		int min = minus(4, 2);
		int mul = multiply(4, 2);
		double div = divide(4, 2);
		int rem = remain(4,2);

		System.out.println("sum : " + sum);
		System.out.println("min : " + min);
		System.out.println("multiply : " + mul);
		System.out.println("divide : " + div);
		System.out.println("remain : " + rem);
	}

	static int add(int a, int b) {
		return a + b;
	}

	static int minus(int a, int b) {
		return a - b;
	}

	static int multiply(int a, int b) {
		return a * b;
	}

	static double divide(int a, int b) {
		return (double) a / b;
	}

	static int remain(int a, int b) {
		return a % b;
	}

}
