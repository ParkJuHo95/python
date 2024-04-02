const http = require('http');
const bodyParser = require('body-parser');
const express = require('express');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : false}));
app.set('view engine', 'ejs');
app.set('views', './views');
app.use('/static' ,express.static('static'))

app.get('/', (req, res) => {
	res.send("Hello Express!");
})

app.get('/param', (req, res) => {
//	let menu = req.param("menu");
	let menu = req.query.menu;
	res.send("PARAM : "+menu);
})

app.post('/post', (req, res) => {
//	let menu = req.param("menu");
	let menu = req.body.menu;
	res.send("PARAM : "+menu);
})

app.get('/ejs', (req, res) => {
	var a = "홍길동";
	var b = ["전우치","홍길동"];
	var c = [
		{e_id:'1',e_name:'1',gen:'1',addr:'1'},
		{e_id:'2',e_name:'2',gen:'2',addr:'2'},
		{e_id:'3',e_name:'3',gen:'3',addr:'3'}
	]
	res.render("forward.ejs",{
		a : a,
		b : b,
		c : c
	});
})




app.get('/holl', (req, res) => {
	res.sendFile(__dirname + "/holl.html");
});

app.get('/sample', (req, res) => {
	res.sendFile(__dirname + "/form.html");
});

app.listen(5000);	//port 번호