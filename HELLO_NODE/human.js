var Animal = require("./animal.js");

class Human extends Animal {
	constructor(){
		super();
		this.asset = 0;
	}
	
	goldspoon() {
		this.asset = 10000000000;
	}
}

module.exports = Human;

if (require.main === module) {
	var human = new Human();
	human.named('김김김')
	human.goldspoon()
	console.log(human.name)
	console.log(human.asset)
}
