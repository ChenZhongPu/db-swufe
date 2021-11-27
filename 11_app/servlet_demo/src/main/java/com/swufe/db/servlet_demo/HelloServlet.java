package com.swufe.db.servlet_demo;

import java.io.*;
import java.sql.Connection;
import java.sql.SQLException;

import jakarta.servlet.http.*;
import jakarta.servlet.annotation.*;

@WebServlet(name = "helloServlet", value = "/hello-servlet")
public class HelloServlet extends HttpServlet {
    private String message;

    public void init() {
        message = "Hello World!";
    }

    public void doGet(HttpServletRequest request, HttpServletResponse response) throws IOException {
        response.setContentType("text/html");

        // Hello
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h1>" + message + "</h1>");
        Connection conn = (Connection) this.getServletContext().getAttribute("pg-db");
        if (conn != null) {
            try {
                out.println(conn.getCatalog());
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        out.println("</body></html>");
    }

    public void destroy() {
    }
}