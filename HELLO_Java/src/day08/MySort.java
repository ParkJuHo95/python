package day08;

import java.util.Arrays;

public class MySort {
	public static void main(String[] args) {
		int[] arr = { 6, 5, 4, 3, 2, 1 };

		for (int i = 0; i < 6; i++) {
			for (int j = 0; j < 6; j++) {
				int a = arr[i];
				int b = arr[j];
				if (a < b) {
					arr[i] = b;
					arr[j] = a;
				}

			}
		}
		System.out.println(Arrays.toString(arr));
	}
}
