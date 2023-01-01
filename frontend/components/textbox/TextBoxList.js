import TextBox from './TextBox';

const TextBoxList = ({ data }) => {

    return (
        <div className='text-box-list'>
            <p>Total cards: {data.length}</p>
            {(data) 
                ? data.map((card) => (
                    <TextBox
                        key={`${card.id}`}
                        title = {card.title}
                        content = {card.content}
                    />
                    ))
                : null }
        </div>
    );
};

export default TextBoxList;