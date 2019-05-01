const firstName = 'happy'
const lastName = 'hacking'
const name = firstName + lastName
// document.write('<h1>' + name + '</h1>')
// ES6+ : Template literal(템플릿 문자열)
document.write(`<h1>${name}</h1>`)

let userName = prompt('너 누구냐?')
// let message = `<h1>${userName}</h1>`
// document.write(message)

// 자바스크립트에서는 ===이 파이썬의 ==과 같은 비교 연산자이다.
// === : 일치함을 비교(값, 타입)
// == : 동등함을 비교(값) : 타입이 암묵적 변환
// 123 == '123': true

if (userName === '보노') {
    message = '<h1>보노는 나가있어.</h1>'
} else if (userName === '보노보노') {
    message = `<h1>${username} 일하자!</h1>`
} else {
    message = `<h1>${userName} 수업듣자`
}
document.write(message)