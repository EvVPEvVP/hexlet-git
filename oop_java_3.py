// 1. Вспомогательный класс: ОРУЖИЕ
class Weapon {
    // Инкапсуляция private
    private String name;
    private int damage;
    private int durability;

    // Конструктор
    public Weapon(String name, int damage, int durability) {
        this.name = name;
        this.damage = damage;
        this.durability = durability;
    }

    // Геттеры
    public String getName() {
        return name;
    }

    public int getDamage() {
        if (durability <= 0) return 1;
        return damage;
    }

    // Логика использования
    public void use() {
        if (durability > 0) {
            durability -= 10;
        } 
    }
    
    public void printInfo() {
        System.out.println("Weapon: " + name + " | Durability: " + durability + "%");
    }
}

// 2. Родительский класс: СУЩЕСТВО (Базовый класс для Героя и Монстра)
class Creature {
    private String name;
    private int hp;
    private boolean isAlive;

    public Creature(String name, int hp) {
        this.name = name;
        this.hp = hp;
        this.isAlive = true;
    }

    // Геттеры
    public String getName() { return name; }
    public boolean isAlive() { return isAlive; }
    public int getHp() { return hp; }

    // Общий метод для всех существ: Получение урона
    public void takeDamage(int dmg) {
        if (!isAlive) return;

        this.hp -= dmg;
        System.out.println(this.name + " получает " + dmg + " урона. (HP: " + this.hp + ")");

        if (this.hp <= 0) {
            this.hp = 0;
            this.isAlive = false;
            System.out.println(">> " + this.name + " погиб.");
        }
    }
    
    // Метод для лечения
    protected void heal(int amount) {
        if (isAlive) {
            this.hp += amount;
            System.out.println(this.name + " исцелился на " + amount + ". (HP: " + this.hp + ")");
        }
    }
}

// 3. Класс МОНСТР (Наследник)
class Monster extends Creature {
    private int baseDamage; // У монстра нет оружия

    public Monster(String species, int hp, int baseDamage) {
        super(species, hp); // Вызов конструктора Creature
        this.baseDamage = baseDamage;
    }

    public void roar() {
        if (isAlive()) {
            System.out.println(getName() + " рычит: RRRRRRR!");
        }
    }

    public void attack(Creature target) {
        if (isAlive()) {
            System.out.println(getName() + " кусает " + target.getName() + "!");
            target.takeDamage(this.baseDamage);
        }
    }
}

// 4. Класс ГЕРОЙ (Наследник)
class Hero extends Creature {
    private Weapon currentWeapon;

    public Hero(String nickname, int hp, Weapon startingWeapon) {
        super(nickname, hp); // Инициализируем имя и здоровье через родителя
        this.currentWeapon = startingWeapon;
    }

    public void attack(Creature target) {
        if (!isAlive()) return;

        System.out.println(getName() + " атакует с помощью " + currentWeapon.getName());
        
        // Берем урон из оружия
        int dmg = currentWeapon.getDamage();
        target.takeDamage(dmg);
        
        // Портим оружие
        currentWeapon.use();
    }
    
    public void drinkPotion() {
        System.out.println(getName() + " пьет зелье.");
        heal(50);
    }
}

public class GameScenario {
    public static void main(String[] args) {
        // 1. Создаем оружие через конструктор
        Weapon sword = new Weapon("Excalibur", 40, 100);

        // 2. Создаем героя (сразу с именем, здоровьем и мечом)
        Hero hero = new Hero("Geralt", 200, sword);

        // 3. Создаем монстра (имя, здоровье, базовый урон)
        Monster monster = new Monster("Griffin", 120, 25);

        System.out.println("<Битва началась");
        
        // Герой бьет монстра
        hero.attack(monster); // Griffin hp: 120 -> 80
        
        // Монстр дает сдачи
        monster.roar();
        monster.attack(hero); // Geralt hp: 200 -> 175
        
        System.out.println("Второй раунд");
        
        hero.attack(monster); // Griffin hp: 80 -> 40
        hero.attack(monster); // Griffin hp: 40 -> 0 -> die
        
        System.out.println("После боя");
        
        // Попытка ударить мертвого
        hero.attack(monster); 
        
        // Лечение
        hero.drinkPotion();
        
        // Состояние оружия
        sword.printInfo();
    }
}