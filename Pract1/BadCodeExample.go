package main
import (
	"fmt"
	"time"
)
// func1 не говорить про те, що вона робить
func func1(a int, b int) int {
	if a > b {
		return a * 2
	} else {
		return b * 2
	}
}
// неясне іменування змінної
func calculate(c int, t int) {
	var x = time.Now().Unix()
	// виводить результат на екран, але не повертає
	fmt.Println(func1(c, t), x)
}
func main() {
	calculate(4, 7)
}

// Імена занадто короткі та незрозумілі
func f(a, b int) int {
    return a + b
}

var x int
x = 10


// Ініціалізація змінних (поганий приклад):
// Неініціалізовані змінні
var count int
if condition {
    count += 1
}


// Пакет (Package)

// Неправильне іменування пакету, що не відповідає суті
package util

func Calculate(a, b int) int {
    return a + b
}


// Функція (Function)

package main

func process(a, b int) int {
    return a * b
}


// Файл (File)

package main

func calculateSum(a, b int) int {
    return a + b
}


// Іменування змінних і функцій

package main

var x, y int

func f(a, b int) int {
    return a + b
}

// Ініціалізація змінних

package main

var total int

func main() {
    if condition {
        total++
    }
}


// Коментарі

package main

func calculate(a, b int) int {
    // Робимо щось
    return a * b
}

// Рефакторинг

package main

func processNumbers(a, b, c int) int {
    if a > b && b > c {
        return a * b * c
    }
    return a + b + c
}


// Оптимізація продуктивності через рефакторинг

package main

func findMax(numbers []int) int {
    max := 0
    for i := 0; i < len(numbers); i++ {
        if numbers[i] > max {
            max = numbers[i]
        }
    }
    return max
}


// Поганий код:

package main

func printUserInfo(name string, age int) {
    println("Name:", name)
    println("Age:", age)
}

func printEmployeeInfo(name string, age int, position string) {
    println("Name:", name)
    println("Age:", age)
    println("Position:", position)
}
