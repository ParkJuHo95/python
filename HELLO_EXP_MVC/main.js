const bodyParser = require('body-parser');
const express = require('express');
var DaoEmp = require("./daoemp.js");
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : false}));
app.set('view engine', 'ejs');
app.set('views', './views');
var de = new DaoEmp();

app.get('/', (req, res) => {
	res.redirect("/emplist");
})

app.get('/emplist', (req, res) => {
	let list = de.selectList();
	res.render('empList.ejs',{list:list})
})

app.get('/empOne', (req, res) => {
	var e_id = req.query.e_id
	var emp = de.select(e_id)
	res.render('empOne.ejs',{emp:emp})
})

app.get('/empModify', (req, res) => {
	var e_id = req.query.e_id
	var emp = de.select(e_id)
	res.render('empMod.ejs',{emp:emp})
})

app.get('/empModAct', (req, res) => {
	var params = req.query
	var e_id = params.e_id;
	var e_name = params.e_name;
	var gen = params.gen;
	var addr = params.addr;
	var cnt = de.update(e_id,e_name,gen,addr);
	res.render('empMod_act.ejs',{cnt:cnt.affectedRows});
})

app.get('/empAdd', (req, res) => {
	res.render('empAdd.ejs')
})

app.get('/empAddAct', (req, res) => {
	var params = req.query
	var e_id = params.e_id;
	var e_name = params.e_name;
	var gen = params.gen;
	var addr = params.addr;
	var cnt = de.insert(e_id,e_name,gen,addr);
	res.render('empAdd_act.ejs',{cnt:cnt.affectedRows })
})

app.get('/empDelete', (req, res) => {
	var e_id = req.query.e_id;
	var cnt = de.delete(e_id);
	res.render('empDel_act.ejs',{cnt:cnt.affectedRows})
})



app.listen(5000);	//port 번호