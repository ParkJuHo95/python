<%@page import="kr.co.aiai.model.Emp"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
Emp vo = (Emp) (request.getAttribute("vo"));
%>   
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>

<script type="text/javascript">
	function fn_mod_act(){
		document.frm.submit();
	}
</script>
</head>
<body>
	EMP_MOD
	<form name="frm" action="emp_mod_act" method="post">
		<table border="1">
			<tr> <th>사번</th><td><input type='text' name = "e_id" value='<%=vo.getE_id()%>' readonly></td> </tr>
			<tr> <th>이름</th><td><input type='text' name = "e_name" value='<%=vo.getE_name()%>'></td> </tr>
			<tr> <th>성별</th><td><input type='text' name = "gen" value='<%=vo.getGen()%>'></td> </tr>
			<tr> <th>주소</th><td><input type='text' name = "addr" value='<%=vo.getAddr()%>'></td> </tr>
			<tr> <td colspan=2> <button onclick="fn_mod_act()">저장</button></td> </tr>
		</table>
	</form>
</body>
</html>