<%@page import="java.util.ArrayList"%>
<%@page import="java.util.List"%>
<%@page import="kr.co.aiai.model.Emp"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
td {
	text-align: center;
}
</style>
</head>
<body>
	<%
	ArrayList<Emp> list = (ArrayList<Emp>) request.getAttribute("list");
	if (list.size() > 0) {
	%>
	&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspEMP _ LIST
	<table border="1">
		<tr>
			<th>사번</th>
			<th>이름</th>
			<th>성별</th>
			<th>주소</th>
		</tr>
		<%
		for (int i = 0; i < list.size(); i++) {
		%>
		<tr>
			<td><a href="emp_detail?emp_id=<%=list.get(i).getE_id()%>"> <%=list.get(i).getE_id()%></a></td>
			<td><%=list.get(i).getE_name()%></td>
			<td><%=list.get(i).getGen()%></td>
			<td><%=list.get(i).getAddr()%></td>
		</tr>
		<%
		}
		}
		%>

	</table>	
	<button>추가</button>
	
	<script src="http://code.jquery.com/jquery-latest.min.js"></script>
	<script>
		$('button').click(function(){
			location.href = "emp_add.jsp";
		});
	</script>
</body>
</html>