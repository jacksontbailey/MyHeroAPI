import TextBox from './TextBox';

const TextBoxList = ({ data }) => {
    return (
        <section className='text-box-flex'>
            <div className='text-box-list'>
                <p className='text-box-list__count-key'>count: 
                    <span className='text-box-list__count-value'> {data.length}</span>
                </p>
                {(data) 
                    ? data.map((card, index) => (
                        card.title ? (
                            <TextBox
                                cardKey={card.cardKey}
                                cardNumber={card.cardNumber}
                                content={[{name: card.title}, {url: card.content}]}
                                key={index}
                            />
                        ) : null
                    ))
                    : null}
            </div>
        </section>
    );
};

export default TextBoxList;
