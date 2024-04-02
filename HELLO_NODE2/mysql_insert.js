var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	port: 3305,
	password: 'python',
	database: 'python'
});

connection.connect(); // mysql과 연결

//var sql = "delete from emp where e_id='2'";
var sql = "update emp set addr = '5' where e_id='2'";

//var sql = "insert into emp values('2','1','1','1')";
connection.query(sql,(error,result)=>{
	console.log(result.affectedRows);
});

var sql2 = 'select * from emp';
connection.query(sql2, function(err, rows, fields) {
	if (err) {
		console.error('error connecting: ' + err.stack);
	}
	console.log(rows);
});
connection.end();

