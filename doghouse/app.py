from flask import Flask
from doghouse.routes import init_routes

def create_app():
    """
    Create and configure the Flask application.
    """
    app = Flask(__name__)
    
    # Initialize routes
    init_routes(app)
    
    return app

# Entry point for running the application
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
