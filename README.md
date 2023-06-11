# СЕМИНАР 1 Основы Python
1. Задание 1
    - Установили Python и IDE для работы
2. Задание 2
      - Работаем в командной строке (терминале ОС)
      - Создайте каталог для проекта first_project и разверните
      - виртуальное окружение Python в папке venv внутри каталога
      - Создайте третий каталог проекта project_new и разверните
      виртуальное окружение Python в папке venv_new внутри каталога
      - Для каждого проекта последовательно активируйте
      и деактивируйте виртуальное окружение
3. Задание 3
      - Активируем виртуальное окружение первого из трёх созданных проектов
   и устанавливаем в него модуль requests используя pip
      - Проверяем установку выводом списка модулей в консоль
      - Сохраняем список в файл, проверяем результат и выходим из окружения
      - Активируем виртуальное окружение второго из трёх созданных проектов
      и устанавливаем в него модуль flask используя pip
      - Проверяем установку выводом списка модулей в консоль
      Сохраняем список в файл и выходим из окружения
      - Активируем третье виртуальное окружение
      - Устанавливаем в него модули из первого и второго проекта используя
      ранее сохранённые в файлы списки модулей
      - Проверяем установку выводом списка модулей в консоль
4. Задание 4 
      - Работа в консоли в режиме интерпретатора Python.
      - Решите квадратное уравнение 5x2-10x-400=0 последовательно
   сохраняя переменные a, b, c, d, x1 и x2.
     - *Попробуйте решить уравнения с другими значениями a, b, c
5. Задание 5 
     - Работа в консоли в режиме интерпретатора Python.
     - Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
     - Используйте while и if.
     - Попробуйте разные значения e и n.
6. [Задание 6](Seminar_1/Task_1_6.py)  
     - Напишите программу, которая запрашивает год и проверяет его на високосность.
     - Распишите все возможные проверки в цепочке elif
     - Откажитесь от магических чисел
     - Обязательно учтите год ввода Григорианского календаря
     - В коде должны быть один input и один print
7. [Задание 7](Seminar_1/Task_1_7.py)  
     - Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
     - Для цифры верните её квадрат, например 5 - 25
     - Для двузначного числа произведение цифр, например 30 - 0
     - Для трёхзначного числа его зеркальное отображение, например 520 - 25
     - Если число не из диапазона, запросите новое число
     - Откажитесь от магических чисел
     - В коде должны быть один input и один print
8. [Задание 8](Seminar_1/Task_1_8.py)  
     - Нарисовать в консоли ёлку спросив
     - у пользователя количество рядов.
     - Пример результата:
     - Сколько рядов у ёлки? 5
9. [Задание 9](Seminar_1/Task_1_9.py)  
     - Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке
10. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_1/Task_1_10.py)
     - Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
     -  Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
     - Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
     - from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT) 

# СЕМИНАР 2 Простые типы данных
1. [Задание 1](Seminar_2/Task_2_1.py)
    - Создайте несколько переменных разных типов.
    - Проверьте к какому типу относятся созданные переменные
2. [Задание 2](Seminar_2/Task_2_2.py)
    - Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
    - ✔ порядковый номер начиная с единицы
    - ✔ значение
    - ✔ адрес в памяти
    - ✔ размер в памяти
    - ✔ хэш объекта
    - ✔ результат проверки на целое число только если он положительный
    - ✔ результат проверки на строку только если он положительный
    - Добавьте в список повторяющиеся элементы и сравните на результаты.
3. [Задание 3](Seminar_2/Task_2_3.py)
    - Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
    - ✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
   <br>
Дополнительно:
   <br>
    - ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
    - ✔ Избегайте магических чисел
    - ✔ Добавьте аннотацию типов где это возможно
    
4. [Задание 4](Seminar_2/Task_2_4.py)
    - Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
    - ✔ Диаметр не превышает 1000 у.е.
    - ✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
5. [Задание 5](Seminar_2/Task_2_5.py)
   - Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
   - ✔ Используйте комплексные числа
