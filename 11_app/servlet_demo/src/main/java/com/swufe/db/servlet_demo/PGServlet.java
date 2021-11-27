package com.swufe.db.servlet_demo;

import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

@WebServlet(name = "PGServlet", value = "/hello")
public class PGServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        Connection conn = (Connection) this.getServletContext().getAttribute("pg-db");

        double budget = Double.parseDouble(request.getParameter("b"));

        String sql = "SELECT dept_name, building, budget FROM department WHERE budget > ?";
        List<Department> departments = new ArrayList<>();
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setDouble(1, budget);
            try (ResultSet resultSet = stmt.executeQuery()) {
                while (resultSet.next()) {
                    Department department = new Department();
                    department.setName(resultSet.getString("dept_name"));
                    department.setBuilding(resultSet.getString("building"));
                    department.setBudget(resultSet.getDouble("budget"));
                    departments.add(department);
                }
            }

        } catch (SQLException e) {

        }

        request.setAttribute("results", departments);
        request.getRequestDispatcher("/result.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}
