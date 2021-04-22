from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import pandas as pd
import json
import io

application = Flask(__name__)
CORS(application)


@application.route('/api/action/scraping/table', methods=['POST'])
def table_scraping():
    output = io.StringIO()
    data = json.loads(request.data)

    dataFrame = pd.read_html(data['data'])[0]
    dataFrame.to_csv(output)

    return make_response(
        jsonify(
            {
                'output': output.getvalue(),
                'html': dataFrame.to_html()
            }
        ),
        200
    )


if __name__ == '__main__':
    application.run(
        host='127.0.0.1',
        port=3000,
        debug=True
    )
