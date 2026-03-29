import zvec

schema = zvec.CollectionSchema(
    fields=[
        zvec.FieldSchema(name="id", data_type=zvec.DataType.STRING)
    ],
    vectors=[
        zvec.VectorSchema(name="vector", data_type=zvec.DataType.VECTOR_FP32, dim=2)
    ]
)

collection = zvec.Collection(name="default", schema=schema)
collection.insert(documents=[{"id": "1", "vector": [0.1, 0.2]}])
collection.optimize()

results = collection.query(vector=[0.1, 0.2], top_k=5)
print(results)