для извлечения квадратного корня.
6. [Задание 6](Seminar_2/Task_2_6.py)
   - Напишите программу банкомат.
   - ✔ Начальная сумма равна нулю
   - ✔ Допустимые действия: пополнить, снять, выйти
   - ✔ Сумма пополнения и снятия кратны 50 у.е.
   - ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
   - ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
   - ✔ Нельзя снять больше, чем на счёте
   - ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
   - операцией, даже ошибочной
   - ✔ Любое действие выводит сумму денег
7. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_2)
   - Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
   - ✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей. Для проверки своего
кода используйте модуль fractions.
   
# СЕМИНАР 3 Коллекции
1. [Задание 1](Seminar_3/Task_3_1.py)
    - Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
    - ✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков
2. [Задание 2](Seminar_3/Task_3_2.py)
    - Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
    - ✔ Целое положительное число
    - ✔ Вещественное положительное или отрицательное число
    - ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
    - ✔ Строку в нижнем регистре в остальных случаях
3. [Задание 3](Seminar_3/Task_3_3.py)
    - Создайте вручную кортеж содержащий элементы разных типов.
    - ✔ Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа
4. [Задание 4](Seminar_3/Task_3_4.py)
    - Создайте вручную список с повторяющимися элементами.
    - ✔ Удалите из него все элементы, которые встречаются дважды.
5. [Задание 5](Seminar_3/Task_3_5.py)
   - Создайте вручную список с повторяющимися целыми числами.
   - ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
   - ✔ Нумерация начинается с единицы.
6. [Задание 6](Seminar_3/Task_3_6.py)
   - Пользователь вводит строку текста. Вывести каждое слово с новой строки.
   - ✔ Строки нумеруются начиная с единицы.
   - ✔ Слова выводятся отсортированными согласно кодировки Unicode.
   - ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
7. [Задание 7](Seminar_3/Task_3_7.py)
   - Пользователь вводит строку текста.
   - ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
   - ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
   - ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
8. [Задание 8](Seminar_3/Task_3_8.py)
   - Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —  кортеж вещей. Ответьте на вопросы:
   - ✔ Какие вещи взяли все три друга
   - ✔ Какие вещи уникальны, есть только у одного друга
   - ✔ Какие вещи есть у всех друзей кроме одного  и имя того, у кого данная вещь отсутствует
   - ✔ Для решения используйте операции  с множествами. Код должен расширяться  на любое большее количество друзей.
9. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_3/Task_3_9.py)
   - Дан список повторяющихся элементов. Вернуть список  с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
   - ✔ В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
   - ✔ Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
   - ✔ *Верните все возможные варианты комплектации рюкзака.

# СЕМИНАР 4 Функции
1. [Задание 1](Seminar_4/Task_4_1.py)
    -  Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
    - ✔ Строки нумеруются начиная с единицы.
    - ✔ Слова выводятся отсортированными согласно кодировки Unicode.
    - Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
2. [Задание 2](Seminar_4/Task_4_2.py)
    - Напишите функцию, которая принимает строку текста.
    - ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
3. [Задание 3](Seminar_4/Task_4_3.py)
    - Функция получает на вход строку из двух чисел через пробел.
    - ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
    - ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

4. [Задание 4](Seminar_4/Task_4_4.py)
    - Функция получает на вход список чисел.
    - ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
    - ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.
5. [Задание 5](Seminar_4/Task_4_5.py)
   - Функция принимает на вход три списка одинаковой длины:
   - ✔ имена str,
   - ✔ ставка int,
   - ✔ премия str с указанием процентов вида «10.25%».
   - ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
   - ✔ Сумма рассчитывается как ставка умноженная на процент премии. 
6. [Задание 6](Seminar_4/Task_4_6.py)
   - Функция получает на вход список чисел и два индекса.
   - ✔ Вернуть сумму чисел между между переданными индексами.
   - ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

7. [Задание 7](Seminar_4/Task_4_7.py)
   - Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
   - ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
8. [Задание 8](Seminar_4/Task_4_8.py)
   - Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
   - ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
   - ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
9. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_4)
   - Напишите функцию для транспонирования матрицы
   - ✔ Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
   - ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.

# СЕМИНАР 5 Итераторы и генераторы
1. [Задание 1](Seminar_5/Task_5_1.py)
    -  Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
    - ✔второе и третье число являются ключами.
    - ✔первое число является значением для первого ключа.
    - ✔четвертое и все возможные последующие числа  хранятся в кортеже как значения второго ключа.

