var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	port: 3305,
	password: 'python',
	database: 'python'
});

connection.connect(); // mysql과 연결

var e_id = '2';

var sql = `
		delete from emp
		where
			e_id = '${e_id}'
		`;
connection.query(sql,(error, result) => {
	console.log(result.affectedRows);
	
});
connection.end();

