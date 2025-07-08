-- CTE 1: Собираем статистику по производству и материалам для каждой мастерской.
WITH WorkshopProductionStats AS (
    SELECT
        w.workshop_id,
        w.name AS workshop_name,
        w.type AS workshop_type,
        COUNT(DISTINCT wc.dwarf_id) AS num_craftsdwarves,
        COALESCE(SUM(wp.quantity), 0) AS total_quantity_produced,
        COALESCE(SUM(p.value * wp.quantity), 0) AS total_production_value,
        COALESCE(SUM(wm.quantity) FILTER (WHERE wm.is_input = TRUE), 0) AS total_materials_consumed,
        MIN(wp.production_date) AS first_production_date,
        MAX(wp.production_date) AS last_production_date,
        COUNT(DISTINCT wp.production_date) AS days_with_production
    FROM
        WORKSHOPS w
        LEFT JOIN WORKSHOP_CRAFTSDWARVES wc ON w.workshop_id = wc.workshop_id
        LEFT JOIN WORKSHOP_PRODUCTS wp ON w.workshop_id = wp.workshop_id
        LEFT JOIN PRODUCTS p ON wp.product_id = p.product_id
        LEFT JOIN WORKSHOP_MATERIALS wm ON w.workshop_id = wm.workshop_id
    GROUP BY
        w.workshop_id, w.name, w.type
),

-- CTE 2: Подготовка данных для анализа корреляции между навыком и качеством.
SkillQualityData AS (
    SELECT
        p.workshop_id,
        p.value AS product_value,
        (SELECT MAX(ds.level) FROM DWARF_SKILLS ds WHERE ds.dwarf_id = p.created_by) AS creator_max_skill_level
    FROM
        PRODUCTS p
    WHERE p.created_by IS NOT NULL AND p.workshop_id IS NOT NULL
),

-- CTE 3: Аналитика, включая корреляцию.
WorkshopAnalysis AS (
    SELECT
        wps.workshop_id,
        wps.workshop_name,
        wps.workshop_type,
        wps.num_craftsdwarves,
        wps.total_quantity_produced,
        wps.total_production_value,
        
        ROUND(
            wps.total_quantity_produced::NUMERIC / NULLIF(wps.last_production_date - wps.first_production_date + 1, 0),
        2) AS daily_production_rate,        
        ROUND(
            wps.total_production_value::NUMERIC / NULLIF(wps.total_materials_consumed, 0),
        2) AS value_per_material_unit,
        ROUND(
            wps.days_with_production::NUMERIC * 100 / NULLIF(wps.last_production_date - wps.first_production_date + 1, 0),
        2) AS workshop_utilization_percent,
        ROUND(
            wps.total_quantity_produced::NUMERIC / NULLIF(wps.total_materials_consumed, 0),
        2) AS material_conversion_ratio,
        (SELECT AVG(ds.level) FROM DWARF_SKILLS ds WHERE ds.dwarf_id IN (SELECT dwarf_id FROM WORKSHOP_CRAFTSDWARVES wc WHERE wc.workshop_id = wps.workshop_id)) AS average_craftsdwarf_skill,
        (SELECT CORR(sqd.product_value, sqd.creator_max_skill_level) FROM SkillQualityData sqd WHERE sqd.workshop_id = wps.workshop_id) AS skill_quality_correlation
    FROM
        WorkshopProductionStats wps
),

RelatedEntities AS (
    SELECT
        w.workshop_id,
        JSON_ARRAYAGG(DISTINCT wc.dwarf_id) FILTER (WHERE wc.dwarf_id IS NOT NULL) AS craftsdwarf_ids,
        JSON_ARRAYAGG(DISTINCT wp.product_id) FILTER (WHERE wp.product_id IS NOT NULL) AS product_ids,
        JSON_ARRAYAGG(DISTINCT wm.material_id) FILTER (WHERE wm.material_id IS NOT NULL) AS material_ids,
        JSON_ARRAYAGG(DISTINCT p.project_id) FILTER (WHERE p.project_id IS NOT NULL) AS project_ids
    FROM
        WORKSHOPS w
        LEFT JOIN WORKSHOP_CRAFTSDWARVES wc ON w.workshop_id = wc.workshop_id
        LEFT JOIN WORKSHOP_PRODUCTS wp ON w.workshop_id = wp.workshop_id
        LEFT JOIN WORKSHOP_MATERIALS wm ON w.workshop_id = wm.workshop_id
        LEFT JOIN PROJECTS p ON w.workshop_id = p.workshop_id
    GROUP BY w.workshop_id
)

SELECT
    JSON_ARRAYAGG(
        JSON_OBJECT(
            'workshop_id', wa.workshop_id,
            'workshop_name', wa.workshop_name,
            'workshop_type', wa.workshop_type,
            'num_craftsdwarves', wa.num_craftsdwarves,
            'total_quantity_produced', wa.total_quantity_produced,
            'total_production_value', wa.total_production_value,
            'daily_production_rate', COALESCE(wa.daily_production_rate, 0),
            'value_per_material_unit', COALESCE(wa.value_per_material_unit, 0),
            'workshop_utilization_percent', COALESCE(wa.workshop_utilization_percent, 0),
            'material_conversion_ratio', COALESCE(wa.material_conversion_ratio, 0),
            'average_craftsdwarf_skill', ROUND(COALESCE(wa.average_craftsdwarf_skill, 0), 2),
            'skill_quality_correlation', ROUND(COALESCE(wa.skill_quality_correlation, 0), 2),
            'related_entities', JSON_OBJECT(
                'craftsdwarf_ids', COALESCE(re.craftsdwarf_ids, '[]'::json),
                'product_ids', COALESCE(re.product_ids, '[]'::json),
                'material_ids', COALESCE(re.material_ids, '[]'::json),
                'project_ids', COALESCE(re.project_ids, '[]'::json)
            )
        )
    ) AS workshops_analysis
FROM
    WorkshopAnalysis wa
JOIN
    RelatedEntities re ON wa.workshop_id = re.workshop_id;