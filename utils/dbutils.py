from starlette.requests import Request

# middlewareでrequestに格納したconnection(Databaseオブジェクト)を返します。


def get_connection(request: Request):
    return request.state.connection
