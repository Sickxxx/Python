# В этой программе реализован калькулятор для рациональных и комплексных чисел. #

1. В модуле ask прописаны 2 вопроса, которые задаются пользователю. С какими числами будем работать и какую операцию производить 
2. В модуле view описаны функции по выводу итога действия калькулятора и инициализации чисел, с которыми в дальнейшем будем работать. Здесь стоит обратить внимание на то, что комплексные и рациональные числа можно ввести двумя способами:
> Комплексные. Непосредственной записью без пробелов(например 2+5j) или вводом двух чисел(a, b) через запятую(функция преобразует их к виду a+bj)

> Рациональные. Можно ввести дробью без пробелов(пример 4/7) или цифрой с плавающей точкой(например 1.24)

3. Модуль model глобально инициализирует наши числа и проводит с ними необходимые математические действия
4. Модуль controller объединяет действия трех выше названных модулей и уже непосредственно реализует работу калькулятора. При этом возвращает необходимые переменные для дальнейшего логгирования
5. Модуль logger описывает функцию добавление информации в файл log.txt. Запись идет таким образом: время; (первое число) (действие) (второе число) = (результат)
6. Модуль ui имеет функцию вызова логирования с передачей в него параметров из модуля контроллер
7. Модуль main последний модуль который отвечает за запуск всей программы. Он запускает калькулятор и записывает логи наших действий