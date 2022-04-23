using FluentValidation;

namespace gRPCInterceptorSample.Interceptors
{
    public class ServiceCollectionValidationProvider : IValidatorLocator
    {
        private readonly IServiceProvider _provider;

        public ServiceCollectionValidationProvider(IServiceProvider provider)
        {
            _provider = provider;
        }

        public bool TryGetValidator<TRequest>(out IValidator<TRequest> result) where TRequest : class
        {
            return (result = _provider.GetService<IValidator<TRequest>>()) != null;
        }
    }
}