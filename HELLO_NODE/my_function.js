function showDan(dan) {
	console.log(`${dan}단`)
	for(let i=1;i<=9;i++){
		console.log(`${dan} * ${i} = ${dan*i}`)
	}
}

showDan(7)