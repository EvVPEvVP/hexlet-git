WITH AttackHistory AS (
    SELECT
        EXTRACT(YEAR FROM date) AS attack_year,
        location_id,
        creature_id,
        outcome,
        casualties,
        enemy_casualties,
        defense_structures_used,
        military_response_time_minutes
    FROM
        CREATURE_ATTACKS
),

ThreatAssessment AS (
    SELECT
        c.type AS creature_type,
        c.threat_level,
        MAX(cs.date) AS last_sighting_date,
        MIN(ct.distance_to_fortress) AS territory_proximity,
        SUM(c.estimated_population) AS estimated_numbers,
        JSON_ARRAYAGG(c.creature_id) AS creature_ids
    FROM
        CREATURES c
    JOIN CREATURE_SIGHTINGS cs ON c.creature_id = cs.creature_id
    JOIN CREATURE_TERRITORIES ct ON c.creature_id = ct.creature_id
    WHERE
        c.active = TRUE
    GROUP BY
        c.type, c.threat_level
),

VulnerabilityAnalysis AS (
    SELECT
        l.location_id AS zone_id,
        l.name AS zone_name,
        (COUNT(ah.location_id) * AVG(ah.military_response_time_minutes)) / NULLIF(l.fortification_level + l.trap_density, 0) AS vulnerability_score,
        COUNT(ah.location_id) FILTER (WHERE ah.outcome = 'Breach') AS historical_breaches,
        l.fortification_level,
        AVG(ah.military_response_time_minutes) AS military_response_time,
        JSON_OBJECT(
            'structure_ids', (SELECT JSON_ARRAYAGG(attack_id) FROM CREATURE_ATTACKS WHERE location_id = l.location_id),
            'squad_ids', (SELECT JSON_ARRAYAGG(squad_id) FROM SQUAD_OPERATIONS so WHERE so.location_id = l.location_id)
        ) AS defense_coverage
    FROM
        LOCATIONS l
    LEFT JOIN AttackHistory ah ON l.location_id = ah.location_id
    GROUP BY
        l.location_id, l.name, l.fortification_level, l.trap_density
),

DefenseEffectiveness AS (
    SELECT
        UNNEST(ah.defense_structures_used) AS defense_type,
        AVG(CASE WHEN ah.outcome IN ('Repelled', 'Victory') THEN 1.0 ELSE 0.0 END) * 100 AS effectiveness_rate,
        AVG(ah.enemy_casualties) AS avg_enemy_casualties
    FROM
        AttackHistory ah
    WHERE ah.defense_structures_used IS NOT NULL
    GROUP BY
        defense_type
),

MilitaryReadiness AS (
    SELECT
        ms.squad_id,
        ms.name AS squad_name,
        (SELECT AVG(ds.level) FROM DWARF_SKILLS ds JOIN SKILLS s ON ds.skill_id = s.skill_id WHERE s.skill_type = 'Combat' AND ds.dwarf_id IN (SELECT dwarf_id FROM SQUAD_MEMBERS sm WHERE sm.squad_id = ms.squad_id)) / 10 *
        (SELECT AVG(effectiveness) FROM SQUAD_TRAINING st WHERE st.squad_id = ms.squad_id) *
        (SELECT AVG(CASE WHEN outcome = 'Victory' THEN 1.0 ELSE 0.0 END) FROM SQUAD_BATTLES sb WHERE sb.squad_id = ms.squad_id) AS readiness_score,
        (SELECT COUNT(*) FROM SQUAD_MEMBERS sm WHERE sm.squad_id = ms.squad_id AND sm.exit_date IS NULL) AS active_members,
        (SELECT AVG(ds.level) FROM DWARF_SKILLS ds JOIN SKILLS s ON ds.skill_id = s.skill_id WHERE s.skill_type = 'Combat' AND ds.dwarf_id IN (SELECT dwarf_id FROM SQUAD_MEMBERS sm WHERE sm.squad_id = ms.squad_id)) AS avg_combat_skill,
        (SELECT AVG(effectiveness) FROM SQUAD_TRAINING st WHERE st.squad_id = ms.squad_id) AS combat_effectiveness,
        (SELECT JSON_ARRAYAGG(JSON_OBJECT('zone_id', so.location_id, 'response_time', 0)) FROM SQUAD_OPERATIONS so WHERE so.squad_id = ms.squad_id) AS response_coverage
    FROM
        MILITARY_SQUADS ms
),

