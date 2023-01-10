const ActionCard = ({ data }) => {
    return (
      <div className="card-type__action">
        <p>Type: {data.type}</p>
      </div>
    );
};

export default ActionCard;