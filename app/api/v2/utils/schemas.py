user_schema={
	"type": "object",
    "properties": {
        
        "username": {type: "string"},
        "email": {type: "string"},
        "password": {type: "string"},
        "role": {type: "string"}

    },
"required": ["username","email","password","role"]
}

products_schema={
	"type": "object",
    "properties": {
        
        "product_name": {type: "string"},
        "category": {type: "string"},
        "price": {type: "string"},
        "quantity": {type: "integer"},
        
    },
"required": ["product_name","category","price","quantity"]
}
sales_schema={
	"type": "object",
    "properties": {
        "product_id": {type: "integer"},
        "quantity": {type: "integer"},
        "attendant": {type: "string"},
        
        
        
    },
"required": ["product_id", "quantity","attendant",]
}


