const http = require('http');
const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const app = express();
var DaoEmp = require("./daoemp.js");
const de = new DaoEmp();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.static('static'))
app.set('view engine', 'ejs');
app.set('views', './views');

app.get('/', (req, res) => {
	res.send("Hello Express!");
})

app.get('/empList', (req, res) => {
	var list = de.selectList();
	res.send({list});
})

app.post('/empAdd', (req, res) => {
	var params = req.body;
	var e_id = params.e_id;
	var e_name = params.e_name;
	var gen = params.gen;
	var addr = params.addr;
	var cnt = de.insert(e_id,e_name,gen,addr);
	console.log(cnt);
	res.send({cnt:cnt});
})

app.get('/empSelectOne', (req, res) => {
	var e_id = req.query.e_id;
	var list = de.select(e_id);
	res.send(list);
})

app.post('/empMod', (req, res) => {
	var params = req.body;
	var e_id = params.e_id;
	var e_name = params.e_name;
	var gen = params.gen;
	var addr = params.addr;
	var cnt = de.update(e_id,e_name,gen,addr);
	console.log(cnt);
	res.send({cnt:cnt});
})

app.post('/empDel', (req, res) => {
	var params = req.body;
	var e_id = params.e_id;
	var cnt = de.delete(e_id);
	console.log(cnt);
	res.send({cnt:cnt});
})

app.listen(5000);	//port 번호