// 자바스크립트 데이터타입 - 원시타입(primitive type)
// Boolean(true, false), null, undefined. number, string

// 자바스크립트 object 표기법
let bono = {
    name: 'bonobono',
    age: 26,
    number: '010-bono-bono'
}
console.log(bono.name) // bonobono
console.log(bono.age) // 26
console.log(typeof bono) // object
console.log(typeof bono.name) // string
console.log(typeof [1, 2, 3]) // object
console.log(bono['name'])
console.log(bono['age'])

// ES6+
// 변수를 그대로 넣으면, 변수명: 값
let name = 'meta'
let stuffs = ['텀블러', '컵']
let meta = {
    name,
    stuffs
}

let jsonData = JSON.stringify(meta)
let jsonParse = JSON.parse(jsonData)