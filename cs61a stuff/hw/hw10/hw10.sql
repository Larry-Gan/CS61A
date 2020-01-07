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
  SELECT d.name as name, s.size as size FROM dogs as d, sizes as s WHERE s.max>=d.height AND d.height>s.min;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child FROM parents as p, dogs as d WHERE p.parent=d.name ORDER BY -d.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT p1.child AS sib1, p2.child as sib2 FROM parents as p1, parents as p2
  WHERE p1.parent=p2.parent AND p1.child<p2.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT sib1 || ' and ' || sib2 || ' are ' || s1.size || ' siblings'
  FROM siblings, size_of_dogs as s1, size_of_dogs as s2
  WHERE s2.size = s1.size AND s1.name = sib1 AND s2.name = sib2;
--   SELECT  FROM siblings;
-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

INSERT INTO stacks_helper(dogs,stack_height, last_height) SELECT d.name, d.height, d.height FROM dogs as d;
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT dogs||', '||d.name, stack_height+d.height, d.height FROM dogs as d,stacks_helper
WHERE last_height < d.height;
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT dogs||', '||d.name, stack_height+d.height, d.height FROM dogs as d,stacks_helper
WHERE last_height < d.height;
INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT dogs||', '||d.name, stack_height+d.height, d.height FROM dogs as d,stacks_helper
WHERE last_height < d.height;


CREATE TABLE stacks AS
  SELECT s1.dogs, s1.stack_height FROM stacks_helper as s1
  WHERE s1.stack_height>=170
  ORDER BY s1.stack_height;
