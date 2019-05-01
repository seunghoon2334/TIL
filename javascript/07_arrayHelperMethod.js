// 1. 배열 반복하면서 출력
    const avengers = ['캡틴아메리카', '닥터스트레인지', '토르', '헐크', '블랙위도우', '스파이더맨', '블랙팬서']
    for (let hero of avengers) {
        console.log(hero)
    }
    avengers.forEach(hero => console.log(hero))
    avengers.forEach( function(hero) {
        console.log(hero)
    })
    // 2. map
    const numbers = [1, 2, 3]
    const strNumbers = numbers.map(number => String(number))
    console.log(strNumbers)
    const squreNumbers = numbers.map(number => number * number)
    const squreNumbers2 = numbers.map(function(number) {
        return number*number
    })
    console.log(squreNumbers)
    console.log(squreNumbers2)
    const vt = [
        {'velocity': 40, 'time': 50},
        {'velocity': 100, 'time': 60},
        {'velocity': 20, 'time': 1000},
    ]
    const distances = vt.map(object => object.velocity * object.time)
    console.log(distances)

    // 3. filter
    const nums = [1, 5, 6, 8]
    const evenNums = nums.filter(num => num%2 === 0)
    const oddNums = nums.filter(num => num%2 === 1)
    console.log(evenNums)
    console.log(oddNums)
    const drinks = [
        {type: 'caffeine', name: 'cold brew'},
        {type: 'caffeine', name: 'green tea'},
        {type: 'juice', name: 'orange'},
        {type: 'juice', name: 'mango'}
    ]
    const noncaffeine = drinks.filter(drink => drink.type !== 'caffeine').map(drink => drink.name)
    console.log(noncaffeine)

    // 4. reduce
    const reduceNum = [1, 5, 6]
    const reduceResult = reduceNum.reduce((result, num) => result += (num*10), 0)
    console.log(reduceResult)

    // 5. find
    const dc = ['슈퍼맨', '배트맨', '샤잠', '조커']
    const villain = dc.find(name => name === '조커')
    console.log(villain)