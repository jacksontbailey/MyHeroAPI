const TextBoxList = ({ data }) => {
    return (
        <section className='text-box-flex'>
            <div className='text-box-list'>
                <p className='text-box-list__count-key'>count:
                    <span className='text-box-list__count-value'> {data.length}</span>
                </p>
                {(data) ? data : null}
            </div>
        </section>
    );
};

export default TextBoxList;
