//export default class Animal {
class Animal {
	constructor(name) {
		this.name = "";
	}
	
	named(name) {
		this.name = name;
	}
}
module.exports = Animal;


if (require.main === module) {
	var animal = new Animal();
	animal.named('rabbit')
	console.log(animal.name)
}
