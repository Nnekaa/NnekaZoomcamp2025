# Week 1 Homework


#QUESTION 3

SELECT COUNT(*) AS trip_count,
CASE
WHEN DATE(lpep_dropoff_datetime) >= '2019-10-01'
AND DATE(lpep_dropoff_datetime) < '2019-11-01' 
AND trip_distance <= 1.0
THEN 'up to 1 mile'

WHEN DATE(	lpep_dropoff_datetime) >= '2019-10-01'
AND DATE(lpep_dropoff_datetime) < '2019-11-01' 
AND trip_distance >= 1.0
AND trip_distance < 3.0
THEN 'Between 1 and 3'

WHEN DATE(	lpep_dropoff_datetime) >= '2019-10-01'
AND DATE(lpep_dropoff_datetime) < '2019-11-01' 
AND trip_distance >= 3.0
AND trip_distance < 7.0
THEN 'Between 3 and 7'

WHEN DATE(	lpep_dropoff_datetime) >= '2019-10-01'
AND DATE(lpep_dropoff_datetime) < '2019-11-01' 
AND trip_distance >= 7.0
AND trip_distance < 10.0
THEN 'Between 7 and 10'

WHEN DATE(lpep_dropoff_datetime) >= '2019-10-01'
AND DATE(lpep_dropoff_datetime) < '2019-11-01' 
AND trip_distance >= 10.0
THEN 'over 10 miles'

END AS trip_mile_category

FROM public.green_tripdata_2019
GROUP BY trip_mile_category



#QUESTION 4

SELECT DATE(lpep_pickup_datetime),
MAX(trip_distance) AS max_trip_distance
FROM green_tripdata_2019
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY max_trip_distance DESC



#QUESTION 5

SELECT DATE(lpep_pickup_datetime),
SUM(total_amount) AS tm, gz."Zone"
FROM green_tripdata_2019 gt
JOIN green_zone_lookup gz
ON gt."PULocationID" = gz."LocationID"
WHERE DATE(lpep_pickup_datetime) = '2019-10-18'
GROUP BY DATE(lpep_pickup_datetime), gz."Zone"
HAVING SUM(total_amount)> 13000

