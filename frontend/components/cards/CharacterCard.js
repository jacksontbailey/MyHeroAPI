const CharacterCard = ({ data }) => {
    return (
      <div className="card-type__character">
        <p>Max Health: {data.max_health}</p>
        <p>Starting Hand Size: {data.starting_hand_size}</p>
        <p>Type: {data.type}</p>
      </div>
    );
};

export default CharacterCard;