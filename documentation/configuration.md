# Configuration

All configuration is done through environment variables. When running the application locally, environment variables are read from the `.env` file. The project includes an example configuration in `.env.dist`, which is meant to contain sensible defaults *for running locally*.

Env|default|required|description
---|-------|--------|-----------
|`PORT`|`5000`||The port the HTTP server will listen on.
|`FLASK_ENV`|`"development"`||Environment the application should run in. Set to `"production"` in production.
|`DEBUG`|||When `True`, the server will run in debug mode, and reloads when changes are made to the source code. Defaults to `True` when `FLASK_ENV` is set to `"development"`.
|`SESSION_SECRET`|`os.urandom(32)`||Secret used for signing session keys. Leaving this blank will result in a good secret, but since the secret changes every time the application reloads, users will also be logged out every time.
|`ADMIN_PASSWORD`|||Password for the `admin` user. Leaving this blank will make the admin user inaccessible.
|`DATABASE_URL`||Yes|Database connection URL.