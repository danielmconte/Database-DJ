### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  ##### A relation database mananagement system.
- What is the difference between SQL and PostgreSQL?
  #### PostgreSQL extends SQL adding additional support and features

- In `psql`, how do you connect to a database?
##### Not sure if this is what is meant, but you create_db filename, or if already created just psql filename, then \dt to see tables 

- What is the difference between `HAVING` and `WHERE`?
  ##### WHERE is used more as a filter for the query, and HAVING tends to wittle down groups (especially when used with GROUP BY) 

- What is the difference between an `INNER` and `OUTER` join?
##### Using a Venn Diagram to visualize, INNER join would be the middle section (the crossover) where OUTER would include the middle section and specified other sections (RIGHT JOIN the right side, FULL JOIN everything) 
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
##### LEFT OUTER (OR LEFT JOIN) includes the middle section (again using a Venn Diagram to visualize) and the left section. And RIGHT OUTER is the same but with the right section instead of left.

- What is an ORM? What do they do?
  ##### Object-Relational Mapping, in this case SQLAlchemy serves as a translation service between the server language (Python) and the database(SQL) 

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  ##### With http requests it is going through client-side browser, where using requests on the server side cuts out the additional steps of taking the external API from server to client back to the server, before heading to your personal db   

- What is CSRF? What is the purpose of the CSRF token?
##### Cross-Site Request Forgery, the token makes sure the data submitted comes from our oun app's form. 
- What is the purpose of `form.hidden_tag()`?
##### Hides the CSRF token so that it is not iterated over in the for loop
