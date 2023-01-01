import CharacterCard from './CharacterCard';
import AttackCard from './AttackCard';
import AssetCard from './AssetCard';
import ActionCard from './ActionCard';
import FoundationCard from './FoundationCard';
import CardData from './CardData';

const Card = ({ data }) => {
    if (!data.type_attributes) {
        return null;
    }

    switch (data.type_attributes.type) {
        case 'Character':
            return (
                <div>
                    <CharacterCard data={data.type_attributes} />
                    <CardData data={data} />
                </div>
            );

        case 'Attack':
            return (
                <div>
                    <AttackCard data={data.type_attributes} />
                    <CardData data={data} />
                </div>
            );

        case 'Asset':
            return (
                <div>
                    <AssetCard data={data.type_attributes} />
                    <CardData data={data} />
                </div>
            );

        case 'Action':
            return (
                <div>
                    <ActionCard data={data.type_attributes} />
                    <CardData data={data} />
                </div>
            );

        case 'Foundation':
            return (
                <div>
                    <FoundationCard data={data.type_attributes} />
                    <CardData data={data} />
                </div>
            );

        default:
            //return null;
    }
};

export default Card;