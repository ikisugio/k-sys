import SignInForm from '@/views/auth/SignIn/SignInForm'
import Side from '@/components/layouts/AuthLayout/Side'

const SignInSide = () => {
    return (
        <Side
            content={
                <>
                    <h3 className="mb-1">KaigoManager</h3>
                    <p>ログインしてください</p>
                </>
            }
        >
            <SignInForm
                disableSubmit={true}
                signUpUrl="/auth/sign-up-side"
                forgotPasswordUrl="/auth/forgot-password-side"
            />
        </Side>
    )
}

export default SignInSide
