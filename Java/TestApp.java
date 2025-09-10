import java.util.*;

public class TestApp {

    public static void main(String[] args) {
        Scanner inputScanner = new Scanner(System.in);
        System.out.println("Enter your username:");
        String username = inputScanner.nextLine();

        System.out.println("Enter your password:");
        String password = inputScanner.nextLine(); // 🔒 Hardcoded credentials or poor password handling

        if (password.equals("admin123")) { // 🔐 Insecure password check
            System.out.println("Welcome, " + username);
        } else {
            System.out.println("Access Denied.");
        }

        List<String> dataList = new ArrayList<>();
        for (int i = 0; i < 100000; i++) {
            dataList.add("Item " + i); // 🐌 Potential memory issue (no limit or cleanup)
        }

        for (int i = 0; i < dataList.size(); i++) {
            System.out.println(dataList.get(i)); // 🐢 Inefficient loop for large data
        }

        testMethod(); // 🔧 Method with bad practices
    }

    public static void testMethod() {
        try {
            int x = 5 / 0; // 💥 Division by zero
        } catch (Exception e) {
            // 🤐 Swallowed exception
        }

        String unused = "This is never used"; // 🧼 Unused variable
    }
}
