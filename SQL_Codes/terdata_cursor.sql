DECLARE countRows INTEGER;
DECLARE flag INTEGER;
DECLARE comp_id INTEGER;

DECLARE etype VARCHAR(100);
DECLARE ename VARCHAR(10000);
DECLARE eemail VARCHAR(100);


DECLARE sampleAccountCur CURSOR FOR
SELECT name, type,email
FROM employee_account
WHERE type  NOT IN (SELECT department_type FROM employee_department)
ORDER BY 1,2;

OPEN sampleAccountCur;
   SET countRows = ACTIVITY_COUNT;
   SET flag = 1;
   SET comp_id = 0;
   REPEAT
      FETCH
         sampleAccountCur
      INTO
          ename
         ,etype
         ,eemail
      ;
   
   update employee_project set type = etype, email=eemail ;
   
   -- there may be n number of sqls can run inside cursor
   --- sql 1
   -- sql 2
   ---sql 3
  
  UNTIL countRows <= 0

  END REPEAT;

  CLOSE sampleAccountCur;