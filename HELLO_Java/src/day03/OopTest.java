package day03;

public class OopTest {
	public static void main(String[] args) {
		Human hum = new Human();
		System.out.println("name : " + hum.name);
		System.out.println("asset : " + hum.asset);
		hum.named("전청조");
		hum.goldspoon();
		System.out.println("name : " + hum.name);
		System.out.println("asset : " + hum.asset);
	}
}
