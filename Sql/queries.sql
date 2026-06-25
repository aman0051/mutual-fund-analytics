-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM nav_history;

-- 3. Total SIP Amount
SELECT SUM(amount_inr) AS total_sip
FROM investor_transactions
WHERE transaction_type='SIP';

-- 4. Transactions by State
SELECT state, COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- 6. Fund Count by Category
SELECT category, COUNT(*) AS total_funds
FROM scheme_performance
GROUP BY category;

-- 7. Average Return by Category
SELECT category,
AVG(return_1yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category;

-- 8. Total Transactions by Payment Mode
SELECT payment_mode,
COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY payment_mode;

-- 9. Highest 1 Year Return Funds
SELECT scheme_name, return_1yr_pct
FROM scheme_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 10. KYC Status Distribution
SELECT kyc_status,
COUNT(*) AS total_investors
FROM investor_transactions
GROUP BY kyc_status;