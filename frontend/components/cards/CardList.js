import React from 'react';
import Card from './Card';
import TextBox from '../textbox/TextBox';

const CardList = ({ cards }) => {
  return (
    <div className="card-list">
      {cards.map((card) => (
        <TextBox
          key={card.id} 
          title={card.name} 
          content={<Card key={card.id} data={card} />} 
        />
      ))}
    </div>
  );
};

export default CardList;
