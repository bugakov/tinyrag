import zvec

schema = zvec.CollectionSchema(
    name="test",
    vectors=[zvec.VectorSchema(name="vector", data_type=zvec.DataType.VECTOR_FP32, dimension=2)],
)

collection = zvec.create_and_open(path="./zvec_example", schema=schema)

collection.insert([
    zvec.Doc(id="1", vectors={"vector": [0.1, 0.2]}),
    zvec.Doc(id="2", vectors={"vector": [0.9, 0.8]}),
])

results = collection.query(
    zvec.VectorQuery("vector", vector=[0.1, 0.2]),
    topk=5,
)

print(results)
