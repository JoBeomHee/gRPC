using gRPCInterceptorSample.Interceptors;

namespace gRPCInterceptorSample.Extensions
{
    public static class ModelValidationExtension
    {
        public static IServiceCollection AddValidation(this IServiceCollection services, IConfiguration configuration)
        {
            services.AddSingleton<IValidatorErrorMessageHandler, DefaultErrorMessageHandler>();
            services.AddScoped<IValidatorLocator>(p => new ServiceCollectionValidationProvider(p));

            return services;
        }
    }
}