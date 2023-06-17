import React from 'react';
import Card from './Card';
import TextBox from '../textbox/TextBox';

const CardList = ({ cards }) => {
  return (
    <section className='card-list-flex'>
      <div className="card-list">
        {cards.map((card) => (
          <TextBox
            key={card.id}
            title={card.id}
            content={<Card key={card.id} data={card} />}
          />
        ))}
      </div>
    </section>
  );
};

export default CardList;
