import SignUpForm from '@/views/auth/SignUp/SignUpForm'
import Cover from '@/components/layouts/AuthLayout/Cover'

const SignUpCover = () => {
    return (
        <Cover
            content={
                <>
                    <h3 className="mb-1">新規登録</h3>
                    <p>以下の情報を入力してください</p>
                </>
            }
        >
            <SignUpForm disableSubmit={true} signInUrl="/auth/sign-in-cover" />
        </Cover>
    )
}

export default SignUpCover
