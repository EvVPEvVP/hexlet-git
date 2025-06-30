1.

SELECT
    squad_id,
    name
FROM
    Squads
WHERE
    leader_id IS NULL;
	
2.

SELECT
    dwarf_id,
    name,
    age,
    profession
FROM
    Dwarves
WHERE
    age > 150 AND profession = 'Warrior';
	
3.

SELECT
    D.dwarf_id,
    D.name,
    D.profession
FROM
    Dwarves D
WHERE EXISTS (
    SELECT 1
    FROM Items I
    WHERE
        I.owner_id = D.dwarf_id
        AND I.type = 'weapon'
);

4.

SELECT
    D.dwarf_id,
    D.name,
    T.status,
    COUNT(T.task_id) AS TaskCount
FROM
    Dwarves D
JOIN
    Tasks T ON D.dwarf_id = T.assigned_to
GROUP BY
    D.dwarf_id, D.name, T.status
ORDER BY
    D.name, T.status;
	
5.

SELECT
    T.task_id,
    T.description,
    T.status,
    D.name
FROM
    Tasks T
JOIN
    Dwarves D ON T.assigned_to = D.dwarf_id
JOIN
    Squads S ON D.squad_id = S.squad_id
WHERE
    S.name = 'Guardians';
	
6.

SELECT
    D1.name AS Dwarf,
    R.relationship AS Relationship,
    D2.name AS RelatedTo
FROM
    Relationships R
JOIN
    Dwarves D1 ON R.dwarf_id = D1.dwarf_id
JOIN
    Dwarves D2 ON R.related_to = D2.dwarf_id;