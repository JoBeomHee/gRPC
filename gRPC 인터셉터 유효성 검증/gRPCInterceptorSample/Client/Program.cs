using Grpc.Net.Client;
using gRPCInterceptorSample;


using var channel = GrpcChannel.ForAddress("https://localhost:7081");

var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(
    new HelloRequest { Name = "Beom12312312312312312312" }
    );

Console.WriteLine($"Greeting {reply.Message}");
