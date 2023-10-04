'''
from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=G-4MN0VH6MBL"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-4MN0VH6MBL');
    </script>
     """
    return prefix_google + "Hello World"



@app.route('/')
def root():
    return 'Hello, World!!'
'''
''' 2eme test
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4MN0VH6MBL"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-4MN0VH6MBL');
    </script>
    """
    return prefix_google + "Hello World"

@app.route('/logger')
def logger():
    # Log on the server (Python)
    print("Server-side log: This is a log message.")
    
    # Log on the browser (JavaScript)
    client_log_script = """
    <script>
        console.log("Client-side log: This is a log message.");
    </script>
    """
    return "Logging page" + client_log_script

if __name__ == "__main__":
    app.run()
'''


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-4MN0VH6MBL"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-4MN0VH6MBL');
    </script>
    """
    return prefix_google + "Hello World"

@app.route('/logger')
def logger():
    # Log on the server (Python)
    print("Server-side log: This is a log message.")
    
    # Log on the browser (JavaScript)
    client_log_script = """
    <script>
        console.log("Client-side log: This is a log message.");
    </script>
    """
    return "New page !!" + client_log_script

if __name__ == "__main__":
    app.run()


