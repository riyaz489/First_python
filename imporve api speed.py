# 1. caching

# 2. DB connection pooling: it helps to save connections. So in future if same client making
# db request then instead of opening new connection we can reuse the saved cnnection.
# which will save time. also connection pooling helps to manage number of active connections.
# lets say in normal scenario if lot users mking db call at once, then our db might crash. but if we add connection pooler as reverse proxy
# then it will handle incoming request, and if no. of connections exceeding provided limit then pooler will stop new requests.

# 3. avod N+1 query problem: let say first we fetch all studenet using single query, then we are fetching marks of all students one by one using student id in where clause.
# which will be n+1 api calls to db. instead we can us joins to make single db call and fetch all result.

# 4.pagination of response

# 5. use fast json serializtion lib, because for every req and res we are going to use it.
# so a slow lib can make a noticable difference.

# 6.compress large request/response payloads  (example brotli algo)

# 7. writing logs asyncronously: because writing logs directly to disk can increase some latency. so we can
# synchronously write logs to disk.
