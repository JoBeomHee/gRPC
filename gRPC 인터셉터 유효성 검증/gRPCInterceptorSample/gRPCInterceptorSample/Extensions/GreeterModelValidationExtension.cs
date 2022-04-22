using FluentValidation;
using gRPCInterceptorSample.Validations.Account;

namespace gRPCInterceptorSample.Extensions
{
    public static class GreeterModelValidationExtension
    {
        public static IServiceCollection AddAccountValidator(this IServiceCollection services, IConfiguration configuration)
        {
            services.AddTransient<IValidator<HelloRequest>, UserValidator>();

            return services;
        }
    }
}
