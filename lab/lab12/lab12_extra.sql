.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date,a.color,a.pet,a.number,b.number FROM students AS a join fa17students as b
  on a.date=b.date and a.color=b.color and a.pet=b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT seven FROM (SELECT * FROM students WHERE number=7 and time in (select time from checkboxes where checkboxes.'7' is 'True'));

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number,count(*) as cnt FROM fa17students
  GROUP BY number
  order by cnt desc
  limit 1;


CREATE TABLE fa17favpets AS
  SELECT pet,COUNT(*) AS cnt FROM fa17students
  GROUP BY pet
  ORDER BY cnt desc,pet
  LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet,COUNT(*) AS cnt FROM students
  GROUP BY pet
  ORDER BY cnt desc,pet
  LIMIT 10;

CREATE TABLE sp18dog AS
  SELECT 'dog',count(*) FROM students WHERE pet ='dog';


CREATE TABLE sp18alldogs AS
  SELECT 'dog',count(*) FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven,denero,count(*) as cnt FROM students
  WHERE seven = '7'
  GROUP BY seven,denero
  order by seven,denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count
  FROM students
  GROUP BY smallest
  ORDER BY smallest;
