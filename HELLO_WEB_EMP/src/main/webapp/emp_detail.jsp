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
<style>
td {
	text-align: center;
}
</style>
<script>
	function fn_mod(){ 
		location.href = "emp_mod?emp_id=<%=vo.getE_id()%>"; 
	}
	function fn_del(){
		var flag = confirm("한번 지워진 데이터는 복구할 수 없습니다. 정말 삭제하시겠습니까?");
		if(flag){
			location.href = "emp_delete?emp_id=<%=vo.getE_id()%>"
		} else {
			return;
		}
	}
</script>

</head>
<body>

	EMP_DATAIL
	<table border=1>
		<tr>
			<th>사번</th>
			<td><%=vo.getE_id()%></td>
		</tr>
		<tr>
			<th>이름</th>
			<td><%=vo.getE_name()%></td>
		</tr>
		<tr>
			<th>성별</th>
			<td><%=vo.getGen()%></td>
		</tr>
		<tr>
			<th>주소</th>
			<td><%=vo.getAddr()%></td>
		</tr>
		<!-- 		<tr> <td colspan=2> <button>수정</button><button>삭제</button> </td> </tr> -->
		<tr>
			<td colspan=2>
				<input type="button" value="수정" onclick="fn_mod()">
				<input type="button" value="삭제" onclick="fn_del()">
			</td>
		</tr>


	</table>

	<!-- 	<script src="http://code.jquery.com/jquery-latest.min.js"></script> -->
	<!-- 	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script> -->
	<!-- 	<script> -->
	<!-- // 		$('button').eq(0).click(function(){ -->
	<%-- 			location.href = "emp_mod.jsp?emp_id=<%=vo.getE_id()%>";		 --%>
	<!-- // 		}); -->
	<!-- 	</script> -->

</body>
</html>