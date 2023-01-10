const AssetCard = ({ data }) => {
    return (
      <div className="card-type__asset">
        <p>Type: {data.type}</p>
      </div>
    );
};

export default AssetCard;