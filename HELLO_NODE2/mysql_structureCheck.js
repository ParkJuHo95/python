var mysql = require('mysql');

var connection = mysql.createConnection({
	host: 'localhost',
	user: 'root',
	port: 3305,
	password: 'python',
	database: 'python'
});

connection.connect(); // mysql과 연결


var sql = "insert into emp values('7','1','1','1')";
connection.query(sql,(error,result)=>{			//java의 thread 개념
	console.log(result.affectedRows);
	console.log('안쪽1')
});

console.log('바깥쪽1')
connection.end();
console.log('바깥쪽2')

