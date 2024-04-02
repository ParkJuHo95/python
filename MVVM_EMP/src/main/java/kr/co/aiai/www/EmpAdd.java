package kr.co.aiai.www;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.util.AjaxUtil;
import kr.co.aiai.vo.EmpVO;

@WebServlet("/emp_add")
public class EmpAdd extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int e_id = Integer.parseInt(request.getParameter("e_id"));
		String e_name = request.getParameter("e_name");
		String gen = request.getParameter("gen");
		String addr = request.getParameter("addr");
		
		EmpDao dao = new EmpDao();
		EmpVO vo = new EmpVO(e_id, e_name, gen, addr);
		
		try {
			if(dao.select(e_id) != null) {
				int cnt = -20;
				AjaxUtil.responseJson(response, cnt+"");
			} else {
				int cnt = dao.insert(vo);
				AjaxUtil.responseJson(response, cnt+"");
			}
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
