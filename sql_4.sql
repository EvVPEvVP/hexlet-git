WITH ExpeditionMetrics AS (
    SELECT
        e.expedition_id,
        e.destination,
        e.status,
        (e.return_date - e.departure_date) AS expedition_duration,
        ROUND(
            (COUNT(DISTINCT em.dwarf_id) FILTER (WHERE em.survived = TRUE))::NUMERIC * 100
            / NULLIF(COUNT(DISTINCT em.dwarf_id), 0),
        2) AS survival_rate,
        COALESCE(SUM(ea.value), 0) AS artifacts_value,
        COUNT(DISTINCT es.site_id) AS discovered_sites,
        ROUND(
            (COUNT(*) FILTER (WHERE ec.outcome IN ('Victory', 'Favorable', 'Avoided')))::NUMERIC * 100
            / NULLIF(COUNT(ec.expedition_id), 0),
        2) AS encounter_success_rate

    FROM
        EXPEDITIONS e
        LEFT JOIN EXPEDITION_MEMBERS em ON e.expedition_id = em.expedition_id
        LEFT JOIN EXPEDITION_ARTIFACTS ea ON e.expedition_id = ea.expedition_id
        LEFT JOIN EXPEDITION_SITES es ON e.expedition_id = es.expedition_id
        LEFT JOIN EXPEDITION_CREATURES ec ON e.expedition_id = ec.expedition_id
    GROUP BY
        e.expedition_id
),
SkillGains AS (
    SELECT
        em.expedition_id,
        COALESCE(SUM(ds.level), 0) AS total_skill_improvement
    FROM
        EXPEDITION_MEMBERS em
        JOIN EXPEDITIONS e ON em.expedition_id = e.expedition_id
        JOIN DWARF_SKILLS ds ON em.dwarf_id = ds.dwarf_id
    WHERE
        ds.date > e.departure_date AND ds.date <= e.return_date
    GROUP BY
        em.expedition_id
),
RelatedEntities AS (
    SELECT
        e.expedition_id,
        JSON_ARRAYAGG(DISTINCT em.dwarf_id) FILTER (WHERE em.dwarf_id IS NOT NULL) AS member_ids,
        JSON_ARRAYAGG(DISTINCT ea.artifact_id) FILTER (WHERE ea.artifact_id IS NOT NULL) AS artifact_ids,
        JSON_ARRAYAGG(DISTINCT es.site_id) FILTER (WHERE es.site_id IS NOT NULL) AS site_ids
    FROM
        EXPEDITIONS e
        LEFT JOIN EXPEDITION_MEMBERS em ON e.expedition_id = em.expedition_id
        LEFT JOIN EXPEDITION_ARTIFACTS ea ON e.expedition_id = ea.expedition_id
        LEFT JOIN EXPEDITION_SITES es ON e.expedition_id = es.expedition_id
    GROUP BY
        e.expedition_id
),
Scoring AS (
    SELECT
        em.expedition_id,
        em.survival_rate,
        em.artifacts_value,
        em.discovered_sites,
        em.encounter_success_rate,
        COALESCE(sg.total_skill_improvement, 0) AS skill_improvement,
        (em.survival_rate - MIN(em.survival_rate) OVER()) / NULLIF(MAX(em.survival_rate) OVER() - MIN(em.survival_rate) OVER(), 0) AS norm_survival,
        (em.artifacts_value - MIN(em.artifacts_value) OVER()) / NULLIF(MAX(em.artifacts_value) OVER() - MIN(em.artifacts_value) OVER(), 0) AS norm_value,
        (em.discovered_sites - MIN(em.discovered_sites) OVER()) / NULLIF(MAX(em.discovered_sites) OVER() - MIN(em.discovered_sites) OVER(), 0) AS norm_sites,
        (em.encounter_success_rate - MIN(em.encounter_success_rate) OVER()) / NULLIF(MAX(em.encounter_success_rate) OVER() - MIN(em.encounter_success_rate) OVER(), 0) AS norm_encounters,
        (COALESCE(sg.total_skill_improvement, 0) - MIN(COALESCE(sg.total_skill_improvement, 0)) OVER()) / NULLIF(MAX(COALESCE(sg.total_skill_improvement, 0)) OVER() - MIN(COALESCE(sg.total_skill_improvement, 0)) OVER(), 0) AS norm_skills
    FROM
        ExpeditionMetrics em
        LEFT JOIN SkillGains sg ON em.expedition_id = sg.expedition_id
)
SELECT
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'expedition_id', s.expedition_id,
            'destination', m.destination,
            'status', m.status,
            'survival_rate', COALESCE(s.survival_rate, 0),
            'artifacts_value', s.artifacts_value,
            'discovered_sites', s.discovered_sites,
            'encounter_success_rate', COALESCE(s.encounter_success_rate, 0),
            'skill_improvement', s.skill_improvement,
            'expedition_duration', m.expedition_duration,
            'overall_success_score', ROUND(
                (
                    COALESCE(s.norm_survival, 0) * 0.30 +
                    COALESCE(s.norm_value, 0) * 0.25 +
                    COALESCE(s.norm_skills, 0) * 0.20 +
                    COALESCE(s.norm_sites, 0) * 0.15 +
                    COALESCE(s.norm_encounters, 0) * 0.10
                ), 2
            ),
            'related_entities', JSON_OBJECT(
                'member_ids', COALESCE(re.member_ids, '[]'::json),
                'artifact_ids', COALESCE(re.artifact_ids, '[]'::json),
                'site_ids', COALESCE(re.site_ids, '[]'::json)
            )
        ) ORDER BY overall_success_score DESC
    ) AS expeditions_analysis
FROM
    Scoring s
JOIN ExpeditionMetrics m ON s.expedition_id = m.expedition_id
JOIN RelatedEntities re ON s.expedition_id = re.expedition_id;
