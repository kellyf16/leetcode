/* Write your T-SQL query statement below */
select Department, Employee, Salary
from (
    select d.name as Department, e.name as Employee, e.salary, max(e.salary) over (partition by d.id) as max_salary
    from department d inner join employee e on d.id = e.departmentId
) as x
where Salary = max_salary
