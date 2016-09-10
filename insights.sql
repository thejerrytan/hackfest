-- 1. Areas with most orders

select u.postal,count(o.id) as NoOfOrders 
from user u inner join `order` o on u.id = o.user_id 
group by u.postal ORDER BY NoOfOrders DESC;

-- 2. Which region does most Elderly people (60 and above) shop at?

select u.postal, count(o.id) as NoOfOrders
from user u inner join `order` o on u.id = o.user_id
where u.age >= 60
group by u.postal;

-- 3. When are most orders delivered?

select count(*) as NoOfOrders
from `order` o
group by o.delivery_start and o.delivery_end;

-- 4. Are there more female customers or male customers in an area which purchases a particular product?
-- 5. which category of products has the most orders in a particular area?
-- 6. What is the total revenue for a particular delivery time?
-- 7. What is the average difference between order day and delivery day?
-- 8. Is it starkly different between corporate and individual customers?
-- 9. Does the total order discount affect the delivery timeslot?
-- 10. Does the delivery time slot affect the number of things each person buy?

-- Age profile of customers

SELECT age, COUNT(*) FROM user GROUP BY age ORDER BY age DESC;