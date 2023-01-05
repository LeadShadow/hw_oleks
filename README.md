# hw_oleks

1. [Заняття №1 Вступ в Пайтон](#module01)



## Заняття №1. Вступ в Пайтон <a name="module01"></a>
Коли ми говоримо про програмування, перше, що спадає на думку - це набір інструкцій у файлі - вихідний код.

    print("Hello World!")
Вище приведений приклад виведення в консоль повідомлення **'Hello World!'**

Але символи, слова та фрази, які становлять програму, насправді незрозумілі для машини. Є крок, який виконується після 
написання програми, який конвертує вихідний код у файлі на набір інструкцій, зрозумілих комп'ютеру. Цим займається 
спеціальна програма: **компілятор** чи **інтерпретатор**.

### Python є високорівневою мовою програмування загального призначення, стандартна бібліотека якої включає великий набір корисних функцій.

#### На сьогоднішній день Python використовують у таких сферах:

* **Web-розробка**
* **Data Science**
* **Data Mining (отримання даних)**
* **Machine Learning (машинне навчання)**
* **Deep Learning (глибинне навчання)**

### Змінні

**Змінна** - це ім'я (псевдонім) для певної області пам'яті комп'ютера. Передбачається, що в цій пам'яті лежить корисна для розробника інформація, до якої необхідно звертатися неодноразово. Python, як і будь-яка інша мова програмування, працює з даними в пам'яті, до яких звертаються за допомогою імен (змінних).

**Змінна** — це комірка пам'яті, яка має ім'я і в якій можуть зберігатися дані.

    age = 20
    user1_age = 30
    user2_age = 30
    ADULT_THR = 18
    
    _do_not_use_this = 0

**Щодо іменування змінних у Python є три суворі правила:**

* Ім'я змінної в Python може складатися тільки з цифр, літер та знаків підкреслення _;
* Ім'я змінної не може починатися з цифри, а може зі знака нижнього підкреслення;
* Використання зарезервованих слів як ім'я змінної призведе до помилки.

**Список зарезервованих слів:**

    False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

### Оператори та операнди
Операнди та оператори – це частини виразу. Оператори - визначають дію, операнди - те, з чим ця дія буде зроблена. У виразі 2 + 3 числа 3 і 2 будуть операндами, а знак + - оператором.

**Для Python визначено такі арифметичні оператори:**
* \+ \- * / // % **
* \+ : додавання 3 + 3 == 6
* \- : віднімання 5 - 3 == 2
* \* : множення 6 * 3 == 18
* \/ : ділення з остачею 15 / 2 == 7.5
* // : ділення без остачі 15 / 2 == 7
* % : остача від ділення
* \** : піднесення до степені 2 ** 3 == 8

**У пайтоні два знаки == це дорівнює!! Один знак = це присвоїти**

**Порядок виконання операцій такий самий як в математиці**

    x = 8**3 + 4*(2 + 2)
Спочатку 8**3, далі додавання 2+2, далі множення на 4 і додавання кінцеве

### Коментарі
Навіть ви у своєму коді за місяць мало що згадаєте. Тому дуже важливим інструментом розробника є коментарі. Також коментарі використовуються в тих випадках, коли виконувати частину програми не потрібно, але видаляти цю частину поки що зарано.

Коментарі в Python позначаються символом #, що після цього символу і до початку нового рядка інтерпретатор просто проігнорує.

    user_age = 7
    user_age = 18
    user_status = "adult"   # 'adult' for users older 18 and 'child' for younger

### Типи даних
Змінні можуть бути різного типу (зберігати інформацію у різних форматах):

* None — пустое значение и "никакой" тип данных.
* Числа (Numeric Type)
* Boolean — булев (логический) тип. Является подтипом целых чисел.
* Строки (Text Sequence Type)
### Тип None
У Python для позначення порожнього значення використовується None

    a = None

None використовується тоді, коли треба явно повернути якесь значення або створити його 
(зарезервувати ім'я для чогось), але по суті і сенсу ніякої корисної 
інформації поки що зберегти в цьому значенні не можна, навіть якого роду ця інформація 
(рядок чи число, або щось інше) поки що неясно. У разі застосовують None.

### Рядки
    hello_string = "Hello"
    world_string = 'World!'
Рядкові змінні - це впорядковані набори символів, що незмінюються. "Упорядковані" означає, що можна звертатися до символів рядків за індексом, копіювати їх, порівнювати, шукати. "Незмінні" означає, що одного разу створивши рядок, не можна змінити його вміст, можна тільки створити новий.

Для того, щоб Python зрозумів, що ви хочете створити рядкову змінну, необхідно укласти символи рядка в лапки. Для цього підійдуть як одинарні лапки”, так і подвійні”.

Наприклад, створимо змінну s, в якій зберігається рядок "Hello, World!":

    s = "Hello, World!"

### Операції над рядками
    s1 = "Hello,"
    s2 = "World!"
    joined_string = s1 + s2
Основною операцією, що реалізована для рядків, є об'єднання 
рядків (конкатенація). Конкатенація рядків реалізована з 
використанням оператора додавання +. Якщо "скласти" два або 
більше рядків, то в результаті отримаємо об'єднаний рядок. 
У прикладі вище joined_string дорівнюватиме "Hello, World!".

Для зручності вивода текста в Python використовуються спеціальну конструкцію f-рядки.

    name = "Oleg"
    hello_string = f"Hello, {name}!"
**f-рядок** — це такий шаблон, який дозволяє зручно генерувати рядок, підставляючи результат виконання виразів у потрібне місце в шаблоні.

Синтаксично f-рядок відрізняється від звичайного тим, що на початку рядка стоїть символ f. Інтерпретатор зрозуміє, що якщо
в такому рядку він зустріне символи фігурних дужок {}, то всередині них міститься вираз, який треба виконати і підставити результат у рядок.

У прикладі  **hello_string** дорівнюватиме **"Hello, Oleg!"**.
