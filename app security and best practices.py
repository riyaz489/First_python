# 1. update applications and system resources time to time , newer versions comes with security patches
# which removes the existing vulnebrilities. example older version of python jwt decode packages has none_algo
# vulnebrility which is removed in newer versions.

# 2. if-if ladder with equality condition, can be replaced with dict to make code more cleaner and dynamic

# 2. Practice the principle of least privilege. This foundational security principle holds that subjects
# (users, processes, programs, systems, devices) be granted only the minimum necessary access to complete a stated
# function. example: In aws security groups we can open backend app only for reverse proxy/api gateway IP. so that no
# one access backend except api_gateway or reverse proxy, if your API is not for public use.
# and we can also whitelist some origins in backend CORS configuration, if API is not public, otherwise use * to make it
# accessible for all origins.

# 3. Encrypt traffic using TLS

# 4. It is not safe to call yaml.load with any data received from an untrusted source! yaml.load is as powerful as
# pickle.load and so may call any Python function."
# so use yaml.safe.load option instead.

# 5. don't use pickle to deserialize data, because any one can execute command on sever side using pickle.
# so use some serializablle pattern, for exmaple json.

# 6. Ensure that APIs only return as much information as is necessary to fulfill their function.

# 7. Use rate limiting. Setting a threshold above which subsequent requests will be rejected (for example, 10,000
# requests per day per account) can prevent denial-of-service and brute force attacks. we can set rate limiting on
# both reverse  proxy like nginx and application level also like django. can set different rate limit for different
# end points like for open endpoints (login, register, home page,etc) we can set lesser number of request/ day (example
# 500/day) and for authorized reuquest(req with token, like update username) we can set more number
# of request/ day (example 10,000/day)

# 8. manage secrets properly, like rotate them timely and don't write them in directly in code. using some secret
# management machenism. (like aws secret manager or aws parameter store)

# 9. Use a web application firewall to control inbound and outgoing traffic of API.

# 10. Use ORMs (Object Relational Mapping Tools) for executing db queries, to avoid sql injection. like django ORM.
# because  Most ORMs have builtin sanitization methods. even if you need to write raw sql queries use django raw method
# package to run it.
# example: sql = 'SELECT * FROM something;'
#     qs = MyModel.objects.raw(sql, [])

# and also use Bento to automatically check Django code for SQL injection patterns.
# pip3 install bento-cli && \
# bento init && \
#  BENTO_REGISTRY=r/r2c.python.django.security.injection.sql bento check -t semgrep --all .


# 11. Use MFA, strong password policy, limit login fails, and invalidate tokens after logout to avoid broken security.

# 12. Disable server directory listing.

# 13. validate JWT token properly and check some required values like aud, algo, iss, expiry, etc.
# well I have created a doc for jwt security already.

# 14. change admin api default url.

# 15. for databases have a secure backup plan(like disaster recovery plan, automated backup, etc) and make them
# accessible only with some credentials(like in aws we can give our EC2 some role to access RDS resources ),
# also encrypt database at rest, to avoid data breaching, check aws SOP and aws checklist for more RDS securing info.

# 16. Never trust user input. always validate data and make sure its string before using it.
# (we can nginx to validate if input data is in correct json form or not.)

# 17. use linting tools like bandit and Pysa

# 18. use 'defusedxml' to parse xml files, it secures from DOS attacks happended while parsing xml files.
# (most common DOS attack while parsing xml is `billion laughs`)

# 19. use asserts statements only in unittesting.

# 20. In 'timing-attacks' attackers try to find out how much time your algo takes to compare given credentials
# with valid one. so timing attack nearly impossible in case of remote server(like APIs), becuase internet speed,
# and other factors are added to response time, so timing-attack is only useful in case of terminal applications.
# example of timing attack is `ssh based timing attack`. to avoid timing attack use `secrets.compare_digest`
# which is intorduced in python 3.5,  to compare secrets and passwords.

# 21. Use a service like PyUp.io to check for dependencies packages updates, it raise pull/merge requests to your
# application and run your tests to keep the packages up to date.

# 22. Use virtual environments for all applications, so that we can manage dependencies project wise very easily,
# and also our main python package directory does not get FLOODED with unnecessary python packages.

# 23. use netstat command to find all running ports and close the unnecessary ones. similarly use firewall to
# close unnecessary open ports

# 24. lock your dependencies, i.e specify exact version of your dependencies (example request==4.2.1 not request==4.2.*)
# so we can ensure that, we got same version of dependencies across all our machines.also sometimes build will fails
# due to updated dependencies and sub-dependencies.
# to lock dependencies we will use pipenv package for virtual evnironment which will create pipefile.lock for us.


