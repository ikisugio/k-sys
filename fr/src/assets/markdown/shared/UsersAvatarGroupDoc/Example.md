```jsx
import UsersAvatarGroup from '@/components/shared/UsersAvatarGroup'

const data = [
    {
        userName: '顧客１さん',
        avatarImg: '/img/avatars/thumb-3.jpg',
    },
    {
        userName: 'Carolyn Hanson',
        avatarImg: '/img/avatars/thumb-9.jpg',
    },
    {
        userName: 'Samantha Phillips',
        avatarImg: '/img/avatars/thumb-6.jpg',
    },
    {
        userName: 'Ella Robinson',
        avatarImg: '/img/avatars/thumb-15.jpg',
    },
]

const Example = () => {
    return (
        <UsersAvatarGroup
            nameKey="userName"
            imgKey="avatarImg"
            avatarProps={{ size: 40 }}
            users={data}
        />
    )
}

export default Example
```
