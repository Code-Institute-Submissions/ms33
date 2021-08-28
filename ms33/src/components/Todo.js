import { useState } from 'react';

import Modal from './Modal';
import Backdrop from './Backdrop';

function Todo(props) {
    const [modalIsOpen, setModalIsOpen] = useState(false); //initial State is not open (false), only work with setModalIsOpen

    function deleteHandler(props) {
        setModalIsOpen(true); //change Modal to closed (true), and to render modalIsOpen to use the JSX code.
    }

    function closeModalHandler() {
        setModalIsOpen(false);
    }

    /* JSX Code */
    return (
        <div className='card'>
            <h2>{props.text}</h2>
            <div className='actions'>
                <button className='btn' onClick={deleteHandler}>Delete</button>
            </div>
            {modalIsOpen && (
                <Modal onCancel={closeModalHandler} onConfirm={closeModalHandler} />
            )}
            {modalIsOpen && <Backdrop onCancel={closeModalHandler} />}
        </div>
    );
}

export default Todo;
