from server import create_app
#import blue prints
from server.route.server_test import test_bp

#create app instance
app = create_app()


#register blueprint
app.register_blueprint(test_bp)

if __name__ == "__main__":
    #add host as 0.0.0.0 to be accessible from outside when running as a #container
    #app.run(host='0.0.0.0')
    app.run(debug=True, port=5000, host='0.0.0.0')