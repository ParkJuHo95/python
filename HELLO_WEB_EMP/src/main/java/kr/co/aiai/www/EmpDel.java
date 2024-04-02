package kr.co.aiai.www;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;

/**
 * Servlet implementation class EmpDel
 */
@WebServlet("/emp_delete")
public class EmpDel extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		EmpDao dao = new EmpDao();
		int emp_id = Integer.parseInt(req.getParameter("emp_id"));
		int cnt = -1;
		try {
			cnt = dao.delete(emp_id);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		req.setAttribute("cnt", cnt);
		req.getRequestDispatcher("emp_delete.jsp").forward(req, resp);
	}

	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		doGet(req, resp);
	}

}
