WITH SquadBattleStats AS (
    SELECT
        squad_id,
        COUNT(report_id) AS total_battles,
        COUNT(report_id) FILTER (WHERE outcome = 'Victory') AS victories,
        SUM(casualties) AS total_casualties,
        SUM(enemy_casualties) AS total_enemy_casualties
    FROM
        SQUAD_BATTLES
    GROUP BY
        squad_id
),
SquadMembershipStats AS (
    SELECT
        squad_id,
        COUNT(DISTINCT dwarf_id) AS total_members_ever,
        COUNT(DISTINCT dwarf_id) FILTER (WHERE exit_date IS NULL) AS current_members
    FROM
        SQUAD_MEMBERS
    GROUP BY
        squad_id
),
SquadTrainingStats AS (
    SELECT
        squad_id,
        COUNT(schedule_id) AS total_training_sessions,
        AVG(effectiveness) AS avg_training_effectiveness
    FROM
        SQUAD_TRAINING
    GROUP BY
        squad_id
),
SquadEquipmentQuality AS (
    SELECT
        sq.squad_id,
        AVG(CAST(e.quality AS INTEGER)) AS avg_equipment_quality
    FROM
        SQUAD_EQUIPMENT sq
    JOIN
        EQUIPMENT e ON sq.equipment_id = e.equipment_id
    GROUP BY
        sq.squad_id
),
MemberSkillProgression AS (
    SELECT
        sm.squad_id,
        AVG(
            (SELECT MAX(ds.level) FROM DWARF_SKILLS ds JOIN SKILLS s ON ds.skill_id = s.skill_id WHERE ds.dwarf_id = sm.dwarf_id AND s.skill_type = 'Combat') -
            (SELECT MIN(ds.level) FROM DWARF_SKILLS ds JOIN SKILLS s ON ds.skill_id = s.skill_id WHERE ds.dwarf_id = sm.dwarf_id AND s.skill_type = 'Combat')
        ) AS avg_combat_skill_improvement
    FROM
        SQUAD_MEMBERS sm
    GROUP BY
        sm.squad_id
),
TrainingBattleCorrelationData AS (
    SELECT
        b.squad_id,
        EXTRACT(YEAR FROM b.date) AS battle_year,
        EXTRACT(QUARTER FROM b.date) AS battle_quarter,
        AVG(CASE WHEN b.outcome = 'Victory' THEN 1.0 ELSE 0.0 END) AS quarterly_victory_rate,
        (
            SELECT AVG(t.effectiveness)
            FROM SQUAD_TRAINING t
            WHERE t.squad_id = b.squad_id
              AND EXTRACT(YEAR FROM t.date) = EXTRACT(YEAR FROM b.date)
              AND EXTRACT(QUARTER FROM t.date) = EXTRACT(QUARTER FROM b.date)
        ) AS quarterly_avg_training
    FROM
        SQUAD_BATTLES b
    GROUP BY
        b.squad_id, battle_year, battle_quarter
)

-- Финальный запрос
SELECT
    ms.squad_id,
    ms.name AS squad_name,
    ms.formation_type,
    d.name AS leader_name,
    COALESCE(bs.total_battles, 0) AS total_battles,
    COALESCE(bs.victories, 0) AS victories,
    ROUND(COALESCE(bs.victories::NUMERIC * 100 / NULLIF(bs.total_battles, 0), 0), 2) AS victory_percentage,
    ROUND(COALESCE(bs.total_casualties::NUMERIC * 100 / NULLIF(bs.total_battles * mem.current_members, 0), 0), 2) AS casualty_rate,
    ROUND(COALESCE(bs.total_enemy_casualties::NUMERIC / NULLIF(bs.total_casualties, 0), 0), 2) AS casualty_exchange_ratio,
    COALESCE(mem.current_members, 0) AS current_members,
    COALESCE(mem.total_members_ever, 0) AS total_members_ever,
    ROUND(COALESCE(mem.current_members::NUMERIC * 100 / NULLIF(mem.total_members_ever, 0), 0), 2) AS retention_rate,
    ROUND(COALESCE(eq.avg_equipment_quality, 0), 2) AS avg_equipment_quality,
    COALESCE(ts.total_training_sessions, 0) AS total_training_sessions,
    ROUND(COALESCE(ts.avg_training_effectiveness, 0), 2) AS avg_training_effectiveness,
    (SELECT CORR(tbc.quarterly_victory_rate, tbc.quarterly_avg_training) FROM TrainingBattleCorrelationData tbc WHERE tbc.squad_id = ms.squad_id) AS training_battle_correlation,
    ROUND(COALESCE(msp.avg_combat_skill_improvement, 0), 2) AS avg_combat_skill_improvement,
    ROUND(
        (COALESCE(bs.victories::NUMERIC / NULLIF(bs.total_battles, 0), 0) * 0.30) +
        (COALESCE(bs.total_enemy_casualties::NUMERIC / NULLIF(bs.total_casualties, 1), 0) / 10 * 0.25)
        (COALESCE(mem.current_members::NUMERIC / NULLIF(mem.total_members_ever, 0), 0) * 0.15) +
        (COALESCE(eq.avg_equipment_quality, 0) / 5 * 0.15) +
        (COALESCE((SELECT CORR(tbc.quarterly_victory_rate, tbc.quarterly_avg_training) FROM TrainingBattleCorrelationData tbc WHERE tbc.squad_id = ms.squad_id), 0) * 0.15)
    , 3) AS overall_effectiveness_score,    
    JSON_OBJECT(
        'member_ids', (SELECT JSON_ARRAYAGG(dwarf_id) FROM SQUAD_MEMBERS sm WHERE sm.squad_id = ms.squad_id AND sm.exit_date IS NULL),
        'equipment_ids', (SELECT JSON_ARRAYAGG(equipment_id) FROM SQUAD_EQUIPMENT se WHERE se.squad_id = ms.squad_id),
        'battle_report_ids', (SELECT JSON_ARRAYAGG(report_id) FROM SQUAD_BATTLES sb WHERE sb.squad_id = ms.squad_id),
        'training_ids', (SELECT JSON_ARRAYAGG(schedule_id) FROM SQUAD_TRAINING st WHERE st.squad_id = ms.squad_id)
    ) AS related_entities
FROM
    MILITARY_SQUADS ms
LEFT JOIN DWARVES d ON ms.leader_id = d.dwarf_id
LEFT JOIN SquadBattleStats bs ON ms.squad_id = bs.squad_id
LEFT JOIN SquadMembershipStats mem ON ms.squad_id = mem.squad_id
LEFT JOIN SquadTrainingStats ts ON ms.squad_id = ts.squad_id
LEFT JOIN SquadEquipmentQuality eq ON ms.squad_id = eq.squad_id
LEFT JOIN MemberSkillProgression msp ON ms.squad_id = msp.squad_id
ORDER BY
    overall_effectiveness_score DESC;
