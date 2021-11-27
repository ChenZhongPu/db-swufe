import java.sql.*;

public class JDBCDemo {
    public static void main(String[] args) throws ClassNotFoundException {
        // As of JDBC 4.0, all drivers that are found in the classpath are automatically loaded.
        // Therefore, we won't need this Class.forName part in modern environments
        Class.forName("org.postgresql.Driver");

        try (Connection con = DriverManager.getConnection("jdbc:postgresql://localhost:5432/mydb",
                "postgres", "")) {
//            testSelect(con);
            testSelect2(con);
//            testUpdate(con);
//            testInsert(con);
            // TODO: implement the delete
//            testDelete(con);
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }

    }

    private static void testSelect(Connection con) {
        try (Statement stmt = con.createStatement()) {
            String selectSql = "SELECT * FROM department";
            try (ResultSet resultSet = stmt.executeQuery(selectSql)) {
                while (resultSet.next()) {
                    System.out.println(resultSet.getString("dept_name"));
                    System.out.println(resultSet.getString("building"));
                    System.out.println(resultSet.getDouble("budget"));
                    System.out.println("----");
                }
            }
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
    }

    private static void testSelect2(Connection con) throws SQLException {
        String selectSql = "SELECT * FROM department";
        try (PreparedStatement pstmt = con.prepareStatement(selectSql)) {
            try (ResultSet resultSet = pstmt.executeQuery()) {
                while (resultSet.next()) {
                    System.out.println(resultSet.getString("dept_name"));
                    System.out.println(resultSet.getString("building"));
                    System.out.println(resultSet.getDouble("budget"));
                    System.out.println("----");
                }
            }
        }
    }

    private static void testUpdate(Connection con) throws SQLException {
        String updateSql = "UPDATE department SET budget = budget * 1.05 WHERE dept_name = ?";
        try (PreparedStatement pstmt = con.prepareStatement(updateSql)) {
            pstmt.setString(1, "Music");
            // The statement is executed with one of the same three methods described before:
            // executeQuery(), executeUpdate(), execute() without the SQL String parameter
            pstmt.execute();
        }
    }

    private static void testInsert(Connection con) throws SQLException {
        String insertSql = "INSERT INTO department(dept_name, building, budget) VALUES(?, ?, ?)";
        try (PreparedStatement pstmt = con.prepareStatement(insertSql)) {
            pstmt.setString(1, "Marx");
            pstmt.setString(2, "Watson");
            pstmt.setDouble(3, 80000.0);
            pstmt.execute();
        }
    }
}
