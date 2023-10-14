import os
import requests
from flask import Flask, request, render_template, jsonify,redirect, url_for

app = Flask(__name__,template_folder = 'templatesTP')
'''
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
    return prefix_google + "    Hello World!Welcome to the Home page  "
'''
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
    return prefix_google + """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Home Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4b400;
                text-align: center;
                padding: 100px;
            }
            h1 {
                color: #fff;
            }
            p {
                color: #fff;
                font-size: 20px;
                margin-top: 40px;
            }
            button {
                background-color: #f90;
                color: #fff;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Home Page</h1>
        <p>Hello World!</p>
        <button onclick="window.location.href='/logger'">Go to Logger</button>
        <button onclick="window.location.href='/textbox'">Go to Textbox</button>
    </body>
    </html>
    """

       



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




@app.route('/textbox', methods=['GET', 'POST'])
def textbox():
    user_message = None
    if request.method == 'POST':
        user_message = request.form.get('message', '')
        
    req = requests.get("https://www.google.com/")
    req2 = requests.get("https://analytics.google.com/analytics/web/#/p408253641/reports/intelligenthome?params=_u..nav%3Dmaui&collectionId=user")
    
    return render_template('textbox.html', user_message=user_message,GA_rep=req2.cookies.get_dict())






@app.route('/statut_code')
def statut_code():
    ganalytics_url = "https://analytics.google.com/analytics/web/?#/p408253641/reports/intelligenthome?params=_u..nav%3Dmaui&collectionId=user"
    req = requests.get(ganalytics_url)
    status_code = req.status_code
    response_text = req.text
    return jsonify(status_code=status_code, text=response_text)







@app.route('/redirect-to-analytics', methods=['POST'])
def redirect_to_analytics():
    return redirect("https://analytics.google.com/analytics/web/#/p408253641/reports/intelligenthome?params=_u..nav%3Dmaui&collectionId=user")




@app.route("/make_google_request", methods=["GET"])
def make_google_request():
    try:
        # Make a request to Google
        response = requests.get("https://www.google.com/")

        # Check if the request was successful
        if response.status_code == 200:
            cookies = response.cookies.get_dict()
            return jsonify(cookies)
        else:
            return jsonify({"error": "Google request failed with status code: " + str(response.status_code)})
    except Exception as e:
        return jsonify({"error": "An error occurred: " + str(e)})


@app.route("/make_google_request2", methods=["GET"])
def make_google_request2():
    try:
        import requests

        # Request to Google Analytics
        response = requests.get("https://analytics.google.com/analytics/web/#/p408253641/reports/intelligenthome?params=_u..nav%3Dmaui&collectionId=user")

        # Check if it works
        if response.status_code == 200:
            return jsonify(response.cookies.get_dict())
        else:
            return jsonify({"error": f"Google request failed with status code: {response.status_code}"})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"})
 
    

if __name__ == "__main__":
    app.run()




#To display in my computer the statut of the code I had some problem to display it on my page /textbox
url = "https://analytics.google.com/analytics/web/#/p408253641/reports/intelligenthome?params=_u..nav%3Dmaui&collectionId=user"


response = requests.get(url)

status_code = response.status_code
response_text = response.text

print(f"Status Code: {status_code}")
print(f"Response Text: {response_text}")


