/* Write your T-SQL query statement below */
select d.dept_name, count(student_id) as student_number
from student s full outer join department d on s.dept_id = d.dept_id
group by d.dept_name
order by student_number desc, d.dept_name asc
