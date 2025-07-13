WITH CivilizationTradeStats AS (
    SELECT
        c.civilization_type,
        COUNT(DISTINCT c.caravan_id) AS total_caravans,
        SUM(tt.value) AS total_trade_value,
        SUM(CASE WHEN tt.balance_direction = 'Export' THEN tt.value ELSE -tt.value END) AS trade_balance,
        CORR(
            (CASE WHEN tt.balance_direction = 'Export' THEN tt.value ELSE -tt.value END),
            de.relationship_change
        ) AS diplomatic_correlation,
        JSON_ARRAYAGG(DISTINCT c.caravan_id) AS caravan_ids
    FROM
        CARAVANS c
    LEFT JOIN TRADE_TRANSACTIONS tt ON c.caravan_id = tt.caravan_id
    LEFT JOIN DIPLOMATIC_EVENTS de ON c.caravan_id = de.caravan_id
    GROUP BY
        c.civilization_type
),

ImportDependencies AS (
    SELECT
        cg.material_type,
        (SUM(cg.quantity) * AVG(cg.value / NULLIF(cg.quantity, 0))) / COUNT(DISTINCT c.civilization_type) AS dependency_score,
        SUM(cg.quantity) AS total_imported,
        COUNT(DISTINCT c.civilization_type) AS import_diversity,
        JSON_ARRAYAGG(DISTINCT cg.original_product_id) AS resource_ids
    FROM
        CARAVAN_GOODS cg
    JOIN CARAVANS c ON cg.caravan_id = c.caravan_id
    WHERE cg.type = 'Import'
    GROUP BY
        cg.material_type
    ORDER BY dependency_score DESC
    LIMIT 5
),

ExportEffectiveness AS (
    SELECT
        w.type AS workshop_type,
        p.type AS product_type,
        (SUM(CASE WHEN cg.type = 'Export' THEN wp.quantity ELSE 0 END)::NUMERIC * 100) / SUM(wp.quantity) AS export_ratio,
        AVG((cg.value / NULLIF(cg.quantity, 0)) / NULLIF(p.value, 0)) AS avg_markup,
        JSON_ARRAYAGG(DISTINCT w.workshop_id) AS workshop_ids
    FROM
        PRODUCTS p
    JOIN WORKSHOPS w ON p.workshop_id = w.workshop_id
    JOIN WORKSHOP_PRODUCTS wp ON p.product_id = wp.product_id
    JOIN CARAVAN_GOODS cg ON p.product_id = cg.original_product_id AND cg.type = 'Export'
    GROUP BY
        w.type, p.type
    ORDER BY export_ratio DESC
),

TradeTimeline AS (
    SELECT
        EXTRACT(YEAR FROM tt.date) AS year,
        EXTRACT(QUARTER FROM tt.date) AS quarter,
        SUM(tt.value) AS quarterly_value,
        SUM(CASE WHEN tt.balance_direction = 'Export' THEN tt.value ELSE -tt.value END) AS quarterly_balance,
        COUNT(DISTINCT c.civilization_type) AS trade_diversity
    FROM
        TRADE_TRANSACTIONS tt
    JOIN CARAVANS c ON tt.caravan_id = c.caravan_id
    GROUP BY
        year, quarter
    ORDER BY
        year, quarter
)

-- Финальный запрос
SELECT
    JSON_OBJECT(
        'total_trading_partners', (SELECT COUNT(*) FROM CivilizationTradeStats),
        'all_time_trade_value', (SELECT SUM(total_trade_value) FROM CivilizationTradeStats),
        'all_time_trade_balance', (SELECT SUM(trade_balance) FROM CivilizationTradeStats),
        'civilization_data', (
            SELECT JSON_OBJECT(
                'civilization_trade_data', (
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'civilization_type', civilization_type,
                            'total_caravans', total_caravans,
                            'total_trade_value', total_trade_value,
                            'trade_balance', trade_balance,
                            'trade_relationship', CASE WHEN trade_balance > 0 THEN 'Favorable' ELSE 'Unfavorable' END,
                            'diplomatic_correlation', ROUND(diplomatic_correlation, 2),
                            'caravan_ids', caravan_ids
                        )
                    )
                    FROM CivilizationTradeStats
                )
            )
        ),
        'critical_import_dependencies', (
            SELECT JSON_OBJECT(
                'resource_dependency', (
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'material_type', material_type,
                            'dependency_score', ROUND(dependency_score, 2),
                            'total_imported', total_imported,
                            'import_diversity', import_diversity,
                            'resource_ids', resource_ids
                        )
                    )
                    FROM ImportDependencies
                )
            )
        ),
        'export_effectiveness', (
            SELECT JSON_OBJECT(
                'export_effectiveness', (
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'workshop_type', workshop_type,
                            'product_type', product_type,
                            'export_ratio', ROUND(export_ratio, 2),
                            'avg_markup', ROUND(avg_markup, 2),
                            'workshop_ids', workshop_ids
                        )
                    )
                    FROM ExportEffectiveness
                )
            )
        ),
        'trade_timeline', (
            SELECT JSON_OBJECT(
                'trade_growth', (
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                            'year', year,
                            'quarter', quarter,
                            'quarterly_value', quarterly_value,
                            'quarterly_balance', quarterly_balance,
                            'trade_diversity', trade_diversity
                        )
                    )
                    FROM TradeTimeline
                )
            )
        )
    ) AS trade_analysis;