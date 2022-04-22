import http.server, socketserver, webbrowser, os

# Switch the working directory to the same directory as `server.py` (since that's where we want to serve from)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.TCPServer(("", 8000), http.server.SimpleHTTPRequestHandler) as server:
    # Launch a new tab pointing to our landing page
    webbrowser.open_new_tab('http://localhost:8000/visualization.html')
    # Run the server forever
    server.serve_forever()
