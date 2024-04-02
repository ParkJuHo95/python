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
var e_name = '6';
var gen = '6';
var addr = '6';

var sql = `
		update emp
		set
			e_name = '${e_name}',
			gen = '${gen}',
			addr = '${addr}'
		where
			e_id = '${e_id}'
		`;
connection.query(sql,(error, result) => {
	console.log(result);
});
connection.end();

