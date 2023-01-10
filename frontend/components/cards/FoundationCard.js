const FoundationCard = ({ data }) => {
  return (
    <div className="card-type__foundation">
      <p>Type: {data.type}</p>
    </div>
  );
};

export default FoundationCard;