2. [Задание 2](Seminar_5/Task_5_2.py)
    - Самостоятельно сохраните в переменной строку текста.
    - ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
    - ✔ Напишите преобразование в одну строку. 

3. [Задание 3](Seminar_5/Task_5_3.py)
    - Продолжаем развивать задачу 2.
    - ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
    - ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

4. [Задание 4](Seminar_5/Task_5_4.py)
    - Создайте генератор чётных чисел от нуля до 100.
    - ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
    - ✔ Решение в одну строку.

5. [Задание 5](Seminar_5/Task_5_5.py)
   - Напишите программу, которая выводит на экран числа от 1 до 100.
   - ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
   - ✔ Вместо чисел, кратных пяти — слово «Buzz».
   - ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
   - ✔ *Превратите решение в генераторное выражение.

6. [Задание 6](Seminar_5/Task_5_6.py)
   - Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
   - ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
   - ✔ Для вывода результата используйте «принт» без перехода на новую строку.

7. [Задание 7](Seminar_5/Task_5_7.py)
   - Создайте функцию-генератор.
   - ✔ Функция генерирует N простых чисел, начиная с числа 2.
   - ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
нацело только на единицу и на себя».

8. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_5/Task_5_8.py)
   - Напишите функцию для транспонирования матрицы
   - ✔ Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
   - ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.

# СЕМИНАР 6 Модули
1. [Задание 1](Seminar_6/task1.py)
    - Вспомните какие модули вы уже проходили на курсе.
    - Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами.
    - (3-7 строк импорта).

2. [Задание 2](Seminar_6/task2.py) и [Задание 2](Seminar_6/my_pacage_task8/module_task2_task3.py) и [Задание 2](Seminar_6/my_pacage_task8/__init__.py)
    - Создайте модуль с функцией внутри.
    - Функци  принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
    - Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
    - Функция выводит подсказки “больше” и “меньше”.
    - Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

3. [Задание 3](Seminar_6/task3.py) и [Задание 3](Seminar_6/my_pacage_task8/module_task2_task3.py) и [Задание 3](Seminar_6/my_pacage_task8/__init__.py)
    - Улучшаем задачу 2.
    - Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
    - Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
    - Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.

4. [Задание 4](Seminar_6/task4_task5_task6.py) и [Задание 4](Seminar_6/my_pacage_task8/module_task4_task5_task6.py) и [Задание 4](Seminar_6/my_pacage_task8/__init__.py)
    - Создайте модуль с функцией внутри.
    - Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
    - Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

5. [Задание 5](Seminar_6/task4_task5_task6.py) и [Задание 5](Seminar_6/my_pacage_task8/module_task4_task5_task6.py) и [Задание 5](Seminar_6/my_pacage_task8/__init__.py)
   - Добавьте в модуль с загадками функцию, которая хранит словарь списков.
   - Ключ словаря - загадка, значение - список с отгадками.
   - Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

6. [Задание 6](Seminar_6/task4_task5_task6.py) и [Задание 65](Seminar_6/my_pacage_task8/module_task4_task5_task6.py) и [Задание 6](Seminar_6/my_pacage_task8/__init__.py)
   - Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и
число (номер попытки, с которой она угадана).
   - Функция формирует словарь с информацией о результатах отгадывания.
   - Для хранения используйте защищённый словарь уровня модуля.
   - Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря
в удобном для чтения виде.
   - Для формирования результатов используйте генераторное выражение.

7. [Задание 7](Seminar_6/task7.py) и [Задание 7](Seminar_6/my_pacage_task8/module_task7.py) и [Задание 7](Seminar_6/my_pacage_task8/__init__.py)
   - Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
   - Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
   - Для простоты договоримся, что год может быть в диапазоне [1, 9999].
   - Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
   - Проверку года на високосность вынести в отдельную защищённую функцию.

8. [Задание 8](Seminar_6/my_pacage_task8/__init__.py)
   - Создайте пакет с всеми модулями, которые вы создали за время занятия.
   - Добавьте в __init__ пакета имена модулей внутри дандер __all__.
   - В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

9. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_6)
   - В модуль с проверкой даты  добавьте возможность запуска в терминале с передачей даты на проверку.
   - Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
 каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь. .
   - Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

# СЕМИНАР 7 Файлы и файловая система
1. [Задание 1](Seminar_7/task_1.py)
    - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
    - ✔ Первое число int, второе - float разделены вертикальной чертой.
    - ✔ Минимальное число - -1000, максимальное - +1000.
    - ✔ Количество строк и имя файла передаются как аргументы функции. 


2. [Задание 2](Seminar_7/task_2.py) 
    - Напишите функцию, которая генерирует псевдоимена.
    - ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
    - ✔ Полученные имена сохраните в файл

3. [Задание 3](Seminar_7/task_3.py)
    - Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
    - ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
    - ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
    - ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
    - ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
    - ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

4. [Задание 4](Seminar_7/task_4.py)
    - Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
    - ✔ расширение
    - ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    - ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    - ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    - ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    - ✔ количество файлов, по умолчанию 42
    - ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


5. [Задание 5](Seminar_7/task_5.py)
   - Доработаем предыдущую задачу.
   - ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
   - ✔ Расширения и количество файлов функция принимает в качестве параметров.
   - ✔ Количество переданных расширений может быть любым.
   - ✔ Количество файлов для каждого расширения различно.
   - ✔ Внутри используйте вызов функции из прошлой задачи.


6. [Задание 6](Seminar_7/task_6.py)
   - Дорабатываем функции из предыдущих задач.
   - ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
   - ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
   - ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


7. [Задание 7](Seminar_7/task_7.py)
   - Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
   - ✔ Каждая группа включает файлы с несколькими расширениями.
   - ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
   - Прмечание: необходимо исправить ошибку - не найден путь


8. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_7)
   - Напишите функцию группового переименования файлов. Она должна:
   - ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
   - ✔ принимать параметр количество цифр в порядковом номере.
   - ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
   - ✔ принимать параметр расширение конечного файла.
   - ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
   - ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
   - **group_file.py** - модуль сортировки файлов по директориям
   - **group_rename.py** - модуль  группового переименования файлов по расширению
   - **main** - точка входа
   - все модули собраны в пакет
   - main - точка входа

# СЕМИНАР 8 Сериализация
1. [Задание 1](Seminar_8/File_manager/txt_to_json.py)
    - Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
    - Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
    - Имена пишите с большой буквы.
    - Каждую пару сохраняйте с новой строки.


2. [Задание 2](Seminar_8/File_manager/create_file_json.py) 
    - Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
    - После каждого ввода добавляйте новую информацию в JSON файл.
    - Пользователи группируются по уровню доступа.
    - Идентификатор пользователя выступает ключём для имени.
    - Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
    - При перезапуске функции уже записанные в файл данные должны сохраняться.


3. [Задание 3](Seminar_8/File_manager/json_to_csv.py)
    - Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

4. [Задание 4](Seminar_8/File_manager/csv_to_json.py)
    - Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
    - Дополните id до 10 цифр незначащими нулями.
    - В именах первую букву сделайте прописной.
    - Добавьте поле хеш на основе имени и идентификатора.
    - Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
    - Имя исходного и конечного файлов передавайте как аргументы функции.

5. Задание 5 - не выполняли на семинаре
   - Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.

6. Задание 6 -  не выполняли на семинаре
   - Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
   - Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
   - Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

7. Задание 7 -  не выполняли на семинаре
   - Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
   - Распечатайте его как pickle строку.


8. [ДОМАШНЯЯ РАБОТА](Seminar_8)
   - Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
   - ○ Для дочерних объектов указывайте родительскую директорию.
   - ○ Для каждого объекта укажите файл это или директория.
   - ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
   - Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

   - create_file_txt - создание файла с расширением txt с данными: рандомное слово: рандомное значение (Задание1 Семинар)
   - txt_to_json - создание из файла txt нового файла json Имена с большой буквы. Каждая пара - с новой строки. (Задание1 Семинар)
   - func - запись в json файл данных: имени, Id и уровня. Id - ключ для имени. Все идентификаторы уникальны независимо от уровня доступа. (Задание2 Семинар)
   - json_to_csv - перенос данных из json файла в файл csv (Задание3 Семинар)
   - csv_to_json - запись из csv файла в json файл, где каждая строка csv файла представлена как отдельный json словарь (Задание4 Семинар)
   - directory_reference - спрвавочник по содержимому директория: (наименование объекта, тип объекта в директории, размер объекта, родительский директорий объекта)
