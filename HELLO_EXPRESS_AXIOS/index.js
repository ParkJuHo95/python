const http = require('http');
const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.set('view engine', 'ejs');
app.set('views', './views');
//app.use('/static' ,express.static('static'))
app.use(express.static('static'))

app.get('/', (req, res) => {
	res.send("Hello Express!");
})
app.post('/ajax', (req, res) => {
	var result = req.body.menu;
	//res.send({ menu: result })
	res.json({ menu: result })
})

app.post('/fetch', (req, res) => {
	var result = req.body;
	console.log(result);
	res.json(result)
})

app.post('/axios', (req, res) => {
	var result = req.body;
	console.log(result);
	res.json(result)
	//res.send(result)
})


app.listen(5000);	//port 번호