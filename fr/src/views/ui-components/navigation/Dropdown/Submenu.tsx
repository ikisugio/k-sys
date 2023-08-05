import Dropdown from '@/components/ui/Dropdown'

const Submenu = () => {
    return (
        <Dropdown title="Click Me!">
            <Dropdown.Item>Item 1</Dropdown.Item>
            <Dropdown.Menu title="Right Item 2">
                <Dropdown.Menu title="Item 2-1">
                    <Dropdown.Item active>Item 2-1-1</Dropdown.Item>
                    <Dropdown.Item>Item 2-1-2</Dropdown.Item>
                    <Dropdown.Item>Item 2-1-3</Dropdown.Item>
                </Dropdown.Menu>
                <Dropdown.Item>Item 2-2</Dropdown.Item>
                <Dropdown.Item>Item 2-3</Dropdown.Item>
            </Dropdown.Menu>
            <Dropdown.Menu title="Right Item 3">
                <Dropdown.Menu title="Item 3-1">
                    <Dropdown.Item>Item 3-1-1</Dropdown.Item>
                    <Dropdown.Item>Item 3-1-2</Dropdown.Item>
                    <Dropdown.Item>Item 3-1-3</Dropdown.Item>
                </Dropdown.Menu>
                <Dropdown.Item>Item 3-2</Dropdown.Item>
                <Dropdown.Item>Item 3-3</Dropdown.Item>
            </Dropdown.Menu>
            <Dropdown.Item>Item 4</Dropdown.Item>
        </Dropdown>
    )
}

export default Submenu
