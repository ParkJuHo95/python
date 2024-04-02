package kr.co.aiai.dao;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import com.ibatis.sqlmap.client.SqlMapClient;

import kr.co.aiai.ibatis.MySqlMapper;
import kr.co.aiai.model.EmpVO;


public class EmpDao {
	private static SqlMapClient sqlMapper;

	public EmpDao() {
		sqlMapper = MySqlMapper.getSqlMapper();
	}

	public List<EmpVO> selectList() throws SQLException {
		return sqlMapper.queryForList("selectList");
	}

	public EmpVO select(int e_id) throws SQLException {
		return (EmpVO) sqlMapper.queryForObject("select", e_id);
	}

	public int insert(EmpVO vo) throws SQLException {
		return sqlMapper.update("insert", vo);
	}

	public int update(EmpVO vo) throws SQLException {
		return sqlMapper.update("update", vo);
	}

	public int delete(int e_id) throws SQLException {
		return sqlMapper.update("delete", e_id);
	}

	public static void main(String[] args) throws SQLException {
		EmpDao dao = new EmpDao();
		List<EmpVO> list = (List<EmpVO>) dao.selectList();
		
		for(int i=0; i<list.size();i++) {
			EmpVO temp = list.get(i);
			System.out.print(temp.getE_id() +"\t");
			System.out.print(temp.getE_name() +"\t");
			System.out.print(temp.getGen()+ "\t");
			System.out.print(temp.getAddr()+ "\n");
		}
		
		EmpVO cnt = dao.select(1);
		System.out.println(cnt);
		
		EmpVO vo = new EmpVO();
		vo.setE_id(4);
		vo.setE_name("9");
		vo.setGen("9");
		vo.setAddr("9");
//		int cnt1 = dao.insert(vo);
		int cnt2 = dao.update(vo);
//		System.out.println("insert : "+cnt1);
		System.out.println("update : "+cnt2);
		
//		int cnt3 = dao.delete(4);
		
	}
}















