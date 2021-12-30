from flask import jsonify
from flask_restx import Resource, Namespace, reqparse, abort

from service.query import QueryService

parser = reqparse.RequestParser()
parser.add_argument("cmd1")
parser.add_argument("value1")
parser.add_argument("cmd2")
parser.add_argument("value2")
parser.add_argument("file_name")

queries_ns = Namespace("perform_query")


@queries_ns.route("/")
class QueryView(Resource):

    @queries_ns.expect(parser)
    def post(self):
        args = parser.parse_args()
        try:
            user_query = QueryService(args)
        except ValueError as e:
            abort(400, str(e))
        result = user_query.get_result()
        return jsonify(result)



