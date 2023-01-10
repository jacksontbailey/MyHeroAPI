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
                <section>
                    <h2>{data.name}</h2>
                    <CharacterCard data={data.type_attributes} />
                    <CardData data={data} />
                </section>
            );

        case 'Attack':
            return (
                <section>
                    <h2>{data.name}</h2>
                    <AttackCard data={data.type_attributes} />
                    <CardData data={data} />
                </section>
            );

        case 'Asset':
            return (
                <section>
                    <h2>{data.name}</h2>
                    <AssetCard data={data.type_attributes} />
                    <CardData data={data} />
                </section>
            );

        case 'Action':
            return (
                <section>
                    <h2>{data.name}</h2>
                    <ActionCard data={data.type_attributes} />
                    <CardData data={data} />
                </section>
            );

        case 'Foundation':
            return (
                <section>
                    <h2>{data.name}</h2>
                    <FoundationCard data={data.type_attributes} />
                    <CardData data={data} />
                </section>
            );

        default:
            //return null;
    }
};

export default Card;