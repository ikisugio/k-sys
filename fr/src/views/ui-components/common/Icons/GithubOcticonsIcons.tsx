import IconWrapper from './IconWrapper'
import {
    // GoOctoface,
    GoFlame,
    // GoMarkGithub,
    GoGitCompare,
    GoGitCommit,
    GoGitPullRequest,
    GoCode,
    // GoMarkdown,
    GoTerminal,
} from 'react-icons/go'
import {
    VscGithub,
} from 'react-icons/vsc'
import {
    FaGithub,
    FaMarkdown
} from 'react-icons/fa'

const renderIcon = [
    { render: () => <FaGithub /> },
    { render: () => <GoFlame /> },
    { render: () => <VscGithub /> },
    { render: () => <GoGitCompare /> },
    { render: () => <GoGitCommit /> },
    { render: () => <GoGitPullRequest /> },
    { render: () => <GoCode /> },
    { render: () => <FaMarkdown /> },
    { render: () => <GoTerminal /> },
]

const GithubOcticonsIcons = () => {
    return (
        <div className="grid grid-cols-3 gap-y-6 text-4xl text-center heading-text">
            {renderIcon.map((icon, index) => (
                <IconWrapper key={`githubOcticonsIcons-${index}`}>
                    {icon.render()}
                </IconWrapper>
            ))}
        </div>
    )
}

export default GithubOcticonsIcons
