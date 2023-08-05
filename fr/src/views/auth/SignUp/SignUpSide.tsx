import SignUpForm from '@/views/auth/SignUp/SignUpForm'
import Side from '@/components/layouts/AuthLayout/Side'

const SignUpSide = () => {
    return (
        <Side
            content={
                <>
                    <h3 className="mb-1">新規登録</h3>
                    <p>以下の情報を入力してください</p>
                </>
            }
        >
            <SignUpForm disableSubmit={true} signInUrl="/auth/sign-in-side" />
        </Side>
    )
}

export default SignUpSide
