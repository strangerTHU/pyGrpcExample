import Example_pb2
import Example_pb2_grpc
import grpc
import time

channel = grpc.insecure_channel("localhost:8888")
stub = Example_pb2_grpc.GreeterStub(channel)
#  异步方法获取响应
# response_future = stub.SayHello.future(
#     Example_pb2.HelloRequest(name="MyName!"))
# print(response_future.result().reply)
nameList = ["Alice", "Bob", "Cindy"]


def GenerateName():
    for name in nameList:
        yield Example_pb2.HelloRequest(name=name)
        time.sleep(1)


names = GenerateName()
response = stub.LotsOfGreetings(names)
print(response)
