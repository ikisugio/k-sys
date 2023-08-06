import SignInForm from './SignInForm'

const SignIn = () => {
    return (
        <>
            <div className="mb-8">
                <h3 className="mb-1">KaigoManager</h3>
                <p>ログイン画面</p>
            </div>
            <SignInForm disableSubmit={false} />
        </>
    )
}

export default SignIn
