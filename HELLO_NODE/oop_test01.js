//import Animal from "./animal.js";		//==>바탕화면 js_export_import_method 참고 
//var Animal = require("./animal.js");
var Human = require("./human.js");

var human = new Human();
console.log(human.asset);
console.log(human.name);
human.named('김김김')
human.goldspoon()
console.log(human.name);
console.log(human.asset);