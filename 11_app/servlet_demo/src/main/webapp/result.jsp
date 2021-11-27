<%--
  Created by IntelliJ IDEA.
  User: zhongpu
  Date: 2021/11/27
  Time: 下午2:42
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Result</title>
</head>
<body>
<table class="table table-success table-striped">
    <thead>
    <tr>
        <th scope="col">Department name</th>
        <th scope="col">Building</th>
        <th scope="col">Budget</th>
    </tr>

    <c:forEach var="dept" items="${results}">
        <tr>
            <td>${dept.name}</td>
            <td>${dept.building}</td>
            <td>${dept.budget}</td>
        </tr>
    </c:forEach>

    </thead>
</table>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

</body>
</html>