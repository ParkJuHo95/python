var mysql = require('sync-mysql');

var connection = new mysql({
	host: 'localhost',
	user: 'root',
	password: 'python',
	port: 3305,
	database: 'python'
});

let result = connection.query("delete from emp where e_id='3'");
//let result = connection.query('SELECT * from emp');

console.log(result.affectedRows);