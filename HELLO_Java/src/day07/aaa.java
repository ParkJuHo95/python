package day07;

import java.util.ArrayList;
import java.util.List;

public class aaa {
    public static void main(String[] args) {
        int[] arr = {0, 0, 0, 1, 1, 1, 2, 2, 0, 1, 1, 0};
        List<List<Integer>> result = splitArray(arr);

        for (List<Integer> sublist : result) {
            System.out.println(sublist);
        }
    }

    public static List<List<Integer>> splitArray(int[] arr) {
        List<List<Integer>> result = new ArrayList<>();

        if (arr.length > 0) {
            List<Integer> sublist = new ArrayList<>();
            sublist.add(arr[0]);

            for (int i = 1; i < arr.length; i++) {
                if (arr[i] != arr[i - 1]) {
                    result.add(sublist);
                    sublist = new ArrayList<>();
                }
                sublist.add(arr[i]);
            }

            result.add(sublist); // 마지막 하위 리스트 추가
        }

        return result;
    }
}