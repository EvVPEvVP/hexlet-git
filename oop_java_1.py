1.1
    1. Яндекс Музыка (Музыкальный плеер)
    Класс Track (Трек): Базовая единица. Поля: название, длительность в секундах, ссылка на файл, жанр, признак "Explicit" (цензура).
    Класс Artist (Исполнитель): Человек или группа. Поля: имя/название, биография, количество ежемесячных слушателей, список альбомов, фото.
    Класс Playlist (Плейлист): Список треков. Поля: название плейлиста, автор (кто составил), дата обновления, картинка обложки, список добавленных треков.

    2. Приложение Интернет-магазина (например, Wildberries)
    Класс Product (Товар): Конкретная вещь на полке. Поля: артикул, название, текущая цена, вес в граммах, габариты упаковки, остаток на складе.
    Класс Order (Заказ): Коробка для отправки. Поля: номер заказа, дата оформления, итоговая сумма, адрес доставки, статус (в сборке/в пути/доставлен).
    Класс Customer (Покупатель): Реальный человек. Поля: номер телефона, привязанная карта (маска карты), список избранного, сумма выкупа (для скидки).

1.2

// РПГ игра

class Weapon {
    String name;            // Название
    String type;            // Тип (Меч, Топор, Лук)
    int damage;             // Урон
    double weight;          // Вес
    int durability;         // Прочность (0-100)
    int requiredLevel;      // Требуемый уровень героя
    boolean isMagical;      // Магическое ли оружие
}

class Hero {
    String nickname;        // Имя персонажа
    String characterClass;  // Класс (Воин, Маг)
    int level;              // Уровень
    int hp;                 // Здоровье
    int maxHp;              // Максимальное здоровье
    double gold;            // Золото в кармане
    boolean isAlive;        // Жив ли герой
    Weapon currentWeapon;   // Ссылка на объект Оружия
}

class Monster {
    String species;         // Вид (Гоблин, Дракон)
    int dangerLevel;        // Уровень опасности
    int hp;                 // Здоровье
    int damage;             // Урон монстра
    String location;        // Где обитает (Пещера, Лес)
    boolean isAggressive;   // Агрессивный или нет
    String lootDrop;        // Что выпадает при смерти
}

public class RpgGame {
    public static void main(String[] args) {
        
        // 1. Создаем оружие
        Weapon sword = new Weapon();
        sword.name = "Excalibur";
        sword.type = "Sword";
        sword.damage = 50;
        sword.weight = 3.5;
        sword.durability = 100;
        sword.requiredLevel = 5;
        sword.isMagical = true;

        // 2. Создаем героя
        Hero hero = new Hero();
        hero.nickname = "Geralt";
        hero.characterClass = "Witcher";
        hero.level = 10;
        hero.hp = 500;
        hero.maxHp = 500;
        hero.gold = 150.0;
        hero.isAlive = true;
        hero.currentWeapon = sword;

        // 3. Создаем монстра
        Monster enemy = new Monster();
        enemy.species = "Griffin";
        enemy.dangerLevel = 8;
        enemy.hp = 800;
        enemy.damage = 40;
        enemy.location = "White Orchard";
        enemy.isAggressive = true;
        enemy.lootDrop = "Griffin Trophy";

        System.out.println("--- STATUS REPORT ---");
        System.out.println("Hero: " + hero.nickname + " (" + hero.characterClass + ")");
        System.out.println("HP: " + hero.hp + "/" + hero.maxHp);
        System.out.println("Weapon: " + hero.currentWeapon.name + " (Damage: " + hero.currentWeapon.damage + ")");
    }
}

1.3

public class Reference {
    public static void main(String[] args) {
        // Создаем первого героя
        Hero hero1 = new Hero();
        hero1.nickname = "Arthur";
        hero1.hp = 100;

        // Создаем ссылку hero2
        Hero hero2 = hero1;

        System.out.println("До изменений");
        System.out.println("Hero 1 HP: " + hero1.hp);
        System.out.println("Hero 2 HP: " + hero2.hp);

        // Работаем с переменной hero2 (он попал в ловушку)
        System.out.println("\n>> Hero 2 наступил в капкан и потерял 50 HP!");
        hero2.hp = 50; 

        // Проверка
        System.out.println("После изменений");
        System.out.println("Hero 2 HP: " + hero2.hp); // 50 (Ожидаемо)
        System.out.println("Hero 1 HP: " + hero1.hp); // 50 (Побочный эффект)
        
    }
}
