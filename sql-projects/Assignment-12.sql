1. Film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?
SELECT COUNT(*) FROM film WHERE length > (SELECT AVG(length) FROM film);
2. Film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?
SELECT COUNT(*) FROM film WHERE rental_rate = (SELECT MAX(rental_rate) FROM film);
3. Film tablosunda en düşük rental_rate ve en düşün replacement_cost değerlerine sahip filmleri sıralayınız.
SELECT * FROM film WHERE rental_rate = (SELECT MIN(rental_rate) FROM film) AND SELECT * FROM film WHERE replacement_cost = (SELECT MIN(replacement_cost FROM film);
4. Payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.
SELECT * FROM payment ORDER BY amount DESC;
