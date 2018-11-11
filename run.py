import os
from app import create_app

app =create_app(os.getenv('APP_SETTINGS'))


from app.manage import migrate

migrate()

if __name__ == '__main__':
	port= int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0', port=port)
