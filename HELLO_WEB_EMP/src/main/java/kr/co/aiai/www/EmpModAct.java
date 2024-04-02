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
@WebServlet("/emp_mod_act")
public class EmpModAct extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		doPost(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String str_emp_id = request.getParameter("e_id");
		String emp_name= request.getParameter("e_name");
		String gen = request.getParameter("gen");
		String addr = request.getParameter("addr");
		int emp_id = Integer.parseInt(str_emp_id);
		Emp pvo = new Emp(emp_id, emp_name, gen, addr);
		EmpDao dao = new EmpDao();
		int cnt = -1;
		try {
			cnt = dao.update(pvo);
		} catch (SQLException e) {
			e.printStackTrace();
		}
		request.setAttribute("cnt", cnt);
		request.getRequestDispatcher("emp_mod_act.jsp").forward(request, response);
	}

}
