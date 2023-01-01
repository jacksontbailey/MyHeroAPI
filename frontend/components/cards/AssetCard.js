const AssetCard = ({ data }) => {
    return (
      <div>
        <h2>{data.name}</h2>
        <p>Type: {data.type}</p>
      </div>
    );
};

export default AssetCard;