let result = add(1, 3)
// 1. 함수 선언식
function add(num1, num2) {
    return num1+num2
}
console.log(add(1, 3))
console.log(result)
// 2. 함수 표현식
let add2 = function (num1, num2) { // 익명함수
    return num1+num2
}
console.log(add2(1, 3))

// 3. ES6+ Arrow Function
let sub = (num1, num2) => {
    return num1-num2
}

// 인자가 하나인 경우, () 생략가능
// 단순 리턴인 경우, {} 및 리턴 키워드 생략 가능
let greeting = name => `${name}, 안녕!`
console.log(greeting('피카'))

let mul = (num1, num2) => num1 * num2
console.log(mul(1, 4))

// 인자가 없는 경우에는 () 작성
let hello = () => 'hello, world'

// object 리턴 시 반드시 () 묶어서 작성
let me = (name, age) => ({name, age})
console.log(me('hi', 3))

// 만약, default args (기본인자)
let bongjour = (name='피자') => `${name}, bongjour`

// 4. 익명 함수
(function (num) {return num*num})

// 5. 즉시 실행 함수 (익명함수 + 호출) - IIFE (Immediately Invoked Function Expression)
( num => num*num )(5)




let negative = (num) => -1 * num

let gutenTag = () => 'Guten Tag'

let vietnam = (member) => {
    member_base = '갸라도스'
    return `${member_base}와 ${member}가 베트남에 가요.`
}

console.log(negative(-3))
console.log(gutenTag())
console.log(vietnam('꼬부기'))

