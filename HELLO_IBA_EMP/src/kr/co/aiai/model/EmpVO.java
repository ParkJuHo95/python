package kr.co.aiai.model;

public class EmpVO {
	private int e_id = 0;
	private String e_name = "";
	private String gen = "";
	private String addr = "";

	
	public int getE_id() {
		return e_id;
	}
	public void setE_id(int e_id) {
		this.e_id = e_id;
	}
	public String getE_name() {
		return e_name;
	}
	public void setE_name(String e_name) {
		this.e_name = e_name;
	}
	public String getGen() {
		return gen;
	}
	public void setGen(String gen) {
		this.gen = gen;
	}
	public String getAddr() {
		return addr;
	}
	public void setAddr(String addr) {
		this.addr = addr;
	}
	@Override
	public String toString() {
		return "Emp [e_id=" + e_id + ", e_name=" + e_name + ", gen=" + gen + ", addr=" + addr + "]";
	}
	
	
	
}
