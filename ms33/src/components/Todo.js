function Todo(props) {
    return (
        <div className='card'>
            <h2>{props.text}</h2>
            <div className='actions'>
                <button className='btn' onClick={ }>Delete</button>
            </div>
        </div>
    );
}

export default Todo;
