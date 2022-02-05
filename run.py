# Run the test server

from app import app

# Run Flask instance created in __init__
app.run(host='127.0.0.1', port=8080, debug=True)


