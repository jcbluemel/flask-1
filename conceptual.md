### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python is mainly used for back-end development, JS mainly usually used for front-end, but can be used for back-end as well. Python code blocks are indented, JS uses {}. Python doesn't require variable keywords when defining. Python uses snake_case, JS uses camelCase. Python has no strict rules that create constant values, JS can use const. Undefined isn't a thing in Python. Python is more likely to throw errors, whereas JS will try and make things work. Data structures are different, Python has tuples, lists, dicts, etc. JS has arrays instead of lists and objects instead of dicts. There are vastly more libraries for Python than for JS.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your program crashing.

  The .get() method will return the value or 'Not Found'. You can use a try except to create an exception for the error, instead of having it crash the program.

- What is a unit test?

  A test to see if an individual component works, typically a function or method. Tests the component in isolation, rather than in integration with others. This ensures that the component perfoms as expected. This might involve testing if a function returns the correct value given its inputs.

- What is an integration test?

  A test that sees if components work together. While unit tests may pass individually, they may not integrate together cleanly. This might involve testing whether a route returns the right HTML, if something calls or returns from the correct API, redirects correctly, etc.

- What is the role of web application framework, like Flask?

  A web framework is a set of functions and classes that help you define which requests to respond to, and how to respond to requests. They help you handle web requests, produce dynamic HTML, handle forms and cookies, connect to databases, provide user authentication, caches for pages and more.

- You can pass information to Flask either as a parameter in a route URL (like
  `/foods/pretzel`) or using a URL query string param (like
  `foods?type=pretzel`). How might you choose which one is a better fit for an
  application?

  We can do similar things with both. However URL params are used more to display the subject as the page. They are used to output the entire static resource. They are usually kept shorter to be cleaner better for search engines. Query params are generally to pass 'more' info about a page, rather than a page itself. They are often used when coming from a form. They effectively provide the key(s) in the URL, which can make for more readable URLs and dynamic content creation, rather than being tuned for search engines.

- How do you collect data from a URL placeholder parameter using Flask?

  Adding <example> placeholders in the URL (@app.get('/hello/<there>')) and accepting the same argument in the view function (def general_kenobi(there):).

- How do you collect data from the query string using Flask?

  Request.args.get('key') can retrieve key, request.args will return a dict like object with all the keys and their values.

- How do you collect data from the body of a POST request using Flask?

  POST requests are often from a form, so request.form can be used. Request.data can retrieve the raw POST request body, and request.get_json can retrieve parsed JSON data.

- What is a cookie and what kinds of things are they commonly used for?

Cookies are a way to store small bits of info by the client (in the browser). They are a name/string-value pair that the server tells the client to store. The client sends cookies to the server with each request. They help the client remember information about your visit.

- What is the session object in Flask?

  A session object contains key value pairs for session variables and associated values. They contain info for the current browser, while preserving their type (unlike cookies). They are serialized and signed (though not secret), so users can't modify the data. By default in Flask, they are stored in the browser as a cookie.


- What are the two things Flask's `jsonify()` does?

  It serializes data to JSON format and wraps it in a Response object with the application/json mimetype, telling the browser that "this is JSON" data

- What was the hardest part of this past week for you?
  What was the most interesting?

  Hardest: I felt like I ran into far more 'syntax' roadblocks this week than I did in the previous 2. This was especially stark in testing, where it felt like the examples in lecture barely covered how we were supposed to write integration tests, which led to random googling and eventually asking for help. It came up again during this assignment, where the tests we wrote during the exercises were for different types of functionality, so the tests had to be written differently (with barely any help in the notes or exercises).

  Interesting: Once I actually had working tests (which I wrote at the end), my entire program felt much more secure. Both in the sense that I felt I could experiment with some changes, and somehow a relief that I could look at it again in the future and have some guiderails. Was really surprised at how strong the feeling was, and I really hope we can nail down the syntactical issues so I can experiment more.
