2.

SELECT
    d.dwarf_id,
    d.name,
    d.age,
    d.profession,
    JSON_OBJECT(
        'skill_ids', (
            SELECT JSON_ARRAYAGG(ds.skill_id)
            FROM DWARF_SKILLS ds
            WHERE ds.dwarf_id = d.dwarf_id
        ),
        'assignment_ids', (
            SELECT JSON_ARRAYAGG(da.assignment_id)
            FROM DWARF_ASSIGNMENTS da
            WHERE da.dwarf_id = d.dwarf_id
        ),
        'squad_ids', (
            SELECT JSON_ARRAYAGG(sm.squad_id)
            FROM SQUAD_MEMBERS sm
            WHERE sm.dwarf_id = d.dwarf_id
        ),
        'equipment_ids', (
            SELECT JSON_ARRAYAGG(de.equipment_id)
            FROM DWARF_EQUIPMENT de
            WHERE de.dwarf_id = d.dwarf_id
        )
    ) AS related_entities
FROM
    DWARVES d;
	
3.

SELECT
    w.workshop_id,
    w.name,
    w.type,
    w.quality,
    JSON_OBJECT(
        'craftsdwarf_ids', (
            SELECT JSON_ARRAYAGG(wc.dwarf_id)
            FROM WORKSHOP_CRAFTSDWARVES wc
            WHERE wc.workshop_id = w.workshop_id
        ),
        'project_ids', (
            SELECT JSON_ARRAYAGG(p.project_id)
            FROM PROJECTS p
            WHERE p.workshop_id = w.workshop_id
        ),
        'input_material_ids', (
            SELECT JSON_ARRAYAGG(wm.material_id)
            FROM WORKSHOP_MATERIALS wm
            WHERE wm.workshop_id = w.workshop_id AND wm.is_input = TRUE
        ),
        'output_product_ids', (
            SELECT JSON_ARRAYAGG(wp.product_id)
            FROM WORKSHOP_PRODUCTS wp
            WHERE wp.workshop_id = w.workshop_id
        )
    ) AS related_entities
FROM
    WORKSHOPS w;
	
4.

SELECT
    ms.squad_id,
    ms.name,
    ms.formation_type,
    ms.leader_id,
    JSON_OBJECT(
        'member_ids', (
            SELECT JSON_ARRAYAGG(sm.dwarf_id)
            FROM SQUAD_MEMBERS sm
            WHERE sm.squad_id = ms.squad_id
        ),
        'equipment_ids', (
            SELECT JSON_ARRAYAGG(se.equipment_id)
            FROM SQUAD_EQUIPMENT se
            WHERE se.squad_id = ms.squad_id
        ),
        'operation_ids', (
            SELECT JSON_ARRAYAGG(so.operation_id)
            FROM SQUAD_OPERATIONS so
            WHERE so.squad_id = ms.squad_id
        ),
        'training_schedule_ids', (
            SELECT JSON_ARRAYAGG(st.schedule_id)
            FROM SQUAD_TRAINING st
            WHERE st.squad_id = ms.squad_id
        ),
        'battle_report_ids', (
            SELECT JSON_ARRAYAGG(sb.report_id)
            FROM SQUAD_BATTLES sb
            WHERE sb.squad_id = ms.squad_id
        )
    ) AS related_entities
FROM
    MILITARY_SQUADS ms;

