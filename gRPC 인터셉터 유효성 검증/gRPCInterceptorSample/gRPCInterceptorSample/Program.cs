using gRPCInterceptorSample.Extensions;
using gRPCInterceptorSample.Interceptors;
using gRPCInterceptorSample.Services;

var configuration = new ConfigurationBuilder()
    .SetBasePath(Directory.GetCurrentDirectory())
    .AddJsonFile("appsettings.json", false, true)
    .AddEnvironmentVariables()
    .Build();

var builder = WebApplication.CreateBuilder(args);

// Additional configuration is required to successfully run gRPC on macOS.
// For instructions on how to configure Kestrel and gRPC clients on macOS, visit https://go.microsoft.com/fwlink/?linkid=2099682

builder.Services.AddValidation(configuration);
builder.Services.AddAccountValidator(configuration);

// Add services to the container.
builder.Services.AddGrpc(options =>
{
    options.Interceptors.Add<ServerLoggingInterceptor>();
    options.Interceptors.Add<ValidationInterceptor>();
});

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<GreeterService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
