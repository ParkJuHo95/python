package kr.co.aiai.www;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.model.Emp;

/**
 * Servlet implementation class EmpUpdate
 */
@WebServlet("/emp_mod")
public class EmpMod extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String str_emp_id = request.getParameter("emp_id");
		int emp_id = Integer.parseInt(str_emp_id);
		EmpDao dao = new EmpDao();
		Emp vo = null;
		try {
			vo = dao.select(emp_id);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		request.setAttribute("vo", vo);
		request.getRequestDispatcher("emp_mod.jsp").forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
