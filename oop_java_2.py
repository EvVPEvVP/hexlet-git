// 1. Класс Оружие
class Weapon {
    String name;
    int damage;
    int durability; // Прочность (0-100)

    // Вывод информации об оружии
    void printInfo() {
        System.out.println("Оружие: " + name + " (Урон: " + damage + ", Прочность: " + durability + "%)");
    }

    // Использование оружия (снижает прочность)
    void use() {
        if (durability > 0) {
            durability = durability - 10;
            System.out.println(">> " + name + " немного затупился. Текущая прочность: " + durability);
        } else {
            System.out.println(">> " + name + " сломан и не может быть использован!");
            damage = 1; // Если сломано, урон становится минимальным
        }
    }
}

// 2. Класс Монстр
class Monster {
    String species;
    int hp;
    int damage;
    boolean isAlive;

    void roar() {
        if (isAlive) {
            System.out.println(species + " рычит: RRRRRRRR!");
        } else {
            System.out.println(species + " молчит, потому что мертв.");
        }
    }

    // Монстр получает урон
    // Метод меняет поле hp
    void takeDamage(int incomingDamage) {
        if (!isAlive) return; // Мертвые не получают урон

        hp = hp - incomingDamage;
        System.out.println(species + " получает " + incomingDamage + " урона. Осталось HP: " + hp);

        if (hp <= 0) {
            isAlive = false;
            System.out.println(">> " + species + " погиб");
        }
    }

    // Атака на героя
    void attackHero(Hero target) {
        if (isAlive) {
            System.out.println(species + " атакует героя " + target.nickname + "!");
            target.receiveDamage(this.damage);
        }
    }
}

// 3. Класс Герой
class Hero {
    String nickname;
    int hp;
    Weapon currentWeapon;

    // Смена оружия
    void equipWeapon(Weapon newWeapon) {
        currentWeapon = newWeapon;
        System.out.println(nickname + " взял в руки " + newWeapon.name);
    }

    // Герой атакует монстра
    void attack(Monster enemy) {
        System.out.println(nickname + " размахивает " + currentWeapon.name + " и бьет " + enemy.species);
        
        enemy.takeDamage(currentWeapon.damage);
        
        // Портится оружие
        currentWeapon.use();
    }

    // Герой получает урон
    void receiveDamage(int dmg) {
        hp = hp - dmg;
        System.out.println(nickname + " ранен! Потеряно " + dmg + " HP. Осталось: " + hp);
    }
    
    // Лечение
    void drinkPotion() {
        hp = hp + 50;
        System.out.println(nickname + " выпил зелье. Здоровье восстановлено до " + hp);
    }
}

public class GameScenario {
    public static void main(String[] args) {
        // 1. Подготовка данных
        Weapon sword = new Weapon();
        sword.name = "Excalibur";
        sword.damage = 60;
        sword.durability = 100;

        Hero hero = new Hero();
        hero.nickname = "Geralt";
        hero.hp = 200;
        // Сразу даем оружие
        hero.equipWeapon(sword);

        Monster monster = new Monster();
        monster.species = "Griffin";
        monster.hp = 100;
        monster.damage = 30;
        monster.isAlive = true;

        System.out.println("--- БОЙ НАЧИНАЕТСЯ ---");
        
        // 2. Логика боя
        monster.roar(); // Монстр пугает
        
        // Раунд 1: Герой бьет монстра
        hero.attack(monster); 
        // Внутри метода attack() сработает takeDamage() у монстра и use() у меча

        System.out.println("--- ОТВЕТНЫЙ УДАР ---");
        
        // Раунд 2: Монстр бьет героя
        if (monster.isAlive) {
            monster.attackHero(hero);
        }
        
        System.out.println("--- ФИНАЛ ---");
        
        // Раунд 3: Герой добивает
        hero.attack(monster);

        // Герой лечится после боя
        hero.drinkPotion();
        
        // Проверяем состояние меча
        sword.printInfo();
    }
}