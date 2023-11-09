# Building an API (another way of interacting with a database)

Now that you have seen how to use both the PSQL and Python script way of interacting with a database,
let us design a simple API where we interact with the database through a tool like Postman which immitates real world usage by other people of your data.

## Installation dependencies

It is preferred that you use a virtual environment when working with this code. Please create one.

Install dependencies of the project using the following command:

```bash
pip install -r requirements.txt
```

Some assumptions are being made
- You are connected to the correct database with all countries data
- You know how to hide passwords from the Python file through an environment variable of some sort. Hint: `.env`

# Create the following URL route

`https://localhost:5000/api/economic-data/<country>/<year>`

Please note that we shall be using an SQL statement that looks a lot like this:

```sql
SELECT c.name, e.year, p.fertility_rate, e.unemployment_rate
FROM countries c
INNER JOIN populations p
ON c.code = p.country_code
INNER JOIN economies e
ON p.year = e.year AND e.code = p.country_code
WHERE c.code ILIKE %s AND p.year IN ({years})
```

Return a dictionary that looks like this:


```json
{
    "year": 2003,
    "fertility_rate": 1.39,
    "unemployment_rate": 6.942
}
```

# Running the project

To run a flask application in the root of the project:

`FLASK_DEBUG=1 flask run`

When testing you can use Postman and input URL for example:

`http://localhost:5000/api/economic-data/DEU/2010`