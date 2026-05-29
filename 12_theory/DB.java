import java.io.*;
import java.util.Scanner;

public class DB {
    static final String DB_NAME = "dog.db";

    static void store(String key, String value) throws IOException {
        try (var w = new FileWriter(DB_NAME, true)) {
            w.write(key + ":" + value + "\n");
        }
    }

    static String retrieve(String key) throws IOException {
        var db = new File(DB_NAME);
        if (!db.exists()) return null;
        String result = null;
        try (var r = new BufferedReader(new FileReader(db))) {
            String line;
            while ((line = r.readLine()) != null) {
                int sep = line.indexOf(':');
                if (sep != -1 && line.substring(0, sep).equals(key))
                    result = line.substring(sep + 1);
            }
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        System.out.println("Mini DB. Commands: PUT k,v | GET k | EXIT");
        var sc = new Scanner(System.in);
        while (true) {
            System.out.print("🐕> ");
            if (!sc.hasNextLine()) break;
            String line = sc.nextLine().strip();
            if (line.isEmpty()) continue;
            int sp = line.indexOf(' ');
            String cmd = (sp == -1 ? line : line.substring(0, sp)).toUpperCase();
            String arg = sp == -1 ? "" : line.substring(sp + 1).strip();
            switch (cmd) {
                case "EXIT" -> { return; }
                case "GET" -> {
                    if (arg.isEmpty()) { System.out.println("Usage: GET k"); continue; }
                    String val = retrieve(arg);
                    System.out.println(val != null ? val : "(not found)");
                }
                case "PUT" -> {
                    int comma = arg.indexOf(',');
                    if (comma == -1) { System.out.println("Usage: PUT k,v"); continue; }
                    store(arg.substring(0, comma).strip(), arg.substring(comma + 1).strip());
                }
                default -> System.out.println("Unknown command: " + cmd);
            }
        }
    }
}
