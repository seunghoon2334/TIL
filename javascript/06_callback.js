// 배열을 받아서 다 더해주는 함수를 작성 해주세요.
// numberAddEach
const numberAddEach = numbers => {
    let sum = 0
    for (let number of numbers) {
        sum += number
    }
    return sum
}
console.log(numberAddEach([1,2,3]))
const numberSubEach = numbers => {
    let sum = 0
    for (let number of numbers) {
        sum -= number
    }
    return sum
}
console.log(numberSubEach([1,2,3]))
const numberMulEach = numbers => {
    let sum = 0
    for (let number of numbers) {
        sum *= number
    }
    return sum
}
console.log(numberMulEach([1,2,3]))

const numberEach = (numbers, calc) => {
    let result
    for (const number of numbers) {
        result = calc(number, result)
    }
    return result
}

const addEach = (number, result=0) => result + number
const subEach = (number, result=0) => result - number
const mulEach = (number, result=1) => result * number

console.log(numberEach([10,20,30], addEach))
console.log(numberEach([10,20,30], subEach))
console.log(numberEach([10,20,30], mulEach))
// 익명함수 + 콜백
console.log(numberEach([10,20,30], (number, result=0) => result + number))
console.log(numberEach([10,20,30], function(number, result=0) {
    return result + number
}))

let foods = ['빠삐코', '메로나', '돼지바']
foods.forEach(function(element, idx, foods) {
    console.log(element, idx, foods)
})
/*
자바스크립트의 함수는 일급 객체이다.
- 조건 -
1. 변수나 특정한 오브젝트에(배열) 함수를 저장할 수 잇따.
2. 함수의 인자로 전달할 수가 있어야 한다.
3. 함수 자체를 return 할 수 있어야 한다.
4. 이름과 상관없이 구별이 가능하다. (익명으로 표현 가능)
5. 동적으로 속성값(property) 할당이 가능하다.
*/

/* 
1. let, const

2. ==, ===

3. function
 + arrow function
 + 익명함수

=========================

'*'*Infinite : 콜백
*/
