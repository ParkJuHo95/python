<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 <%
int cnt = (int)(request.getAttribute("cnt"));
%>  
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
	var cnt = <%=cnt%>;
	console.log(cnt);
	if(cnt == 1) {
		alert('추가 성공!');
		location.href = "emp_list";
	} else if(cnt == 20) {
		alert('이미 등록된 사번입니다.')
		history.back();
	} else {
		alert('추가 실패....');
		history.back();
	}
</script>
</head>
<body>

</body>
</html>