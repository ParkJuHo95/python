var mysql = require('sync-mysql');

class DaoEmp {
	constructor(){
		this.conn = new mysql({
			host: 'localhost',
			user: 'root',
			password: 'python',
			port: 3305,
			database: 'python'
		});	
	}
	
	selectList(){
		return this.conn.query('select * from emp');
	}
	select(e_id){
		var list = this.conn.query(`select * from emp where e_id = ${e_id}`)
		return list[0]
	}
	insert(e_id,e_name,gen,addr){
		var sql = `
			insert into emp
			values(
				${e_id},
				'${e_name}',
				'${gen}',
				'${addr}'
			)
		`
		var cnt = this.conn.query(sql)
		return cnt;
	}
	update(e_id,e_name,gen,addr){
		var sql = `
			UPDATE emp 
			set 
				e_name = '${e_name}', 
				gen = '${gen}', 
				addr = '${addr}'  
			WHERE 
				e_id = ${e_id};
		`
		var cnt = this.conn.query(sql)
		return cnt;
	}
	delete(e_id){
		var sql = `
			DELETE FROM emp 
			WHERE e_id=${e_id}
		`
		var cnt = this.conn.query(sql)
		return cnt;
	}
	
}

module.exports = DaoEmp;

if (require.main === module) {
	var dao = new DamEmp();
	var result = dao.selectList();
	console.log(result)
}
