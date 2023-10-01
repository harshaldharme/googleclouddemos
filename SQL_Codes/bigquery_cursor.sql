DECLARE countRows INT64;
DECLARE flag INT64;
DECLARE comp_id INT64;

DECLARE etype STRING;
DECLARE ename STRING;
DECALRE eemail STRING;


FOR sampleAccountCur IN ( SELECT name, type,email
FROM employee_account
WHERE type  NOT IN (SELECT department_type FROM employee_department)
ORDER BY 1,2)

  DO
   SET countRows = @@row_count;
   SET flag = 1;
   SET comp_id = 0;
 BEGIN
 
-- we can use clumn name with reference of cursor name
   SET ename = sampleAccountCur.name;
   SET etype = sampleAccountCur.type;
   SET eemail = sampleAccountCur.email;
 
  update employee_project set type = etype, email=eemail ;
  
  -- there may be n number of sqls can run inside cursor
  --- sql 1
  -- sql 2
  ---sql 3
 
 END;
 END FOR;