# 25.The server should never assume the Accept and Content-Type header it should always check that the Accept and
# Content-Type header and if it is unexpected then return with a 406 Not Acceptable response.

# 25. handle exceptions properly to increase security, because exceptions leaks some info through stacktrace for
# attackers:
# a) Manage exceptions in a centralized manner to avoid duplicated try/catch blocks in the code.
# b) Ensure that all unexpected behavior is correctly handled inside the application.
# c) Ensure that error messages displayed to users do not leak critical data, but are still verbose enough to enable
#    the proper user response.
# d) Ensure that exceptions are logged in a way that gives enough information for support, QA, forensics or incident
#    response teams to understand the problem.
# e) ensure that proper status code is sent to client in response

# we can use below template for error response:

# note: here title/error_code and more_info are optional
# we can store error title,desc, status_code in enum
# for  normal errors
# status_code = 401
# response=
# { data : null,
#  errors: [
#       {
#     "title/error_code": "Incorrect username or password.",
#     "status": 401(The HTTP response code),
#     "detail": "Authentication failed due to incorrect username or password.",
#     "instance": "/login/log/abc123(uri where error occured)",
#     "timestamp": "2021-01-27T10:37:18.261969343Z",
#     "more_info": " errors/invalid_auth (A URI identifier that categorizes the error)"
#
#       },
#       {...
#       }
#  ]
# }

# for success response
# status_code = 200
# response =
# {
# data: {...},
# errors: null
# }

# for failed input validation
# status code = 400
# response =
# {
# data: null,
# errors: [{
#    "title/error_code": "Input validation failed.",
#    "status": 400,
#    "instance": "/login/log/abc123(uri where error occured)",
#     "timestamp": "2021-01-27T10:37:18.261969343Z",
#     "more_info": " errors/validation_failed "
#   "detail" : [
#     {
#       "title/error_code" : "invalid name",
#       "field" : "first_name",
#       "message" : "First name cannot have fancy characters"
#     "more_info": " errors/validation_failed/first_name "

#     },
#     {
#        "code" : "invalid pass",
#        "field" : "password",
#        "message" : "Password cannot be blank"
#     "more_info": " errors/validation_failed/password "

#     }
#   ]
# }]
#
# }

# Note: 401 vs 403
# i) Has the user not provided authentication credentials? Were they invalid? 👉 401 Unauthorized.
# ii) Was the user correctly authenticated, but they don’t have the required permissions to access the
# resource? 👉 403 Forbidden.

# 26.document your code and use something like swagger to view all endpoints and their docmentation.
# 27. API URL best practices:
#   a) use plural nouns instead of verbs in urls
# example: GET /employees, not GET /fetch_employees, not GET /employee
#   b) Allow filtering, sorting, and pagination
#   c) version API using url. example: localhost/v1/employees


# 28. do pen-teting and load-testing.
# 29. do follow famous compliance like ISO, PCI, etc. to reduce security issues.
# 30 use raise instead of early return.
# 31. use if conditions on bad path instead of happy path.
# 32. for temp files always use tempfile package and delete them using context-manager or try-finally block
# 33. use time.monotonic instead of time.time,
# Note: that monotonic this time will not be comparable to times from the built-in time function.
# A monotonic clock is a time source that won't ever jump forward or backward (due to NTP or Daylight Savings
# Time updates) The only real use of the value is comparing against other values returned from time.monotonic().
# 34. use pytz for timezones.
# 35. don't use mutable types as default argument. eg `def a(x=[]):`
# instead do this : def a(x=None):
#                        if x is None:
#                            x=[]
# 36. use [] and {} over list() and set(), because they are faster.
# 37. specify timeout for each http-request.
# 38. don't use import *, use selective import instead.
# 39. do not push business logic in exception handler:
#     i.e instead of `raise Exception('tax in invalid')` we can use raise Exception('Amount in invalid')
# 40. except Exception as e:
#       return {'message':str(e)}
# handle some specific exception type and return some handwritten message instead of `e`. note: but in logs and db we
# can still store original exceptions.
# 41. during deployment always scan the deployed image and all libraries and dependencies for vulnerabilities.(app-scan)
# 42. also put a scanner in your code repo also which will scan the dependencies periodically in your
# latest code-base and send you alerts on that. (dependbot,snyk in github)
# 43. set encryption mechanism for PII information. so before storing PII info in db or logs we need to encrypt it.
# for that we can use AES for data encryption and RSA(as rsa is slow) for key encryption, and we
# need some key management in place also, to rotate and store keys separately.
