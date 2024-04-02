var DaoEmp = require("./daoemp.js");
var de = new DaoEmp();

//var list = de.select(1);
//console.log(list)
//var cnt = de.insert(5,5,5,5);
//var cnt = de.update(5,4,4,4);
var cnt = de.delete(5);
console.log(cnt)