(ДОМАШНЕЕ ЗАДАНИЕ)
   - все модули добавлены в пакет File_manager
   - [main](Seminar_8/main.py) - точка входа

# СЕМИНАР 9 Декораторы
1. [Задание 1](Seminar_9/Task1.py)
    - Создайте функцию-замыкание, которая запрашивает два целых числа:
    - ○ от 1 до 100 для загадывания,
    - ○ от 1 до 10 для количества попыток
    - Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 


2. [Задание 2](Seminar_9/Task2.py) 
    - Дорабатываем задачу 1.
    - Превратите внешнюю функцию в декоратор.
    - Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
    - Если не входят, вызывать функцию со случайными числами  из диапазонов.

3. [Задание 3](Seminar_9/Task3.py)
    - Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
    - Каждый ключевой параметр сохраните как отдельный ключ json словаря.
    - Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
    - Имя файла должно совпадать с именем декорируемой функции.


4. [Задание 4](Seminar_9/Task4.py)
    - Создайте декоратор с параметром.
    - Параметр - целое число, количество запусков декорируемой функции.

5. [Задание 5](Seminar_9/Task5.py)
   - Объедините функции из прошлых задач.
   - Функцию угадайку задекорируйте:
   - ○ декораторами для сохранения параметров,
   - ○ декоратором контроля значений и
   - ○ декоратором для многократного запуска.
   - Выберите верный порядок декораторов.

6. Задание 6 - не выполняли
   - Доработайте прошлую задачу добавив декоратор wraps в  каждый из декораторов.

7. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_9/Task_9_7.py)
   - Напишите следующие функции:
   - ○ Нахождение корней квадратного уравнения
   - ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
   - ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
   - ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
   - Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

# СЕМИНАР 10 ООП Начало
1. [Задание 1](Seminar_10/Task1.py)
    - Создайте класс окружность.
    - Класс должен принимать радиус окружности при создании экземпляра.
    - У класса должно быть два метода, возвращающие длину окружности и её площадь.

2. [Задание 2](Seminar_10/Task2.py) 
    - Создайте класс прямоугольник.
    - Класс должен принимать длину и ширину при создании экземпляра.
    - У класса должно быть два метода, возвращающие периметр и площадь.
    - Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

3. [Задание 3](Seminar_10/Task3_Task4.py)
    - ННапишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
    - У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
    - Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

4. [Задание 4](Seminar_10/Task3_Task4.py)
    - Создайте класс Сотрудник.
    - Воспользуйтесь классом человека из прошлого задания.
    - У сотрудника должен быть:
    - ○ шестизначный идентификационный номер
    - ○ уровень доступа вычисляемый как остаток от деления  суммы цифр id на семь

5. [Задание 5](Seminar_10/Task5_Nask6.py)
   - Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
   - У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
   - Для каждого класса создайте метод, выводящий информацию специфичную для данного класса

6. [Задание 6](Seminar_10/Task5_Nask6.py)
   - Доработайте задачу 5.
   - Вынесите общие свойства и методы классов в класс Животное.
   - Остальные классы наследуйте от него.
   - Убедитесь, что в созданные ранее классы внесены правки.


7. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_10)
   - Доработаем задачи 5-6. Создайте класс-фабрику.
   - ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
   - ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
   - Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов экземпляра.


# СЕМИНАР 11 ООП. Особенности Python
1. [Задание 1](Seminar_11/Task_1.py)
    - Создайте класс Моя Строка, 
    - где: будут доступны все возможности str
    - дополнительно хранятся имя автора строки и время создания (time.time)

2. [Задание 2](Seminar_11/Task2.py)   [Задание 2](Seminar_11/Task2.py) 
    - Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    - При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списковархивов
    - list-архивы также являются свойствами экземпляра

