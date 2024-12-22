# bad code expample
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


# Good code example

package main

import (
	"fmt"
	"time"
)

// multiplyGreaterNumber обчислює найбільше число і множить його на 2
func multiplyGreaterNumber(num1 int, num2 int) int {
	if num1 > num2 {
		return num1 * 2
	}
	return num2 * 2
}

// calculateAndPrint обчислює найбільше число і виводить результат разом із поточним часом
func calculateAndPrint(value1 int, value2 int) {
	currentTimestamp := time.Now().Unix()
	result := multiplyGreaterNumber(value1, value2)
	fmt.Printf("Result: %d, Timestamp: %d\n", result, currentTimestamp)
}

func main() {
	calculateAndPrint(4, 7)
}

// Імена функцій і змінних описують їх призначення
func addNumbers(firstNumber, secondNumber int) int {
    return firstNumber + secondNumber
}

var userAge int
userAge = 25


// Ініціалізація змінних (гарний приклад):

// Ініціалізація змінної при оголошенні
count := 0
if condition {
    count++
}


// Пакет (Package)

// Пакет чітко вказує, що він обробляє математичні операції
package mathutils

func Add(a, b int) int {
    return a + b
}


// Функція (Function)

package main

func multiplyNumbers(firstNumber, secondNumber int) int {
    return firstNumber * secondNumber
}


// Файл (File)

package main

func calculateSum(a, b int) int {
    return a + b
}


// Іменування змінних і функцій

package main

var length, width int

func calculateArea(length, width int) int {
    return length * width
}

// Ініціалізація змінних

package main

var total int = 0

func main() {
    if condition {
        total++
    }
}

// Коментарі

package main

// calculateArea обчислює площу прямокутника
func calculateArea(length, width int) int {
    return length * width
}


// Рефакторинг

package main

// isDescending перевіряє чи йдуть числа в порядку спадання
func isDescending(a, b, c int) bool {
    return a > b && b > c
}

// calculateProduct обчислює добуток чисел
func calculateProduct(a, b, c int) int {
    return a * b * c
}

// processNumbers виконує основну операцію
func processNumbers(a, b, c int) int {
    if isDescending(a, b, c) {
        return calculateProduct(a, b, c)
    }
    return a + b + c
}


// Гарний код после рефакторинга:

package main

func findMax(numbers []int) int {
    max := numbers[0]
    for _, num := range numbers {
        if num > max {
            max = num
        }
    }
    return max
}

// Гарний код после рефакторинга:


package main

func printPersonInfo(name string, age int, additionalInfo ...string) {
    println("Name:", name)
    println("Age:", age)
    for _, info := range additionalInfo {
        println(info)
    }
}

func main() {
    printPersonInfo("John", 30)
    printPersonInfo("Alice", 25, "Position: Engineer")
}
