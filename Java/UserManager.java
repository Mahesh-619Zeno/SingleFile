import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.util.Scanner;

public class UserManager {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine(); // ✅ User input

        System.out.print("Enter password: ");
        String password = scanner.nextLine(); // 🚨 Password in plain text

        authenticateUser(username, password);
    }

    public static void authenticateUser(String username, String password) {
        try {
            // 🚨 Hardcoded database credentials
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/testdb", "root", "root123"
            );

            Statement stmt = conn.createStatement();

            // 🚨 SQL Injection vulnerability
            String query = "SELECT * FROM users WHERE username = '" + username +
                           "' AND password = '" + password + "'";
            ResultSet rs = stmt.executeQuery(query);

            if (rs.next()) {
                System.out.println("Login successful for user: " + username);
            } else {
                System.out.println("Invalid credentials.");
            }

            // 🚨 Not closing resources
            // stmt.close();
            // conn.close();

        } catch (Exception e) {
            // 🚨 Swallowing exception without logging
        }
    }

    // 🚨 Unused method
    public static void logActivity(String activity) {
        String log = "[LOG] " + activity;
        // log is never used
    }
}
