package kr.co.aiai.www;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.model.Emp;

@WebServlet("/emp_list")
public class EmpList extends HttpServlet{

	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{
//		PrintWriter out = resp.getWriter();
//		out.print("EMPLIST");
//		req.getRequestDispatcher("/emp_list.jsp").forward(req, resp);
//		RequestDispatcher rd = req.getRequestDispatcher("/emp_list.jsp");
//		String a = "홍길동";
//		ArrayList<Emp> list = new ArrayList<Emp>();
//		list.add(new Emp(1,"1","1","1"));
//		list.add(new Emp(2,"2","2","2"));
//		req.setAttribute("name", a);

//		
		req.setCharacterEncoding("UTF-8");
		EmpDao dao = new EmpDao();
		ArrayList<Emp> list = new ArrayList<Emp>();
		try {
			list = (ArrayList<Emp>)dao.selectList();
		} catch (SQLException e) {
		}
//		rd.forward(req, resp);
		req.setAttribute("list", list);
		resp.setCharacterEncoding("UTF-8");
		req.getRequestDispatcher("/emp_list.jsp").forward(req, resp);
	}

	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		doGet(req, resp);
	}
}
