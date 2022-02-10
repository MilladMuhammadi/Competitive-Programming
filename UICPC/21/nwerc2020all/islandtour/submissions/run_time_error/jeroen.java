import java.io.*;
import java.util.*;

public class jeroen {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] dst = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int[][] p = new int[3][n];
		for(int i = 0; i < 3; i++)
			p[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		// Precompute start and end times for k when person i starts at position j
		int[][][] start = new int[3][n][n];
		int[][][] end = new int[3][n][n];
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < n; j++) {
				int s = 0;
				for(int k = 0; k < n; k++) {
					start[i][j][(j+k)%n] = s;
					s += p[i][(j+k)%n];
					end[i][j][(j+k)%n] = s;
					s += dst[(j+k)%n];
				}
			}
		}

		// This looks terrible, but it is in O(n^3)
		// For each pair of persons we compute where
		// they could start without overlapping times.
		boolean[][][][] can = new boolean[3][3][n][n];
		for(int p1 = 0; p1 < 3; p1++) {
			for(int p2 = p1 + 1; p2 < 3; p2++) {
				for(int s1 = 0; s1 < n; s1++) {
					for(int s2 = 0; s2 < n; s2++) {
						can[p1][p2][s1][s2] = true;
						for(int i = 0; i < n; i++) {
							if(end[p1][s1][i] > start[p2][s2][i] && end[p2][s2][i] > start[p1][s1][i]) {
								can[p1][p2][s1][s2] = false;
							}
						}
					}
				}
			}
		}

		// Now bruteforce starting locations in O(n^3)
		for(int s1 = 0; s1 < 3; s1++) {
			for(int s2 = 0; s2 < 3; s2++) {
				for(int s3 = 0; s3 < 3; s3++) {
					if(can[0][1][s1][s2] && can[0][2][s1][s3] && can[1][2][s2][s3]) {
						System.out.println((s1+1) + " " + (s2+1) + " " + (s3+1));
						return;
					}
				}
			}
		}

		System.out.println("impossible");
	}
}
