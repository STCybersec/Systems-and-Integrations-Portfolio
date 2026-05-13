-- ============================================================
-- Inventory Business Queries
-- Author: Sanele Siyabonga Thusi
-- Purpose: Operational insights for management reporting
-- ============================================================

USE inventory_supply;
GO

-- ============================================================
-- QUERY 1: Product Catalogue by Price (Descending)
-- ============================================================
SELECT
    product_id,
    brand,
    category,
    unit_cost_rand
FROM dbo.products
ORDER BY unit_cost_rand DESC;

-- ============================================================
-- QUERY 2: Total Stock Quantity Per Branch
-- ============================================================
SELECT
    b.branch_name,
    b.city,
    SUM(i.quantity) AS total_quantity
FROM dbo.branches b
JOIN dbo.inventory i ON b.branch_id = i.branch_id
GROUP BY b.branch_name, b.city
ORDER BY total_quantity DESC;

-- ============================================================
-- QUERY 3: Total Stock Value in Rands Per Branch
-- ============================================================
SELECT
    b.branch_name,
    b.city,
    SUM(i.quantity * p.unit_cost_rand) AS stock_value_rand
FROM dbo.branches b
JOIN dbo.inventory i ON b.branch_id = i.branch_id
JOIN dbo.products  p ON p.product_id = i.product_id
GROUP BY b.branch_name, b.city
ORDER BY stock_value_rand DESC;

-- ============================================================
-- QUERY 4: Low Stock Alert (Quantity Below 50)
-- Continuous Monitoring requirement
-- ============================================================
SELECT
    b.branch_name,
    p.brand,
    p.category,
    i.quantity,
    i.last_updated,
    'LOW STOCK - ACTION REQUIRED' AS alert_status
FROM dbo.inventory i
JOIN dbo.branches b ON b.branch_id = i.branch_id
JOIN dbo.products p ON p.product_id = i.product_id
WHERE i.quantity < 50
ORDER BY i.quantity ASC;

-- ============================================================
-- QUERY 5: Brand Performance Across All Branches
-- ============================================================
SELECT
    p.brand,
    p.category,
    SUM(i.quantity)  AS total_units,
    SUM(i.quantity * p.unit_cost_rand) AS total_value_rand
FROM dbo.products  p
JOIN dbo.inventory i ON p.product_id = i.product_id
GROUP BY p.brand, p.category
ORDER BY total_value_rand DESC;

-- ============================================================
-- QUERY 6: Delivery Status Report
-- System Integration + Monitoring requirement
-- ============================================================
SELECT
    d.delivery_id,
    b.branch_name,
    p.brand,
    d.quantity,
    d.delivery_date,
    d.status,
    CASE
        WHEN d.status = 'Failed'     THEN 'URGENT - Investigate'
        WHEN d.status = 'Pending'    THEN 'MONITOR - Not dispatched'
        WHEN d.status = 'In Transit' THEN 'ACTIVE - En route'
        ELSE 'COMPLETE'
    END AS action_required
FROM dbo.deliveries d
JOIN dbo.branches b ON b.branch_id = d.branch_id
JOIN dbo.products p ON p.product_id = d.product_id
ORDER BY d.delivery_date DESC;

-- ============================================================
-- QUERY 7: Unresolved System Alerts Dashboard
-- Continuous Monitoring + Uptime Management
-- ============================================================
SELECT
    sa.alert_id,
    sa.alert_type,
    sa.description,
    b.branch_name,
    sa.alert_date,
    CASE WHEN sa.resolved = 0 THEN 'OPEN' ELSE 'RESOLVED' END AS status
FROM dbo.system_alerts sa
JOIN dbo.branches b ON b.branch_id = sa.branch_id
WHERE sa.resolved = 0
ORDER BY sa.alert_date ASC;

-- ============================================================
-- QUERY 8: Executive Summary View
-- ============================================================
SELECT
    b.branch_name,
    SUM(i.quantity)                                          AS total_units,
    SUM(i.quantity * p.unit_cost_rand)                       AS total_value_rand,
    SUM(CASE WHEN i.quantity < 50 THEN 1 ELSE 0 END)         AS low_stock_items,
    COUNT(DISTINCT CASE WHEN d.status = 'Failed'
          THEN d.delivery_id END)                            AS failed_deliveries
FROM dbo.branches b
JOIN dbo.inventory  i  ON b.branch_id = i.branch_id
JOIN dbo.products   p  ON p.product_id = i.product_id
LEFT JOIN dbo.deliveries d ON b.branch_id = d.branch_id
GROUP BY b.branch_name
ORDER BY total_value_rand DESC;

