import { useState } from 'react';

function Todo(props) {
    const [modalIsOpen, setModalIsOpen] = useState(false); //State is not open (false), only work with setModalIsOpen

    function deleteHandler() {
        setModalIsOpen(true); //change Modal to closed (true), and to render modalIsOpen to use the JSX code.
    }


    /* JSX Code */
    return (
        <div className='card'>
            <h2>{props.text}</h2>
            <div className='actions'>
                <button className='btn' onClick={deleteHandler}>Delete</button>
            </div>
        </div>
    );
}

export default Todo;
