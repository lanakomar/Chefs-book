import blank from '../../images/blank-state-image.png';


const EmtyGroceryList = () => {
    return (
        <div className='emptyGL'>
            <div className='empty-list'>
                <img src={blank} alt="empty-grocery-list" />
            </div>
            <h3>Build Your Grocery List</h3>
            <p>Add recipes you plan to cook.</p>
            <p> Adjust what you need to buy.</p>
        </div>
    )
};

export default EmtyGroceryList;
