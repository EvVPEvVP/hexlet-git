1.

SELECT
    d.name AS dwarf_name,
    d.age,
    d.profession,
    s.name AS squad_name,
    s.mission
FROM
    Dwarves d
JOIN
    Squads s ON d.squad_id = s.squad_id;

2.

SELECT
    *
FROM
    Dwarves
WHERE
    profession = 'miner' AND squad_id IS NULL;

3.

WITH table1 AS (
    SELECT
        *,
        row_number() OVER (ORDER BY priority DESC) as priority_rank
    FROM
        Tasks
    WHERE
        status = 'pending'
)
SELECT
    task_id,
    description,
    priority,
    assigned_to,
    status
FROM
    table1
WHERE
    priority_rank = 1;


4.

SELECT
    d.name,
    COUNT(i.item_id) AS item_count
FROM
    Dwarves d
JOIN
    Items i ON d.dwarf_id = i.owner_id
GROUP BY
    d.dwarf_id, d.name
ORDER BY
    item_count DESC;
	
5.

WITH DwarfPerSquad AS (
    SELECT
        squad_id,
        COUNT(dwarf_id) AS dwarf_count
    FROM
        Dwarves
    GROUP BY
        squad_id
)
SELECT
    s.name AS squad_name,
    s.mission,
    COALESCE(dc.dwarf_count, 0) AS dwarf_count
FROM
    Squads s
LEFT JOIN
    DwarfPerSquad dc ON s.squad_id = dc.squad_id;
	
6.

WITH Professions AS (
    SELECT
        d.profession,
        COUNT(t.task_id) AS unfinished_task_count,
        RANK() OVER (ORDER BY COUNT(t.task_id) DESC) as rn
    FROM
        Dwarves d
    JOIN
        Tasks t ON d.dwarf_id = t.assigned_to
    WHERE
        t.status IN ('pending', 'in_progress')
    GROUP BY
        d.profession
)
SELECT
    profession,
    unfinished_task_count
FROM
    Professions
WHERE
    rn = 1;

7.

SELECT
    i.type AS item_type,
    ROUND(AVG(d.age)) AS average_owner_age
FROM
    Items i
JOIN
    Dwarves d ON i.owner_id = d.dwarf_id
GROUP BY
    i.type;
	
8.

WITH DwarvesWithoutItems AS (
    SELECT
        d.dwarf_id,
        d.name,
        d.age,
        d.profession,
        d.squad_id
    FROM
        Dwarves d
    LEFT JOIN
        Items i ON d.dwarf_id = i.owner_id
    WHERE
        i.item_id IS NULL
)
SELECT
    *
FROM
    DwarvesWithoutItems
WHERE
    age > (SELECT AVG(age) FROM Dwarves);















