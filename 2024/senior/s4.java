import java.util.*;

public class s4 {
    static HashSet<Integer> seen = new HashSet<>();
    static HashMap<Integer, ArrayList<Integer[]>> graph = new HashMap<>();
    static char[] paint;

    static void dfs(int node, char color) {
        for (Integer[] neighbor : graph.get(node)) {
            int neighborNode = neighbor[0];

            if (!seen.contains(neighborNode)) {
                seen.add(neighborNode);
                paint[neighbor[1]] = color;
                dfs(neighborNode, color == 'R' ? 'B' : 'R');
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        sc.nextInt();

        int m = sc.nextInt();

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());

            graph.get(a).add(new Integer[] {b, i});
            graph.get(b).add(new Integer[] {a, i});
        }

        sc.close();
        paint = new char[m];
        Arrays.fill(paint, 'G');

        for (int node : graph.keySet()) {
            if (!seen.contains(node)) {
                seen.add(node);
                dfs(node, 'R');
            }
        }

        System.out.println(new String(paint));
    }
}