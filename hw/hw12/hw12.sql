CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs join sizes
  on dogs.height>sizes.min and dogs.height<=max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT dog1.name FROM dogs AS dog1  join parents on dog1.name=parents.child  join dogs as dog2 on parents.parent=dog2.name
  where parents.parent is not null
  order by dog2.height desc
  ;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  select p1.child as n1,p2.child as n2 FROM parents AS p1 join parents as p2 on p1.parent=p2.parent
  where p1.child <p2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT n1 || ' and ' || n2 || ' are ' || s1.size || ' siblings' FROM siblings join size_of_dogs as s1 on n1=s1.name join size_of_dogs as s2 on n2=s2.name
  where s1.size=s2.size;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

INSERT into stacks_helper(dogs, stack_height, last_height)
  SELECT name,height,height FROM dogs;

-- Add your INSERT INTOs here
INSERT into stacks_helper(dogs, stack_height, last_height)
  select dogs || ', ' || name, stack_height+height,height from stacks_helper,dogs
  where height>last_height;

INSERT into stacks_helper(dogs, stack_height, last_height)
  select dogs || ', ' || name, stack_height+height,height from stacks_helper,dogs
  where height>last_height;

INSERT into stacks_helper(dogs, stack_height, last_height)
  select dogs || ', ' || name, stack_height+height,height from stacks_helper,dogs
  where height>last_height;

CREATE TABLE stacks AS
  SELECT dogs,stack_height FROM stacks_helper WHERE stack_height>170 order by stack_height;
