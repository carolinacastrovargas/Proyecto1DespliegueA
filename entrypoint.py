
from app import create_app

#app = create_app()

if __name__=='__main__':
    from app import create_app
    app = create_app()
    app.run(debug=False,use_reloader=False,host="0.0.0.0", port=8081)

    
