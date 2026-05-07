#11th
# Simulated Impala Output in VS Code JUST FOR REFERENCE


##BELOW CODE IS TO JUST SHOW THE EXAMPLE OF THE QUERY OUTPUT USING IMPALA ( IMP:NOT FOR PRACTICAL USE)
def print_line():
    print("-" * 50)

print("[Impala] > CREATE DATABASE test_db;")
print("Query: CREATE DATABASE test_db")
print("Fetched 0 row(s) in 0.10s\n")

print("[Impala] > USE test_db;")
print("Query: USE test_db")
print("Fetched 0 row(s) in 0.01s\n")

print("[Impala] > CREATE TABLE employees (id INT, name STRING, age INT, department STRING);")
print("Query: CREATE TABLE employees")
print("Fetched 0 row(s) in 0.12s\n")

print("[Impala] > INSERT INTO employees VALUES (1, 'Alice', 30, 'HR');")
print("Inserted 1 row(s) in 0.20s")

print("[Impala] > INSERT INTO employees VALUES (2, 'Bob', 35, 'Engineering');")
print("Inserted 1 row(s) in 0.18s")

print("[Impala] > INSERT INTO employees VALUES (3, 'Charlie', 40, 'Marketing');")
print("Inserted 1 row(s) in 0.19s\n")

print("[Impala] > SELECT * FROM employees;")

print("+----+----------+-----+-------------+")
print("| id | name     | age | department  |")
print("+----+----------+-----+-------------+")
print("| 1  | Alice    | 30  | HR          |")
print("| 2  | Bob      | 35  | Engineering |")
print("| 3  | Charlie  | 40  | Marketing   |")
print("+----+----------+-----+-------------+")
print("Fetched 3 row(s) in 0.15s\n")

print("[Impala] > SELECT * FROM employees WHERE department = 'Engineering';")

print("+----+------+-----+-------------+")
print("| id | name | age | department  |")
print("+----+------+-----+-------------+")
print("| 2  | Bob  | 35  | Engineering |")
print("+----+------+-----+-------------+")
print("Fetched 1 row(s) in 0.10s\n")

print("[Impala] > DROP TABLE employees;")
print("Query: DROP TABLE employees")
print("Fetched 0 row(s) in 0.08s\n")

print("[Impala] > DROP DATABASE test_db;")
print("Query: DROP DATABASE test_db")
print("Fetched 0 row(s) in 0.09s")