SecurityEvolution AS (
    SELECT
        attack_year,
        AVG(CASE WHEN outcome IN ('Repelled', 'Victory') THEN 1.0 ELSE 0.0 END) * 100 AS defense_success_rate,
        COUNT(*) AS total_attacks,
        SUM(casualties) AS casualties,
        (AVG(CASE WHEN outcome IN ('Repelled', 'Victory') THEN 1.0 ELSE 0.0 END) * 100) -
        LAG(AVG(CASE WHEN outcome IN ('Repelled', 'Victory') THEN 1.0 ELSE 0.0 END) * 100, 1, 0) OVER (ORDER BY attack_year) AS year_over_year_improvement
    FROM
        AttackHistory
    GROUP BY
        attack_year
)

-- Финальный запрос
SELECT
    JSON_OBJECT(
        'total_recorded_attacks', (SELECT COUNT(*) FROM AttackHistory),
        'unique_attackers', (SELECT COUNT(DISTINCT creature_id) FROM AttackHistory),
        'overall_defense_success_rate', (SELECT AVG(CASE WHEN outcome IN ('Repelled', 'Victory') THEN 1.0 ELSE 0.0 END) * 100 FROM AttackHistory),
        'security_analysis', JSON_OBJECT(
            'threat_assessment', (
                SELECT JSON_OBJECT(
                    'current_threat_level', CASE
                        WHEN MAX(threat_level) >= 5 THEN 'Critical'
                        WHEN MAX(threat_level) >= 3 THEN 'High'
                        ELSE 'Moderate'
                    END,
                    'active_threats', (SELECT JSON_ARRAYAGG(JSON_OBJECT(
                        'creature_type', creature_type, 'threat_level', threat_level, 'last_sighting_date', last_sighting_date,
                        'territory_proximity', territory_proximity, 'estimated_numbers', estimated_numbers, 'creature_ids', creature_ids
                    )) FROM ThreatAssessment)
                ) FROM ThreatAssessment
            ),
            'vulnerability_analysis', (SELECT JSON_ARRAYAGG(JSON_OBJECT(
                'zone_id', zone_id, 'zone_name', zone_name, 'vulnerability_score', ROUND(vulnerability_score, 2),
                'historical_breaches', historical_breaches, 'fortification_level', fortification_level,
                'military_response_time', ROUND(military_response_time, 0), 'defense_coverage', defense_coverage
            )) FROM VulnerabilityAnalysis WHERE vulnerability_score > 0.5 ORDER BY vulnerability_score DESC),
            'defense_effectiveness', (SELECT JSON_ARRAYAGG(JSON_OBJECT(
                'defense_type', defense_type, 'effectiveness_rate', ROUND(effectiveness_rate, 2), 'avg_enemy_casualties', ROUND(avg_enemy_casualties, 2)
            )) FROM DefenseEffectiveness),
            'military_readiness_assessment', (SELECT JSON_ARRAYAGG(JSON_OBJECT(
                'squad_id', squad_id, 'squad_name', squad_name, 'readiness_score', ROUND(readiness_score, 2), 'active_members', active_members,
                'avg_combat_skill', ROUND(avg_combat_skill, 2), 'combat_effectiveness', ROUND(combat_effectiveness, 2), 'response_coverage', response_coverage
            )) FROM MilitaryReadiness ORDER BY readiness_score DESC),
            'security_evolution', (SELECT JSON_ARRAYAGG(JSON_OBJECT(
                'year', attack_year, 'defense_success_rate', ROUND(defense_success_rate, 2), 'total_attacks', total_attacks,
                'casualties', casualties, 'year_over_year_improvement', ROUND(year_over_year_improvement, 2)
            )) FROM SecurityEvolution)
        )
    ) AS security_report
FROM (SELECT 1) AS dummy;