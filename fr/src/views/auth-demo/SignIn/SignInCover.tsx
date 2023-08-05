import SignInForm from '@/views/auth/SignIn/SignInForm'
import Cover from '@/components/layouts/AuthLayout/Cover'

const SignInCover = () => {
    return (
        <Cover
            content={
                <>
                    <h3 className="mb-1">ろぐいん３</h3>
                    <p>Please enter your credentials to sign in!</p>
                </>
            }
        >
            <SignInForm
                disableSubmit={true}
                signUpUrl="/auth/sign-up-cover"
                forgotPasswordUrl="/auth/forgot-password-cover"
            />
        </Cover>
    )
}

export default SignInCover
