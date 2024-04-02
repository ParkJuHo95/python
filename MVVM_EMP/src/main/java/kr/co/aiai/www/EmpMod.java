package kr.co.aiai.www;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.EmpDao;
import kr.co.aiai.util.AjaxUtil;
import kr.co.aiai.vo.EmpVO;

@WebServlet("/emp_mod")
public class EmpMod extends HttpServlet {
	private static final long serialVersionUID = 1L;
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String e_idS = request.getParameter("e_id");
		int e_id = Integer.parseInt(e_idS);
		String e_name = request.getParameter("e_name");
		String gen = request.getParameter("gen");
		String addr = request.getParameter("addr");
		EmpDao dao = new EmpDao();
		EmpVO vo = new EmpVO(e_id, e_name, gen, addr);
		
		try {
			int cnt = dao.update(vo);
			AjaxUtil.responseJson(response, cnt+"");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
