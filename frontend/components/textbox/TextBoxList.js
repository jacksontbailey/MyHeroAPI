import TextBox from './TextBox';

const TextBoxList = ({ data }) => {
    return (
        <div className='text-box-list'>
            <p>Total cards: {data.length}</p>
            {(data) 
                ? data.map((card, index) => (
                    card.title ? (
                        <TextBox
                            title={card.title}
                            cardKey={card.cardKey}
                            cardNumber={card.cardNumber}
                            content={card.content}
                            key={index}
                        />
                    ) : null
                ))
                : null}
        </div>
    );
};

export default TextBoxList;
