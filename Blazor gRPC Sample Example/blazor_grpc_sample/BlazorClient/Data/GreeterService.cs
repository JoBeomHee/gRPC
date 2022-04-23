using Grpc.Net.Client;

namespace BlazorClient.Data
{
    public class GreeterService
    {
        public async Task<string> SayHello(string name)
        {
            using var httpClientHandler = new HttpClientHandler
            {
                ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator
            };

            using var httpClient = new HttpClient(httpClientHandler);
            using var channel = GrpcChannel.ForAddress("https://localhost:7005", new GrpcChannelOptions { HttpClient = httpClient });

            var client = new Greeter.GreeterClient(channel);
            var reply = await client.SayHelloAsync(
                    new HelloRequest { Name = name });

            return reply.Message;

        }
    }
}
