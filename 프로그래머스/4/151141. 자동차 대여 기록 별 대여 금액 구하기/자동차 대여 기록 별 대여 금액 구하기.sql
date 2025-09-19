SELECT 
    h.history_id,
    ROUND(((DATEDIFF(h.end_date, h.start_date) + 1) * c.daily_fee) *
    (1 - (IFNULL(p.discount_rate, 0) / 100)), 0) AS fee
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
LEFT JOIN CAR_RENTAL_COMPANY_CAR c
    ON h.car_id = c.car_id
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
    ON CASE WHEN (DATEDIFF(h.end_date, h.start_date) + 1) >= 90 THEN '90일 이상'
            WHEN (DATEDIFF(h.end_date, h.start_date) + 1) >= 30 THEN '30일 이상'
            WHEN (DATEDIFF(h.end_date, h.start_date) + 1) >= 7 THEN '7일 이상' END
        = p.duration_type
    AND c.car_type = p.car_type
WHERE c.car_type = '트럭'
ORDER BY fee DESC, history_id DESC