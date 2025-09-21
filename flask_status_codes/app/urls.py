from .views import *

def register_routes(app):
    app.add_url_rule('/user', view_func=get_user, methods=['GET'])
    app.add_url_rule('/user', view_func=create_user, methods=['POST'])
    app.add_url_rule('/user', view_func=delete_user, methods=['DELETE'])
    app.add_url_rule('/redirect-old', view_func=old_route)
    app.add_url_rule('/redirect-new', view_func=new_route, endpoint='new_route')
    app.add_url_rule('/bad-request', view_func=bad_request, methods=['POST'])
    app.add_url_rule('/protected', view_func=protected_route, methods=['GET'])
    app.add_url_rule('/forbidden', view_func=forbidden_route, methods=['GET'])
    app.add_url_rule('/only-post', view_func=method_not_allowed, methods=['GET', 'POST'])
    app.add_url_rule('/timeout', view_func=delayed_response, methods=['GET'])
    app.add_url_rule('/rate-limit', view_func=rate_limited, methods=['GET'])
    app.add_url_rule('/server-error', view_func=cause_error, methods=['GET'])

