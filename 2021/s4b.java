// https://dmoj.ca/problem/ccc21s4/editorial
//
// Python wouldn't cut it, so I learned Java to have
// a rematch with this problem :P

import java.io.*;
import java.util.*;

class Main {
    static final int MY_INF = 9_999_999;

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);
    static StringTokenizer line;

    static int N, W, D;
    static List<List<Integer>> adjs = new ArrayList<>();  // 1-indexed
    static int[] route;

    static int nextInt() throws IOException {
        while (line == null || !line.hasMoreTokens()) {
            line = new StringTokenizer(in.readLine().trim());
        }

        return Integer.parseInt(line.nextToken());
    }

    static void increment(SortedMap<Integer, Integer> bag, int key) {
        bag.put(key, bag.getOrDefault(key, 0) + 1);
    }

    static void decrement(SortedMap<Integer, Integer> bag, int key) {
        int count = bag.getOrDefault(key, 0);

        if (count > 1) {
            bag.put(key, count - 1);
        } else {
            bag.remove(key);
        }
    }

    static Map<Integer, Integer> getMinDistsToSchool() {
        Map<Integer, Integer> dist = new HashMap<>();
        Queue<Integer> dq = new ArrayDeque<>();

        dist.put(N, 0);  // node N is school
        dq.add(N);

        while (!dq.isEmpty()) {
            int curr = dq.poll();

            for (int adj : adjs.get(curr)) {
                int tentative = dist.get(curr) + 1;

                if (tentative < dist.getOrDefault(adj, MY_INF)) {
                    dist.put(adj, tentative);
                    dq.add(adj);
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) throws IOException {
        N = nextInt();
        W = nextInt();
        D = nextInt();

        for (int i = 0; i <= N; i++) {
            adjs.add(new ArrayList<>());
        }

        for (int i = 0; i < W; i++) {
            int u = nextInt();
            int v = nextInt();

            // Inverting dir so we can BFS *from* school.
            adjs.get(v).add(u);
        }

        route = new int[N];

        for (int i = 0; i < N; i++) {
            route[i] = nextInt();
        }

        Map<Integer, Integer> minDistsToSchool = getMinDistsToSchool();

        // We use a Map to keep count of duplicate candidate times.
        // This prevents deletion of equal candidates when swapping.
        SortedMap<Integer, Integer> candidates = new TreeMap<>();

        for (int i = 0; i < N; i++) {
            increment(candidates, i + minDistsToSchool.getOrDefault(route[i], MY_INF));
        }

        for (int i = 0; i < D; i++) {
            int a = nextInt() - 1;
            int b = nextInt() - 1;

            decrement(candidates, a + minDistsToSchool.getOrDefault(route[a], MY_INF));
            decrement(candidates, b + minDistsToSchool.getOrDefault(route[b], MY_INF));

            increment(candidates, b + minDistsToSchool.getOrDefault(route[a], MY_INF));
            increment(candidates, a + minDistsToSchool.getOrDefault(route[b], MY_INF));

            out.println(candidates.firstKey());

            int temp = route[a];
            route[a] = route[b];
            route[b] = temp;
        }

        in.close();
        out.close();
    }
}
