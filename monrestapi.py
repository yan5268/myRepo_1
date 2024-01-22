#!/usr/bin/env python


from flask import Flask, jsonify, request


app = Flask(__name__)



@app.route('/')
def index():
	return 'Monitoring REST API Server...\n\n'

@app.route('/hello', methods=['GET'])
def runMonModule():
	if (request.method == 'GET'):
		data = {"data": "Hello World"}
		return jsonify(data)


@app.route('/HAHA', methods=['GET'])
def runMonModule_HAHA():
	if (request.method == 'GET'):
		data = {"data": "HAHA..."}
		return jsonify(data)




if __name__ == '__main__':
	
	#if not os.path.exists(sitedataFile):
	#	with open(sitedataFile,'w') as f:
	#		json.dump(SiteData, f, indent = 4)
	app.run(host='0.0.0.0',port=9001)
