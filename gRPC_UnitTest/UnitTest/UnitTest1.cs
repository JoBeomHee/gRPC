using gRPC_UnitTest;
using gRPC_UnitTest.Services;
using Microsoft.Extensions.Logging;
using Moq;
using System.Threading.Tasks;
using Xunit;

namespace UnitTest
{
    public class UnitTest1
    {
        [Fact]
        public async Task SayHelloTest()
        {
            // Arrange
            var loggerFactory = new LoggerFactory();
            ILogger<GreeterService> logger = loggerFactory.CreateLogger<GreeterService>();
            var mockGreeter = new Mock<IGreeter>();
            mockGreeter.Setup(
                m => m.Greet(It.IsAny<string>())).Returns((string s) => $"Hello {s}");
            var service = new GreeterService(logger, mockGreeter.Object);

            // Act
            var response = await service.SayHello(
        new HelloRequest { Name = "Joe" }, TestServerCallContext.Create());

            // Assert
            mockGreeter.Verify(v => v.Greet("Joe"));
            Assert.Equal("Hello Joe", response.Message);
        }
    }
}