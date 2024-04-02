<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
	function fn_add(){
		document.frm.submit();
	}
</script>
</head>
<body>
	<form action="emp_add" name="frm" method="post">
		<table border="1">
			<tr> <th>사번</th><td><input name="e_id" type="text"></td> </tr>
			<tr> <th>이름</th><td><input name="e_name" type="text"></td> </tr>
			<tr> <th>성별</th><td><input name="gen" type="text"></td> </tr>
			<tr> <th>주소</th><td><input name="addr" type="text"></td> </tr>
			<tr> <td colspan=2> <button onclick="fn_add()">저장</button></td> </tr>
		</table>
	</form>
</body>
</html>