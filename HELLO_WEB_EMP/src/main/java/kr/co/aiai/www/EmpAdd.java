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
 * Servlet implementation class EmpAdd
 */
@WebServlet("/emp_add")
public class EmpAdd extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String emp_id = request.getParameter("e_id");
		int e_id = Integer.parseInt(emp_id);
		String e_name = request.getParameter("e_name");
		System.out.println(e_name);
		String gen = request.getParameter("gen");
		String addr = request.getParameter("addr");
		Emp vo = new Emp(e_id, e_name, gen, addr);
		
		EmpDao dao = new EmpDao();
		int cnt = -1;
		try {
			if(dao.select(e_id) == null) {
				try {
					cnt = dao.insert(vo);
				} catch (SQLException e) {
					e.printStackTrace();
				}
			} else {
				cnt = 20;
			}
		} catch (SQLException e1) {
			e1.printStackTrace();
		}
		
		request.setAttribute("cnt", cnt);
		request.getRequestDispatcher("emp_add_act.jsp").forward(request, response);
	}

}
