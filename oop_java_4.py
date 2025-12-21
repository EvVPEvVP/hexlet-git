//  ИЕРАРХИЯ 1: ОРУЖИЕ 
class Weapon {
    String name;
    int damage;

    public Weapon(String name, int damage) {
        this.name = name;
        this.damage = damage;
    }
}

class Sword extends Weapon {
    public Sword() { super("Меч", 15); }
}

class Bow extends Weapon {
    public Bow() { super("Лук", 10); }
}

//  ИЕРАРХИЯ 2: СУЩЕСТВА 
class Creature {
    String name;

    public Creature(String name) {
        this.name = name;
    }

    // Задание 4.2: Метод для переопределения
    public void foo() {
        System.out.println("Я просто Существо");
    }
}

class Monster extends Creature {
    public Monster(String name) { super(name); }

    // Задание 4.2: Реализация для Монстра
    @Override
    public void foo() {
        System.out.println("Класс MONSTER (" + name + ")");
    }
}

class Hero extends Creature {
    // Задание 4.1: КОМПОЗИЦИЯ (Герой СОДЕРЖИТ Оружие)
    Weapon currentWeapon; 

    public Hero(String name, Weapon startWeapon) {
        super(name);
        this.currentWeapon = startWeapon;
    }

    // Метод для смены оружия
    public void setWeapon(Weapon newWeapon) {
        this.currentWeapon = newWeapon;
        System.out.println(name + " взял " + newWeapon.name);
    }

    // Задание 4.2: Реализация для Героя
    @Override
    public void foo() {
        System.out.println("Я Класс HERO (" + name + ")");
    }

    // Задание 4.3: Обычная атака
    public void attack() {
        System.out.println(name + " бьет используя " + currentWeapon.name + " (Урон " + currentWeapon.damage + ")");
    }

    // Задание 4.3: Ad hoc полиморфизм
    public void attack(boolean isCritical) {
        int dmg = currentWeapon.damage;
        if (isCritical) dmg = dmg * 2;
        System.out.println(name + " наносит критический урон: " + dmg);
    }
}

//  ЗАПУСК 
public class Main {
    public static void main(String[] args) {
        
        // === 4.1. КОМПОЗИЦИЯ ===
        System.out.println(" 4.1 Композиция ");
        Sword sword = new Sword();
        Bow bow = new Bow();
        
        Hero hero = new Hero("Геральт", sword); // Дали меч
        hero.attack(); 
        
        hero.setWeapon(bow); // Подменили на лук
        hero.attack();


        // === 4.3. AD HOC ПОЛИМОРФИЗМ ===
        System.out.println(" 4.3 Ad hoc (Перегрузка) ");
        hero.attack();       // Вызов метода без параметров
        hero.attack(true);   // Вызов метода с параметром boolean


        // === 4.2. МАССИВ И ПОЛИМОРФИЗМ ===
        System.out.println(" 4.2 Массив и Полиморфизм ");
        Creature[] army = new Creature[500];

        // Заполняем случайно (Math.random() встроен в язык)
        for (int i = 0; i < 500; i++) {
            if (Math.random() > 0.5) {
                army[i] = new Hero("H" + i, sword);
            } else {
                army[i] = new Monster("M" + i);
            }
        }

        // Вызываем foo(). Для примера выведем только первые 5, чтобы не засорять консоль
        for (int i = 0; i < 5; i++) {
            army[i].foo(); 
        }
    }
}


4.2. 
Был создан массив общего типа Creature[], но положили туда разных наследников (Hero и Monster).
Сработало позднее связывание. Программа во время выполнения проверяет, какой именно класс лежит в ячейке памяти. Если там создан new Monster(), вызывается метод foo() из класса Monster, даже если переменная в цикле имеет тип Creature.