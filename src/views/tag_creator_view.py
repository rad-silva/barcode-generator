from src.views.http_types.http_request import HttpResquest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with HTTP
    '''

    def validate_and_create(self, http_request: HttpResquest) -> HttpResponse:
        #body = http_request.body
        #product_code = body["product_code"]

        # lógica de regra de negócio
        print('Estou naminha view')
        print(http_request)

        # retorno http
        return HttpResponse(status_code=200, body={"hello":"world"})
