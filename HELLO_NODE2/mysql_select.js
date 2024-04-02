var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	port: 3305,
	password: 'python',
	database: 'python'
});

connection.connect(); // mysql과 연결

var sql = 'select * from emp';
connection.query(sql, function(err, rows, fields) {
	if (err) {
		console.error('error connecting: ' + err.stack);
	}
	console.log(rows);
});
connection.end();

