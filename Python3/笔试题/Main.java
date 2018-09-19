import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        String[] list = input.split(' ');
        int N = Integer.parseInt(list[0]);
        int M = Integer.parseInt(list[1]);
        int[][] result;
        result = new int[N + 1][M + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {
                result[i][j] = -1;
            }
        }
        System.out.println(search(N, M));
        int search(int xi, int yi) {
            if (xi == 0 || yi == 0) {
                return 1;
            }
            if (result[xi][yi] >= 0) {
                return result[xi][yi];
            result[xi][yi] = search(xi - 1, yi) + search(xi, yi - 1);
            return result[xi][yi];
        }
    }
}
