import SignUpForm from '@/views/auth/SignUp/SignUpForm'
import Simple from '@/components/layouts/AuthLayout/Simple'

const SignUpSimple = () => {
    return (
        <Simple
            content={
                <div className="mb-4">
                    <h3 className="mb-1">新規登録</h3>
                    <br></br>
                </div>
            }
        >
            <SignUpForm disableSubmit={true} signInUrl="/auth/sign-in-simple" />
        </Simple>
    )
}

export default SignUpSimple
