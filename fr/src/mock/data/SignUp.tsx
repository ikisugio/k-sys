import SignUpForm from './SignUpForm'

const SignUp = () => {
    return (
        <>
            <div className="mb-8">
                <h3 className="mb-1">新規登録</h3>
                <p>以下の情報を入力してください</p>
            </div>
            <SignUpForm disableSubmit={false} />
        </>
    )
}

export default SignUp
