from jsonschema import validate
from jsonschema.exceptions import ValidationError
from jsonschema.exceptions import SchemaError
import json
def test_product_schema():
    with open("product.json") as f:
        product = json.load(f)
    with open("product_schema.json") as f:
        schema = json.load(f)
    try:
        validate(product, schema)
    except ValidationError as e:
        assert False, e
    except SchemaError as e:
        assert False, e
    assert True
    
{ } # JSON payload
    ]
}
