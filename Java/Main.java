import java.util.Scanner;

public class Main {
    public int max(int a, int b) {
        if (a >= b) {
            return a;
        } else {
            return b;
        }
    }

    public static void main(String[] args) {
        int time, size, count = 0;
        int[] money = new int[100];
        Main m = new Main();
        Scanner in = new Scanner(System.in);
        time = in.nextInt();
        size = in.nextInt();
        for (int i = 0; i < size; i += 1) {
            money[i] = in.nextInt();
        }
        for (int j = 0; j < size; j += time) {
            count += m.max(0, money[j + time] - money[j]);
        }
        System.out.println(count);
    }
}
