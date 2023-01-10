import { useState } from "react";

const CardData = ({ data }) => {
  const [showImage, setShowImage] = useState(false);

  return (
    <>
      <p>Description: {data.description.join(', ')}</p>
      <p>Set: {data.set}</p>
      <p>Block Modifier: {data.block_modifier}</p>
      <p>Block Zone: {data.block_zone}</p>
      <p>Check: {data.check}</p>
      <p>ID: {data.id}</p>
      <div style={{ position: "relative" }}>
        <p>Image: {data.image_url && (
                    <a href={data.image_url} onMouseEnter={() => setShowImage(true)} onMouseLeave={() => setShowImage(false)}>
                      {data.image_url}
                    </a>
                  )}
        </p>

        {showImage && (
          <div style={{ position: "absolute", top: "100%", left: '25%' }}>
            <img src={data.image_url} alt={data.name} />
          </div>
        )}
        
      </div>
      {data.keyword && <p>Keyword: {data.keyword.join(', ')}</p>}
      <p>Play Difficulty: {data.play_difficulty}</p>
      <p>Rarity: {data.rarity}</p>
      <p>Symbols: {data.symbols.join(', ')}</p>
    </>
  );
};
export default CardData;