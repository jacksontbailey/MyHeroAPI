import React from 'react';
import Card from './Card';

const CardList = ({ cards }) => {
  return (
    <div className="card-list">
      {cards.map((card) => (
        <Card key={card.id} data={card} />
      ))}
    </div>
  );
};

export default CardList;
