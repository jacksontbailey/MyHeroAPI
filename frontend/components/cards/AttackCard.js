const AttackCard = ({ data }) => {
    return (
      <div>
        <h2>{data.name}</h2>
        <p>Ability: {data.ability}</p>
        <p>Attack Keywords: {data.attack_keywords.join(', ')}</p>
        <p>Attack Zone: {data.attack_zone}</p>
        <p>Damage: {data.damage}</p>
        <p>Speed: {data.speed}</p>
        <p>Type: {data.type}</p>
      </div>
    );
};

export default AttackCard;