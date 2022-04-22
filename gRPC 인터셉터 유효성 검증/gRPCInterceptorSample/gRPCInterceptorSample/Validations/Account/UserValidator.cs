using FluentValidation;

namespace gRPCInterceptorSample.Validations.Account
{
    public class UserValidator : BaseValidator<HelloRequest>
    {
        public UserValidator(IConfiguration configuration) : base(configuration)
        {
            RuleFor(greeter => greeter.Name).Length(1, 5).WithMessage("메시지 글자 범위를 초과하였습니다.");
        }
    }
}

public class BaseValidator<T> : AbstractValidator<T> where T : class
{
    protected readonly IConfiguration Configuration;

    public BaseValidator(IConfiguration configuration)
    {
        Configuration = configuration ?? throw new ArgumentNullException();
    }
}