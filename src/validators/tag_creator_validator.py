from cerberus import Validator
from src.errors.error_types.http_unprocessable_entity import HttpunprocessableEntityError

def tag_creator_validator(resquest: any) -> None:
    body_validator = Validator({
        "product_code": {"type": "string", "required": True, "empty": False}

    })

    response = body_validator.validate(resquest.json)

    if response is False:
        raise HttpunprocessableEntityError(body_validator.errors)