3. Задание 3
    - Добавьте к задачам 1 и 2 строки документации для классов.

4. [Задание 4](Seminar_11/Task4.py)
    - Доработаем класс Архив из задачи 2.
    - Добавьте методы представления экземпляра для программиста и для пользователя.

5. [Задание 5](Seminar_11/Task5.py)
   - Дорабатываем класс прямоугольник из прошлого семинара.
   - Добавьте возможность сложения и вычитания.
   - При этом должен создаваться новый экземпляр прямоугольника.
   - Складываем и вычитаем периметры, а не длинну и ширину.
   - При вычитании не допускайте отрицательных значений.


6. [Задание 6](Seminar_11/Task6.py)
   - Доработайте прошлую задачу.
   - Добавьте сравнение прямоугольников по площади
   - Должны работать все шесть операций сравнения


7. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_11/main.py)
   - Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
   - Создайте класс Матрица. Добавьте методы для:
   - ○ вывода на печать,
   - ○ сравнения,
   - ○ сложения,
   - ○ *умножения матриц


# СЕМИНАР 12 ООП. ООП. Финал
1. [Задание 1](Seminar_12/Task_1.py)
    - Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
    - Экземпляр должен запоминать последние k значений.
    - Параметр k передаётся при создании экземпляра.
    - Добавьте метод для просмотра ранее вызываемых значений и их факториалов.


2. [Задание 2](Seminar_12/Task2.py)   [Задание 2](Seminar_11/Task2.py) 
    - Доработаем задачу 1.
    - Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл

3. [Задание 3](Seminar_12/Task3.py)
    - Создайте класс-генератор.
    - Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
    - Если переданы два параметра, считаем step=1.
    - Если передан один параметр, также считаем start=1.

4. [Задание 4](Seminar_12/Task4.py)
    - Доработайте класс прямоугольник из прошлых семинаров.
    - Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений
(отрицательных).
    - Используйте декораторы свойств.


5. [Задание 5](Seminar_12/Task4.py)
   - Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.


6. [Задание 6](Seminar_12/Task6.py)
   - Изменяем класс прямоугольника.
   - Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.



7. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_12/Student_performance.py)
   - Создайте класс студента.
   - ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
   - ○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
   - ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
   - ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых. 

# СЕМИНАР 13 Исключения
1. [Задание 1](Seminar_13/Task1.py)
    - Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
вещественное число.
    - Обрабатывайте не числовые данные как исключения.


2. [Задание 2](Seminar_13/Task2.py)   [Задание 2](Seminar_11/Task2.py) 
    - Создайте функцию аналог get для словаря.
    - Помимо самого словаря функция принимает ключ и значение по умолчанию.
    - При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
    - Реализуйте работу через обработку исключений.


3. [Задание 3](Seminar_13/Task3.py)
    - Создайте класс с базовым исключением и дочерние классыисключения:
    - ○ ошибка уровня,
    - ○ ошибка доступа

4. [Задание 4](Seminar_13/Task4.py)
    - Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
    - Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
    - Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.



5. [Задание 5](Seminar_13/Task5.py)
   - Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
   - загрузка данных (функция из задания 4)
   - вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из множества пользователей.
   - добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня
доступа.


6. [Задание 6](Seminar_13/Task5.py)
   - Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
   - Передавайте необходимые данные из основного кода проекта.



7. [ДОМАШНЯЯ РАБОТА](Homework/Seminar_13)
   - Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
   - Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами
отрицательной длины.
   - В качестве примеров взяты три задачи:
   1. Rectangle.py - расчет площади, периметра прямоугольника, селадывание и вычитание двух прямоугольников.
      - Exceptions: ValueError - формат ввода , при возникновении ошибки, по умолчанию стороны всех прямоуголников = 1
      - class ValError - валидность значений сторон прямоугольника на отрицательные значения
   2. Bank.py - банкомат по выдачи и зачислению cash с учетом комиссии на снятие денег и начисленнию процентов
      - Exceptions: ValueError - формат ввода, class ValueBankError - валидность значений cash
   3. Matrix - сравнение, умножение, сложение двух матриц
      - Exceptions: ValFormatError - валидность формата матриц при различных операциях

